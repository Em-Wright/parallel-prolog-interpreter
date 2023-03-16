open Core
open Async
open Include
open Ast
open Util

let (fresh, reset, update) =
  let nxt = ref 0 in
  let f () = (nxt := !nxt + 1; !nxt) in
  let r () = nxt := 0 in
  let u n = nxt := Int.max !nxt n in
  (f, r, u)

let rename_vars_in_dec d =
  match d with
  | Clause (h, b) ->
    let head_vars = find_vars [h] in
    let body_vars = find_vars b in
    (* find uniq vars from both head and body *)
    let vars : exp list = uniq (head_vars @ body_vars) in
    (* get fresh variable mappings *)
    let sub = List.map ~f:(fun x -> (x, VarExp (fresh() |> Int.to_string))) vars in
    (* substitute new names for variables *)
    Clause (sub_lift_goal sub h, sub_lift_goals sub b)
  | Query (b) ->
    (* find uniq vars in query *)
    let body_vars = find_vars b in
    (* get fresh variable mappings *)
    let vars = uniq (body_vars) in
    let sub = List.map ~f:(fun x -> (x, VarExp (fresh() |> Int.to_string))) vars in
    (* substitute new names for variables *)
    Query (sub_lift_goals sub b)

module Job = struct
  type t = {
    goals : (exp * int) list;
    env : ((exp * exp) list);
    path : (int*int) list
  } [@@deriving bin_io, fields]
end

module Job_and_nxt = struct
  type t = Job.t * int [@@deriving bin_io]
end

module Job_and_bool_and_vars = struct
  type t = Job.t * int * bool * String.Set.t [@@deriving bin_io]
end

module Dec = struct
  type t = dec [@@deriving bin_io]
end

module Results = struct
  type t = ((exp * exp) list * (int*int) list )list [@@deriving bin_io]

  let reverse_path_order t : t =
    List.map t ~f:( fun (env, path) -> (env, List.rev path))
end

module Worker_to_toplevel = struct
  type t =
    Results of Results.t
    | Job of Job_and_nxt.t
    | Cut of (int*int) list
  [@@deriving bin_io]
end

module Toplevel_to_worker = struct
  type t =
    Work_request
    | Cut of (int*int) list
  [@@deriving bin_io]
end

let remove_due_to_cut path cut_path =
  let rec loop p cp =
    match p, cp with
    | (x,dx)::_, (y, dy)::[] -> if x > y && dx=dy then true else false
    | (x,dx)::xs, (y, dy)::ys -> if x = y && dx=dy then loop xs ys else false
    | _,_ -> false
  in
  loop path (List.rev cut_path)

let rec truncate path depth =
  match path with
  | (_, d)::p -> if d > depth then truncate p depth else  path
  | [] -> []

module T = struct

  module Worker_state = struct
    type init_arg = (dec list * int)
    [@@deriving bin_io]

    type t = {
      q : Job.t Deque.t;
      index : int;
      mutable db : dec list;
      mutable reader : Toplevel_to_worker.t Pipe.Reader.t;
      mutable writer : Worker_to_toplevel.t Pipe.Writer.t
    } [@@deriving fields]
  end

  module Connection_state = struct
    type init_arg = unit [@@deriving bin_io]
    type t = unit
  end

  (* eval takes
     - a list of goals to prove (exp list)
     - the environment to prove them in ((exp * exp) list)
     - the database of rules to use to prove them (dec list)
     and returns the remainder of work to be done before this job is complete.
     This is in the form of a list of jobs, each containing a list of goals
     to prove, and an updated environment to prove them in. ((exp list) * ((exp * exp) list)) list.

     The function itself performs one step of evaluation on the job it is given, and
     either manages to prove it, returning the empty list, or generates one or more other
     jobs to be done.
  *)
  let eval gs env db path =
    match gs with
    | (g1, depth)::gl -> (
        (* we have at least one more subgoal (g1) to prove in this job *)
        match g1 with
        | TermExp ("false", []) -> [], None
        | TermExp("true", []) -> [ (gl, env, path)], None
        | TermExp("cut", []) ->
          let truncated = truncate path (depth ) in
          [(gl, env, path)], Some truncated
        | TermExp("equals", [lhs; rhs]) -> (
            match unify [(lhs, rhs)] with
            | Some s -> (
                match unify (s@env) with
                | Some env2 -> [(sub_lift_goals_cut s gl, env2, path)], None
                | None -> [], None
              )
            | None -> [], None
          )
        | TermExp("not_equal", [lhs;rhs]) -> (
            match unify [(lhs, rhs)] with
            | Some s -> (
                match unify (s@env) with
                | Some _ -> [], None
                | None -> [(gl, env, path)], None
              )
            | None -> [ (gl, env, path) ], None
          )
        | TermExp("greater_than", [lhs; rhs]) -> (
            match lhs, rhs with
            | IntExp i1, IntExp i2 -> if i1 > i2 then [(gl, env, path)], None else [], None
            | _ -> [], None (* arguments insufficiently instantiated *)
          )
        | TermExp("less_than", [lhs; rhs]) ->
          (
            match lhs, rhs with
            | IntExp i1, IntExp i2 -> if i1 < i2 then [(gl, env, path)], None else [], None
            | _ -> [], None (* arguments insufficiently instantiated *)
          )
        | TermExp("greater_than_or_eq", [lhs; rhs]) -> (
            match lhs, rhs with
            | IntExp i1, IntExp i2 -> if i1 >= i2 then [(gl, env, path)], None else [], None
            | _ -> [], None (* arguments insufficiently instantiated *)
          )
        | TermExp("less_than_or_eq", [lhs; rhs]) ->
          (
            match lhs, rhs with
            | IntExp i1, IntExp i2 -> if i1 <= i2 then [(gl, env, path)], None else [],None
            | _ -> [], None (* arguments insufficiently instantiated *)
          )
        | TermExp("is", [lhs; rhs]) -> (
            (* evaluate the arithmetic expressions with current substitutions, then check if it is
                 possible to unify them with any additional substitutions *)
            match rhs with
            | ArithmeticExp (op, t1, t2) -> (
                match t1, t2 with
                | ArithmeticInt i1, ArithmeticInt i2 -> (
                    let result = perform_arithmetic op i1 i2 in
                    match lhs with
                      | VarExp _ -> (
                          match unify ((lhs, IntExp result)::env) with
                          | Some env2 ->
                            [ (
                              sub_lift_goals_cut [(lhs, IntExp result)] gl,
                              env2,
                              path
                            )], None
                          | None -> [], None
                        )
                      | IntExp i -> if i = result then [(gl, env, path)], None else [], None
                      | _ -> [], None
                    )
                  | _ -> [], None
              )
            | IntExp result -> (
                match lhs with
                | VarExp _ ->
                  ( match unify ((lhs, rhs)::env) with
                    | Some env2 ->
                      [(
                        sub_lift_goals_cut [(lhs, rhs)] gl,
                        env2,
                        path
                      )], None
                    | None -> [], None
                  )
                | IntExp i -> if i = result then [(gl, env, path)], None else [], None
                | _ -> [], None
              )
            | _ -> [], None
          )
        (* if goal is some other predicate *)
        | TermExp(_,_) -> (
            List.foldi db ~init:[]
              ~f:(fun i acc rule ->
                  match (rename_vars_in_dec rule) with
                  | Clause (h, body) -> (
                      (* check if this rule can be used for this subgoal *)
                      match unify [(g1, h)] with
                      | Some s -> (
                          match unify (s@env) with
                          | Some env2 -> (
                              if (List.length body = 1)
                              then (
                                match body with
                                (* if the rule proved the subgoal (ie. rule was a
                                     fact) then recurse on remaining subgoals
                                *)
                                | ((TermExp ("true", _)) :: _) ->
                                  (
                                    sub_lift_goals_cut s gl,
                                    env2,
                                    (i, depth+1)::path
                                  )::acc
                                | _ ->
                                  let body2 = sub_lift_goals s body |> List.map ~f:(fun a -> a, (depth+1)) in
                                  (
                                    body2 @ (sub_lift_goals_cut s gl),
                                    env2,
                                    (i, depth + 1)::path
                                  )::acc
                              )
                              else
                                let body2 = sub_lift_goals s body |> List.map ~f:(fun a -> a, (depth+1)) in
                                (
                                  body2 @ (sub_lift_goals_cut s gl),
                                  env2,
                                  (i, depth+1)::path
                                )::acc
                            )
                          | _ -> acc
                        )
                      (* this rule's head doesn't unify with the subgoal *)
                      | _ -> acc
                    )
                  |  _ -> acc
                )), None
        (* subgoal g1 isn't a TermExp *)
        | _ -> [(gl, env, path)], None
      )
    | [] -> [], None
  ;;

  (* main takes the worker state and returns unit
     It loops, checking for and then handling updates from the toplevel, before
     taking a job from the stack and calling `eval' on it.
     It sends results or work back to the toplevel via the `writer' pipe in
     the worker_state.
     It returns when it no longer has any work on its stack.
  *)
  let main (worker_state : Worker_state.t) send_initial_jobs_bool orig_vars =
    (* Clear the pipe of any previous requests for work which
    are no longer relevant *)
    Pipe.clear worker_state.reader;
    let handle_job (goals, env, path2) =
      let goals2, _ = List.unzip goals in
      let vars_set_string = String.Set.of_list (find_vars_string goals2) |> String.Set.union orig_vars
      in
      let env =
        List.filter env ~f:(fun (v, _) ->
            match v with
            | VarExp elt -> String.Set.exists vars_set_string ~f:(fun a -> String.equal elt a)
            | _ -> false
          )
      in
      Deque.enqueue_back worker_state.q {goals; env; path=path2}
    in
    let init_results = match Deque.dequeue_back worker_state.q with
    | None -> []
    | Some {goals =[]; env; path} -> [(env, path)]
    | Some {goals; env; path} -> (
        let jobs, cut =
          ( eval goals env worker_state.db path) in
        (
          match cut with
          | Some cut -> Pipe.write_without_pushback worker_state.writer (Cut cut);
            List.iter jobs
              ~f:( fun (goals, env, path2) ->
                  if not (remove_due_to_cut path2 cut) then (
                    handle_job (goals, env, path2)
                ))
          | None ->
            List.iter jobs
              ~f:( fun (goals, env, path2) -> handle_job (goals, env, path2))
        );
        []
      )
    in
    let rec loop_send_jobs () =
      if (Deque.length worker_state.q) > 1 then (
          match Deque.dequeue_front worker_state.q with
          | None -> Deferred.unit (* Should never happen *)
          | Some job -> ignore (Pipe.read_now worker_state.reader);
            let%bind _ = Pipe.write worker_state.writer (Job (job, fresh ())) in
            loop_send_jobs ()
        ) else Deferred.unit
    in
    let%bind _ =
    if send_initial_jobs_bool then loop_send_jobs () else Deferred.unit
        in
    let rec main_inner (results : ((exp * exp) list * (int*int) list) list) =
      let%bind _check_for_requests =
        (* NOTE - if you ever use a `read' function to check if there's
           anything in the pipe, make sure to use read_now - `read' waits
           until there's a value available.
        *)
          match Pipe.peek worker_state.reader with
          | None -> Deferred.unit
          | Some (Cut cut) -> 
            Deque.iteri worker_state.q
              ~f:(fun i job ->
                  if remove_due_to_cut job.path cut then
                    Deque.set_exn worker_state.q i ({job with goals=[TermExp("false", []), 0]})
                );
            Deferred.unit
          | Some Work_request -> (
              (* We only give out work if we have at least 2 jobs on our stack.
              Otherwise, we would give away all our work, and have to ask the
              toplevel for more *)
              if (Deque.length worker_state.q) > 1 then (
                match Deque.dequeue_front worker_state.q with
                | None -> Deferred.unit (* Should never happen *)
                | Some job -> ignore (Pipe.read_now worker_state.reader);
                  Pipe.write worker_state.writer (Job (job, fresh ()))
              ) else Deferred.unit
            )
      in
      match Deque.dequeue_back worker_state.q with
      | None -> Pipe.write worker_state.writer (Results (Results.reverse_path_order results))
      | Some {goals =[]; env; path} -> main_inner ((env, path)::results)
      | Some {goals; env; path} -> (
          let jobs, cut =
            ( eval goals env worker_state.db path) in
          (
            match cut with
            | Some cut -> Pipe.write_without_pushback worker_state.writer (Cut cut);
              List.iter jobs
                ~f:( fun (goals, env, path2) ->
                    if not (remove_due_to_cut path2 cut) then (
                      handle_job (goals, env, path2)
                    ))
            | None ->
              List.iter jobs
                ~f:( fun (goals, env, path2) -> handle_job (goals, env, path2))
          );
          main_inner results
        )
    in
    main_inner init_results
  ;;


  let initialise ((init_db, index) : Worker_state.init_arg) : Worker_state.t  =
    let q = Deque.create () in
    let (_, temp_writer) = Pipe.create () in
    {q; index; db = init_db; reader = Pipe.empty (); writer = temp_writer}

  type 'worker functions = {
    eval_query : ('worker, Job_and_bool_and_vars.t, unit) Rpc_parallel_edit.Function.t;
    update_db : ('worker, dec, unit) Rpc_parallel_edit.Function.t;
    worker_to_toplevel_pipe : ('worker, unit, Worker_to_toplevel.t Pipe.Reader.t) Rpc_parallel_edit.Function.t;
    toplevel_to_worker_pipe : ('worker, unit * Toplevel_to_worker.t Pipe.Reader.t, unit) Rpc_parallel_edit.Function.t
  }

  module Functions
      (C : Rpc_parallel_edit.Creator
       with type worker_state := Worker_state.t
        and type connection_state := Connection_state.t) =
  struct
    let eval_query_impl ~worker_state ~conn_state:() (job, highest_var, send_initial_jobs_bool, orig_vars) =
      update highest_var;
      Deque.enqueue_back (Worker_state.q worker_state) job;
      main worker_state send_initial_jobs_bool orig_vars
    ;;

    let update_db_impl ~worker_state ~conn_state:() d =
      Worker_state.set_db worker_state (worker_state.db @ [d]) |> return
    ;;

    let worker_to_toplevel_pipe_impl ~worker_state ~conn_state:() _ =
      let (reader, writer) = Pipe.create () in
      Worker_state.set_writer worker_state writer;
      return reader

    let toplevel_to_worker_pipe_impl ~worker_state ~conn_state:() _ reader =
      Worker_state.set_reader worker_state reader |> return

    let eval_query =
      C.create_rpc
        ~f:eval_query_impl
        ~bin_input:(Job_and_bool_and_vars.bin_t)
        ~bin_output:(Unit.bin_t)
        ()

    let update_db =
      C.create_rpc
        ~f:update_db_impl
        ~bin_input:Dec.bin_t
        ~bin_output:Unit.bin_t
        ()

    let worker_to_toplevel_pipe =
      C.create_pipe
        ~f:worker_to_toplevel_pipe_impl
        ~bin_input:Unit.bin_t
        ~bin_output:Worker_to_toplevel.bin_t
        ()

    let toplevel_to_worker_pipe =
      C.create_reverse_pipe
        ~f:toplevel_to_worker_pipe_impl
        ~bin_query:Unit.bin_t
        ~bin_update:Toplevel_to_worker.bin_t
        ~bin_response:Unit.bin_t
        ()

    let functions = {eval_query; update_db; worker_to_toplevel_pipe; toplevel_to_worker_pipe}
    let init_worker_state init_arg = initialise init_arg |> return
    let init_connection_state ~connection:_ ~worker_state:_ = return

  end
end

include Rpc_parallel_edit.Make (T)

module Worker_info = struct
  type t = {
    conn : Connection.t;
    reader : Worker_to_toplevel.t Pipe.Reader.t;
    writer : Toplevel_to_worker.t Pipe.Writer.t
  } [@@deriving fields]
end

(* init_workers takes an int and returns a list of Worker_info.t
   It initialises the given number of workers, gets the connection to each of them which
   can be used to run RPCs, and sets up pipes to and from each of them, before
   returning each of the connections, pipe readers and pipe writers.
*)
let init_workers n : Worker_info.t list Deferred.t =
    Deferred.List.init n
      ~how:`Parallel
      ~f:(fun i ->
          let%bind worker = spawn_exn
            ~on_failure:Error.raise
            ~shutdown_on:Heartbeater_connection_timeout
            ~redirect_stdout:(`File_append ("/Users/em/Documents/diss_stdout"^(string_of_int i)^".txt"))
            ~redirect_stderr:(`File_append "/Users/em/Documents/diss_stderr.log")
            ([], i)
          in
          let%bind conn = Connection.client_exn worker () in
          let%bind reader =
            Connection.run_exn conn
              ~f:(functions.worker_to_toplevel_pipe) ~arg:()
          in
          let (worker_reader, writer) = Pipe.create () in
          let%bind _ =
            Connection.run_exn conn
              ~f:(functions.toplevel_to_worker_pipe) ~arg:((), worker_reader)
          in
          Worker_info.Fields.create ~conn ~reader ~writer |> return
        )
  ;;

(* add_dec_to_db takes a declaration (dec) and list of Worker_info.t and sends
   the declaration to each of the workers to be added to their databases.
   It returns unit.
*)
let add_dec_to_db dec workers_info =
  let disallowed = ["true"; "is"; "list"; "empty_list"; "equals"; "not_equal"; "less_than";
                    "greater_than"; "less_than_or_eq"; "greater_than_or_eq"; "cut"]
  in
  match dec with
  | Clause (h, _) -> (
      match h with
      | TermExp (name, _) -> if List.exists disallowed ~f:(fun a -> String.equal name a )
        then ( print_string ("Can't reassign '"^name^"' predicate\n"); Deferred.unit)
        else Deferred.List.iter ~how:`Parallel workers_info
               ~f:(fun worker_info ->
                   Connection.run_exn (Worker_info.conn worker_info) ~f:(functions.update_db) ~arg:dec
                 )
      | _ -> Deferred.List.iter ~how:`Parallel workers_info
               ~f:(fun worker_info ->
                   Connection.run_exn (Worker_info.conn worker_info) ~f:(functions.update_db) ~arg:dec
                 )
    )
  | Query _ -> Deferred.unit
;;

(* eval_query takes the body of a query (b) and a list of Worker_info.t
   It handles giving work to the workers and aggregating the results they give back.
   It loops until none of the workers have any work left, at which point it returns the
   aggregated results.
*)
let eval_query b worker_info_list =
  let orig_vars = String.Set.of_list (find_vars_string b) in
  let num_workers = List.length worker_info_list in
  let have_work__requested_work = Hashtbl.of_alist_exn (module Int)
      (List.init num_workers ~f:(fun i -> (i, (false, false)))) in

  (* define helper functions *)
  let update_have_work index b =
    Hashtbl.update have_work__requested_work index ~f:(fun data_opt ->
        match data_opt with
        | Some (_, requested) -> (b, requested)
        | None -> (b, false)
      )
  in
  let update_requested_work index b =
    Hashtbl.update have_work__requested_work index ~f:(fun data_opt ->
        match data_opt with
        | Some (have_work , _) -> (have_work, b)
        | None -> (true, b)
      )
  in
  let give_work index (job, n, b) =
    don't_wait_for
      (
        Connection.run_exn
          (Worker_info.conn (List.nth_exn worker_info_list index))
          ~f:(functions.eval_query)
          ~arg:(job, n, b, orig_vars)
      );
    update_have_work index true
  in
  let request_work index =
    Pipe.write_without_pushback  (List.nth_exn worker_info_list index).writer Work_request;
    update_requested_work index true
  in
  let send_cut cut index_of_sender =
    Deferred.List.iteri worker_info_list ~f:(fun index {conn=_; reader=_; writer} ->
        if not (Int.equal index_of_sender index) then Pipe.write writer cut else Deferred.unit
      )
  in

  let spare_jobs = Queue.create () in
  let accumulated_results = ref [] in
  let accumulated_cuts = ref [] in

  (* start by giving work to the first worker, then requesting work if we have more than 1 worker *)
  let req_init_work = if num_workers > 1 then true else false in
  let b = List.map b ~f:(fun x -> (x,0)) in
  give_work 0 ({goals = b; env = []; path = []}, 0, req_init_work);
  if num_workers > 1 then
       request_work 0;

  let rec eval_inner () =
    List.iteri worker_info_list ~f:(fun index {conn=_; reader; writer=_} ->
        match Pipe.read_now reader with
        | `Nothing_available -> ()
        | `Eof -> print_endline ("Pipe closed unexpectedly in worker "^ (Int.to_string index))
        | `Ok (Job job) -> (
            update_requested_work index false;
            Queue.enqueue spare_jobs job
          )
        | `Ok (Results results) ->
          Hashtbl.set have_work__requested_work ~key:index ~data:(false, false);
          accumulated_results := (results@(!accumulated_results))
        | `Ok (Cut cut) ->
          don't_wait_for (send_cut (Cut cut) index);
          accumulated_cuts := ([cut]@(!accumulated_cuts))
      );
    (* give new_jobs to any idle workers and update have_work accordingly *)
    let idle = Hashtbl.filter have_work__requested_work ~f:(fun (b, _) -> not b) in
    let work_given = Hashtbl.fold ~init:[] idle ~f:(fun ~key ~data:_ acc ->
        match Queue.dequeue spare_jobs with
        | None -> acc
        | Some (job, n) ->
          give_work key (job, n, false);
          key::acc
      )
    in
    List.iter work_given ~f:(fun index -> Hashtbl.remove idle index);

    (* Make any more requests for work that are needed *)
    if (Queue.length spare_jobs < num_workers) then (
      let not_requested = Hashtbl.filter have_work__requested_work
          ~f:(fun (have_work, requested_work) -> have_work && (not requested_work) ) in
      Hashtbl.iteri not_requested ~f:(fun ~key ~data:_ ->
          request_work key
        )
    );

    (* if there's now no work, return the accumulated results. Otherwise, repeat
    *)
    if (Hashtbl.count have_work__requested_work ~f:(fun (have_work, _) -> have_work)) = 0 &&
       (Queue.length spare_jobs ) = 0
    then
      return (accumulated_results, accumulated_cuts)
    else
      (
        let%bind _ = Clock.after (Time.Span.of_ns 10.0) in
        eval_inner ()
      )
  in
  eval_inner ()
;;

(* main takes the name of a file and the number of parallel workers to use, and prints
   the results of any queries in the file.
   It loops, reading in each line of the file, and evaluating queries as it encounters
   them.
*)
let main filename num_workers =
  let%bind workers_info = init_workers num_workers in
   (
    let%bind () = (
          let rec loop file_lines =
            (
              match file_lines with
              | s::ss -> (
                  try (
                    let lexbuf = Lexing.from_string s in
                    let dec = Parser.clause (
                        fun lb -> (
                            match Lexer.token lb with
                            | EOF -> raise Lexer.EndInput
		                        | r -> r
		                      )
	                    ) lexbuf
                    in
                    let%bind _ = (
                    match dec with
                    | Clause (_, _) -> add_dec_to_db dec workers_info
                    | Query b -> (
                        print_endline s;
                        (* find all uniq VarExps in query *)
                        let orig_vars = uniq (find_vars b) in
                        (* find num of VarExps in query *)
                        let orig_vars_num = List.length orig_vars in
                        (* evaluate query *)
                        let%bind res, cuts = eval_query b workers_info in
                        let res = List.filter !res ~f:(fun (_, path) ->
                            List.exists !cuts ~f:(fun cut_path ->
                                remove_due_to_cut path cut_path) |> not
                          ) in
                        let sorted_res = List.sort res ~compare:(fun (_env1, path1) (_env2, path2) ->
                            (* need to sort by path *)
                            let a = List.compare (fun (a,_) (b,_) -> Int.compare a b) path1 path2 in
                            if a = 0 then
                            (List.length path1) - (List.length path2)
                            else a
                          )
                        in
                        let envs = List.map sorted_res ~f:(fun (env, _) -> env) |> List.rev in
                        (* print the result *)
                        print_string "\n";
                        print_endline (string_of_res envs orig_vars orig_vars_num);
                        print_string "\n\n";
                        (* reset fresh variable counter *)
                        reset ();
                        Deferred.unit
                      )
                  ) in
                    loop ss
                  ) with
                  | Failure f -> ( (* in case of an error *)
                      print_endline ("Failure: " ^ f ^ "\n");
                      loop ss
                    )
                  | Parser.Error -> ( (* failed to parse input *)
                      print_endline "\nDoes not parse\n";
                      loop ss
                    )
                  | Lexer.EndInput -> exit 0 (* EOF *)
                  | _ -> ( (* Any other error *)
                      print_endline "\nUnrecognized error\n";
                      loop ss
                    )
                )
              | [] -> return ()
            )
          in
          print_endline ("Opening file " ^ filename ^ "\n");
          let file_lines = In_channel.read_lines filename in
          let%bind () = loop file_lines in
          print_endline "\nFile contents loaded.\n"
        |> return
        )
    in
    return ()
  )

let command =
  Command.async
    ~summary:"Parallel Prolog interpreter"
    [%map_open.Command
      let filename =
        flag
          ~doc:"FILE to read prolog from"
          "file"
          (required string)
      and num_workers =
        flag
          ~doc:"INT number of parallel workers"
          "num-workers"
          (required int)
      in
      fun () -> main filename num_workers
    ]


open Core
open Async
open Prolog_interpreter.Trail_util
open Include

(* TODO - need to create modules for sending jobs - we can't send references *)

module Job = struct
  type t = {
    goals : Exp.t ref list;
    var_mapping : Exp.t Var.t String.Table.t;
    path : int list
  } [@@deriving bin_io, fields]

  (* type for_sending = { *)
  (*   goals : Exp.for_sending list; *)
  (*   var_mapping : Exp.for_sending Var.for_sending String.Table.t; *)
  (*   path : int list *)
  (* } [@@deriving bin_io, fields] *)

  let deep_copy {goals; var_mapping; path} =
    let var_translation = String.Table.create () in
    let new_var_mapping = String.Table.map var_mapping ~f:(fun v ->
        Var.deep_copy v (fun e -> Exp.deep_copy e var_translation) var_translation
      )
    in
    print_endline "old_var_mapping-----";
    print_endline (String.Table.fold ~init:"" var_mapping
                     ~f:(fun ~key ~data acc -> "("^key^", "^(Var.to_string data Exp.to_string)^")"^acc ));
    print_endline "new_var_mapping-----";
    print_endline (String.Table.fold ~init:"" var_translation
                     ~f:(fun ~key ~data acc -> "("^key^", "^(Var.to_string !data Exp.to_string)^")"^acc ));
    print_endline (String.Table.fold ~init:"" new_var_mapping
                     ~f:(fun ~key ~data acc -> "("^key^", "^(Var.to_string data Exp.to_string)^")"^acc ));
    print_endline "var_mapping ends-----";
    let new_goals = List.map goals ~f:(fun e -> Exp.reref_vars !e var_translation |> ref) in
    {goals=new_goals; var_mapping=new_var_mapping; path}
end

module Job_and_nxt = struct
  type t = Job.t * int [@@deriving bin_io]
end

module Job_and_bool = struct
  type t = Job.t * int * bool [@@deriving bin_io]
end

module Results = struct
  type t = ((string * string) list * int list) list [@@deriving bin_io]

  let reverse_path_order t : t =
    List.map t ~f:( fun (env, path) -> (env, List.rev path))
end

module Worker_to_toplevel = struct
  type t =
    Results of Results.t
    | Job of Job_and_nxt.t
  [@@deriving bin_io]
end

module T = struct

  module Worker_state = struct
    type init_arg = (Clause.t list * int)
    [@@deriving bin_io]

    type t = {
      q : Job.t Deque.t;
      index : int;
      mutable db : Clause.t list;
      mutable reader : unit Pipe.Reader.t;
      mutable writer : Worker_to_toplevel.t Pipe.Writer.t
    } [@@deriving fields]
  end

  module Connection_state = struct
    type init_arg = unit [@@deriving bin_io]
    type t = unit
  end

  (* eval takes
     - a job
     - the database of clauses
     and returns the remainder of work to be done before this job is complete.
     This is in the form of a list of jobs.

     The function itself performs one step of evaluation on the job it is given, and
     either manages to prove it, returning the empty list, or generates one or more other
     jobs to be done.
  *)
  let eval (job : Job.t) db : Job.t list =
    print_endline "called eval";
      match job.goals with
      | [] -> []
      | g1::gl -> (
          (
            print_endline ("popped: " ^ (Exp.to_string !g1));
            match !g1 with
            (* if goal is the true predicate *)
            | Exp.TermExp("true", []) -> [ {goals=gl;var_mapping=job.var_mapping; path=job.path} ]
            | TermExp("equals", [lhs; rhs]) ->
              (* check if the lhs and rhs can unify *)
              let trail = Trail.create () in
              if (unify lhs rhs trail) then (
                [ {goals=gl; var_mapping=job.var_mapping; path=job.path} ]
              ) else (Trail.undo trail; [])
            | TermExp("not_equal", [lhs;rhs]) -> (
                (* check if the lhs and rhs can unify. If they can, this is not a
                   successful substitution. If they don't, we can continue solving the
                   rest of the goals
                *)
                let trail = Trail.create () in
                if not (unify lhs rhs trail) then (
                  Trail.undo trail;
                  [ {goals=gl; var_mapping=job.var_mapping; path=job.path} ]
                ) else (Trail.undo trail; [])
              )
            | TermExp("greater_than", [lhs; rhs]) -> (
                match (resolve !lhs), (resolve !rhs) with
                | IntExp i1, IntExp i2 ->
                  if i1 > i2 then
                    [ {goals=gl; var_mapping=job.var_mapping; path=job.path}]
                  else []
                | _ -> [] (* arguments insufficiently instantiated *)
              )
            | TermExp("greater_than_or_eq", [lhs; rhs]) -> (
                match (resolve !lhs), (resolve !rhs) with
                | IntExp i1, IntExp i2 ->
                  if i1 >= i2 then
                    [ {goals=gl; var_mapping=job.var_mapping; path=job.path}]
                  else []
                | _ -> [] (* arguments insufficiently instantiated *)
              )
            | TermExp("less_than", [lhs; rhs]) -> (
                match (resolve !lhs), (resolve !rhs) with
                | IntExp i1, IntExp i2 ->
                  if i1 < i2 then
                    [ {goals=gl; var_mapping=job.var_mapping; path=job.path}]
                  else []
                | _ -> [] (* arguments insufficiently instantiated *)
              )
            | TermExp("less_than_or_eq", [lhs; rhs]) -> (
                match (resolve !lhs), (resolve !rhs) with
                | IntExp i1, IntExp i2 ->
                  if i1 <= i2 then
                    [ {goals=gl; var_mapping=job.var_mapping; path=job.path}]
                  else []
                | _ -> [] (* arguments insufficiently instantiated *)
              )
            | TermExp("is", [lhs; rhs]) -> (
                (* evaluate the arithmetic expressions with current substitutions, then check if it is
                   possible to unify them with any additional substitutions *)
                match !rhs with
                | ArithmeticExp (op, t1, t2) -> (
                    match (resolve_arith t1), (resolve_arith t2) with
                    | ArithmeticInt i1, ArithmeticInt i2 -> (
                        let result = perform_arithmetic op i1 i2 in
                        (
                          match !lhs with
                          | VarExp _ -> let trail = Trail.create () in
                            if unify lhs (ref (Exp.IntExp result)) trail then
                              [{goals=gl; var_mapping=job.var_mapping; path=job.path}]
                            else (Trail.undo trail ; [])
                          | IntExp i -> if i = result then
                              [{goals=gl; var_mapping=job.var_mapping; path=job.path}]
                              else []
                          | _ -> []
                        )
                      )
                    | _ -> []
                  )
                | IntExp result -> (
                    (
                      match !lhs with
                      | VarExp _ -> let trail = Trail.create () in
                        if unify lhs (ref (Exp.IntExp result)) trail then
                          [{goals=gl; var_mapping=job.var_mapping; path=job.path }]
                        else (Trail.undo trail ; [])
                      | IntExp i -> if i = result then
                          [{goals=gl; var_mapping=job.var_mapping; path=job.path }]
                          else []
                      | _ -> []
                    )
                  )
                | _ -> []
              )
            | TermExp(_,_) -> (
                print_endline "iter thru db";
                let db_copy = List.map db ~f:(fun clause ->  Clause.copy clause ) in
                List.foldi db_copy ~init:[]
                  ~f:(fun i acc c ->
                      let (head, body) = Clause.copy c in
                      let trail = Trail.create () in
                      if unify head g1 trail then (
                        print_endline ("goals before copy: " ^ (List.to_string (body@gl) ~f:(fun gl -> Exp.to_string !gl) ));
                        let new_job = Job.deep_copy
                            {goals=(body@gl); var_mapping=job.var_mapping; path=(i::job.path)} in
                        Trail.undo trail;
                        print_endline ("goals after copy: " ^ (List.to_string new_job.goals
                                                               ~f:(fun gl -> Exp.to_string !gl) ));
                        (new_job)::acc
                      ) else (
                        Trail.undo trail;
                        acc
                      )
                    )
              )
            | _ -> []
          )
        )

  (* main takes the worker state and returns unit
     It loops, checking for and then handling updates from the toplevel, before
     taking a job from the stack and calling `eval' on it.
     It sends results or work back to the toplevel via the `writer' pipe in
     the worker_state.
     It returns when it no longer has any work on its stack.
  *)
  let main (worker_state : Worker_state.t) send_initial_jobs_bool =
    (* Clear the pipe of any previous requests for work which
    are no longer relevant *)
    Pipe.clear worker_state.reader;
    let init_results = match Deque.dequeue_back worker_state.q with
    | None -> []
    | Some {goals =[]; var_mapping; path} -> [((realise_solution var_mapping), path)]
    | Some job -> (
        let goals_str = List.fold ~init:"" job.goals ~f:(fun acc g -> let gs = Exp.to_string !g in
                                                        acc^","^gs) in
        print_endline ("goals: "^goals_str);
        let jobs = eval job worker_state.db in
        List.iter jobs
          ~f:( fun new_job ->
              Deque.enqueue_back worker_state.q new_job );
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
    let rec main_inner (results : ((string * string) list * int list) list) =
      print_endline "\n loop";
      let%bind _check_for_requests =
        (* NOTE - if you ever use a `read' function to check if there's
           anything in the pipe, make sure to use read_now - `read' waits
           until there's a value available.
        *)
          match Pipe.peek worker_state.reader with
          | None -> Deferred.unit
          | Some () -> (
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
      | Some {goals =[]; var_mapping; path} ->
        let soln = realise_solution var_mapping in main_inner ((soln, path)::results)
      | Some job -> (
          let goals_str = List.fold ~init:"" job.goals ~f:(fun acc g -> let gs = Exp.to_string !g in
                                                            acc^","^gs) in
          print_endline ("goals: "^goals_str);
          let jobs = eval job worker_state.db in
          List.iter jobs
            ~f:( fun new_job ->
                Deque.enqueue_back worker_state.q new_job );
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
    eval_query : ('worker, Job_and_bool.t, unit) Rpc_parallel_edit.Function.t;
    update_db : ('worker, Clause.t, unit) Rpc_parallel_edit.Function.t;
    worker_to_toplevel_pipe : ('worker, unit, Worker_to_toplevel.t Pipe.Reader.t) Rpc_parallel_edit.Function.t;
    toplevel_to_worker_pipe : ('worker, unit * unit Pipe.Reader.t, unit) Rpc_parallel_edit.Function.t
  }

  module Functions
      (C : Rpc_parallel_edit.Creator
       with type worker_state := Worker_state.t
        and type connection_state := Connection_state.t) =
  struct
    let eval_query_impl ~worker_state ~conn_state:() (job, highest_var, send_initial_jobs_bool) =
      update highest_var;
      Deque.enqueue_back (Worker_state.q worker_state) job;
      main worker_state send_initial_jobs_bool
    ;;

    let update_db_impl ~worker_state ~conn_state:() d =
      Worker_state.set_db worker_state (d::worker_state.db) |> return
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
        ~bin_input:(Job_and_bool.bin_t)
        ~bin_output:(Unit.bin_t)
        ()

    let update_db =
      C.create_rpc
        ~f:update_db_impl
        ~bin_input:Clause.bin_t
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
        ~bin_update:Unit.bin_t
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
    writer : unit Pipe.Writer.t
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
            ~redirect_stdout:(`File_truncate
                        ("/Users/em/OneDrive/Documents/Uni/II/Dissertation/diss_stdout"^(string_of_int i)^".txt"))
            ~redirect_stderr:(`File_append "/Users/em/OneDrive/Documents/Uni/II/Dissertation/diss_stderr.log")
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

(* send_db_to_workers takes a list of clauses and list of Worker_info.t and sends
   the clauses to each of the workers to be added to their databases.
   It returns unit Deferred.t
*)
let send_db_to_workers db workers_info =
  let disallowed = ["true"; "is"; "list"; "empty_list"; "equals"; "not_equal"; "less_than";
                    "greater_than"; "less_than_or_eq"; "greater_than_or_eq"; "cut"]
  in
  Deferred.List.iter db ~f:(fun (h,b) ->
      match !h with
      | Exp.TermExp (name, _) -> if List.exists disallowed ~f:(fun a -> String.equal name a )
        then ( print_string ("Can't reassign '"^name^"' predicate\n"); Deferred.unit)
        else Deferred.List.iter ~how:`Parallel workers_info
            ~f:(fun worker_info ->
                Connection.run_exn (Worker_info.conn worker_info) ~f:(functions.update_db) ~arg:(h,b)
              )
      | _ -> Deferred.List.iter ~how:`Parallel workers_info
               ~f:(fun worker_info ->
                   Connection.run_exn (Worker_info.conn worker_info) ~f:(functions.update_db) ~arg:(h,b)
                 )
    )

(* eval_query takes the body of a query (b) and a list of Worker_info.t
   It handles giving work to the workers and aggregating the results they give back.
   It loops until none of the workers have any work left, at which point it returns the
   aggregated results.
*)
let eval_query (job : Job.t) worker_info_list =
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
          ~arg:(job, n, b)
      );
    update_have_work index true
  in
  let request_work index =
    Pipe.write_without_pushback  (List.nth_exn worker_info_list index).writer ();
    update_requested_work index true
  in

  let spare_jobs = Queue.create () in
  let accumulated_results = ref [] in

  (* start by giving work to the first worker, then requesting work if we have more than 1 worker *)
  let b = if num_workers > 1 then true else false in
  give_work 0 (job, 0, b);
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
      return accumulated_results
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
          let rec loop file_lines db =
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
                    let%bind db2 = (
                    match dec with
                    | Clause (h, b) ->
                      (* TODO - need to be careful about making sure the workers are using fresh variables
                         relative to the variables being used in the db - need to bear this in mind when
                         converting the db, when receiving jobs, when sending jobs.

                         So we probably need a new convert function, a new Var.create - so a whole new Var
                         module, new reref_var functions, new deep_copy functions. Hm.

                         Sorted this by redefining fresh, reset and update in Trail_util
                      *)
                      let var_mapping = String.Table.create () in
                      let h2 = convert h var_mapping in
                      let b2 = List.map b ~f:(fun e -> convert e var_mapping |> ref) in
                      (ref h2, b2)::db |> return
                    | Query b -> (
                        print_endline s;
                        (* NOTE we create an empty var_mapping here so we don't have overlap between the rules and the
                           query *)
                        let var_mapping = String.Table.create () in
                        let b_converted : Exp.t ref list = List.map b ~f:(fun e -> convert e var_mapping |> ref ) in
                        (* send additional db entries to workers *)
                        let%bind _ = send_db_to_workers db workers_info in
                        (* evaluate query *)
                        let%bind res = eval_query {goals=b_converted; var_mapping; path=[]} workers_info in
                        let sorted_res = List.sort !res ~compare:(fun (_env1, path1) (_env2, path2) ->
                            (* need to sort by path *)
                            let a = List.compare Int.compare path1 path2 in
                            if a = 0 then
                            (List.length path1) - (List.length path2)
                            else a
                          )
                        in
                        let envs = List.map sorted_res ~f:(fun (env, _) -> env) in
                        (* print the result *)
                        List.iter envs ~f:(fun result ->
                            print_endline "===============";
                            List.iter result ~f:(fun (a,b) ->
                                print_endline (a ^ " = "^b)
                              );
                            print_endline "===============";
                          ); return []
                      )
                  ) in
                    loop ss db2
                  ) with
                  | Failure f -> ( (* in case of an error *)
                      print_endline ("Failure: " ^ f ^ "\n");
                      loop ss db
                    )
                  | Parser.Error -> ( (* failed to parse input *)
                      print_endline "\nDoes not parse\n";
                      loop ss db
                    )
                  | Lexer.EndInput -> exit 0 (* EOF *)
                  | _ -> ( (* Any other error *)
                      print_endline "\nUnrecognized error\n";
                      loop ss db
                    )
                )
              | [] -> return ()
            )
          in
          print_endline ("Opening file " ^ filename ^ "\n");
          let file_lines = In_channel.read_lines filename in
          let%bind () = loop file_lines [] in
          print_endline "\nFile contents loaded.\n"
        |> return
        )
    in
    return ()
  )

let command =
  Command.async
    ~summary:"Parallel Trail-Stack Prolog interpreter"
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


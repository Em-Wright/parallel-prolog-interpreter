open Core
open Async
open Prolog_interpreter.Ast
open Prolog_interpreter.Util
open Include

module Job = struct
  type t = {
    goals : exp list;
    env : ((exp * exp) list)
  } [@@deriving bin_io, fields]
end

module Dec = struct
  type t = dec [@@deriving bin_io]
end

module Results = struct
  type t = (exp * exp) list list [@@deriving bin_io]
end

module Worker_to_toplevel = struct
  type t =
    Results of Results.t
    | Job of Job.t
    | Request
  [@@deriving bin_io]
end

module T = struct

  module Worker_state = struct
    type init_arg = dec list
    [@@deriving bin_io]

    type t = {
      q : Job.t Deque.t;
      mutable db : dec list;
      mutable reader : unit Pipe.Reader.t;
      mutable writer : Worker_to_toplevel.t Pipe.Writer.t
    } [@@deriving fields]
  end

  module Connection_state = struct
    type init_arg = unit [@@deriving bin_io]
    type t = unit
  end

  let eval_inner gs env db  =
    match gs with
    | g1::gl -> (
        (* we have at least one more subgoal (g1) to prove in this job *)
        match g1 with
        | TermExp("true", []) -> [ (gl, env)]
        | TermExp("equals", [lhs; rhs]) -> (
            match unify [(lhs, rhs)] with
            | Some s -> (
                match unify (s@env) with
                | Some env2 -> [(sub_lift_goals s gl, env2)]
                | None -> []
              )
            | None -> []
          )
        | TermExp("not_equal", [lhs;rhs]) -> (
            match unify [(lhs, rhs)] with
            | Some s -> (
                match unify (s@env) with
                | Some _ -> []
                | None -> [(gl, env)]
              )
            | None -> [ (gl, env) ]
          )
        | TermExp("greater_than", [lhs; rhs]) -> (
            match lhs, rhs with
            | IntExp i1, IntExp i2 -> if i1 > i2 then [(gl, env)] else []
            | _ -> [] (* arguments insufficiently instantiated *)
          )
        | TermExp("less_than", [lhs; rhs]) ->
          (
            match lhs, rhs with
            | IntExp i1, IntExp i2 -> if i1 < i2 then [(gl, env)] else []
            | _ -> [] (* arguments insufficiently instantiated *)
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
                              sub_lift_goals [(lhs, IntExp result)] gl,
                              env2
                            )]
                          | None -> []
                        )
                      | IntExp i -> if i = result then [(gl, env)] else []
                      | _ -> []
                    )
                  | _ -> []
                )
              | IntExp result -> (
                  match lhs with
                  | VarExp _ ->
                    ( match unify ((lhs, rhs)::env) with
                      | Some env2 ->
                         [(
                          sub_lift_goals [(lhs, rhs)] gl,
                          env2
                        )]
                      | None -> []
                    )
                  | IntExp i -> if i = result then [(gl, env)] else []
                  | _ -> []
                )
              | _ -> []
            )
          (* if goal is some other predicate *)
          | TermExp(_,_) -> (
              List.fold db ~init:[]
                ~f:(fun acc rule ->
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
                                      sub_lift_goals s gl,
                                      env2
                                    )::acc
                                  | _ ->
                                    (
                                      (sub_lift_goals s body) @ (sub_lift_goals s gl),
                                      env2
                                    )::acc
                                )
                                else
                                  (
                                    (sub_lift_goals s body) @ (sub_lift_goals s gl),
                                    env2
                                  )::acc
                              )
                            | _ -> acc
                          )
                        (* this rule's head doesn't unify with the subgoal *)
                        | _ -> acc
                      )
                    |  _ -> acc
            ))
          (* subgoal g1 isn't a TermExp *)
          | _ -> [(gl, env)]
      )
    | [] -> []
  ;;

  let main (worker_state : Worker_state.t) =
    (* Clear the pipe of any previous requests for work which
    are no longer relevant *)
    Pipe.clear worker_state.reader;
    let rec main_inner results =
      let%bind _check_for_requests =
        (* NOTE - if you ever use a `read' function to check if there's
           anything in the pipe, make sure to use read_now - `read' waits
           until there's a value available.
        *)
          match Pipe.peek worker_state.reader with
          | None -> Deferred.unit
          | Some () -> (
              (* We only give out work if we have at least 2 jobs on our stack.
              Otherwise, we give away all our work, and have to ask the
              toplevel for more *)
              if (Deque.length worker_state.q) > 1 then (
                match Deque.dequeue_front worker_state.q with
                | None -> Deferred.unit (* Should never happen *)
                | Some job -> ignore (Pipe.read_now worker_state.reader);
                  Pipe.write worker_state.writer (Job job)
              ) else Deferred.unit
              (* we don't have any work to
                 give the main process. We don't send a request
                 for more work here, since we'll be sending one later
                 anyway, so it would be redundant

                 TODO - maybe I ought to add a message type which says
                 `I don't have any work for you' which can be used where we
                 only have 1 job on our stack? Hopefully this happens
                 rarely enough that I don't need to think about it
              *)
            )
      in
      match Deque.dequeue_back worker_state.q with
      | None -> (let%bind _write = Pipe.write worker_state.writer (Results results) in
                 Pipe.write worker_state.writer Request
                )
      | Some {goals =[]; env} -> main_inner (env::results)
      | Some {goals; env} -> (
          List.iter
            ( eval_inner goals env worker_state.db)
            ~f:( fun (goals, env) -> Deque.enqueue_back worker_state.q {goals; env} );
          main_inner results
        )
    in
    main_inner []
  ;;


  let initialise (init_arg : Worker_state.init_arg) : Worker_state.t  =
    let q = Deque.create () in
    let (_, temp_writer) = Pipe.create () in
    {q; db = init_arg; reader = Pipe.empty (); writer = temp_writer}

  type 'worker functions = {
    eval_query : ('worker, Job.t, unit) Rpc_parallel_edit.Function.t;
    update_db : ('worker, dec, unit) Rpc_parallel_edit.Function.t;
    worker_to_toplevel_pipe : ('worker, unit, Worker_to_toplevel.t Pipe.Reader.t) Rpc_parallel_edit.Function.t;
    toplevel_to_worker_pipe : ('worker, unit * unit Pipe.Reader.t, unit) Rpc_parallel_edit.Function.t
  }

  module Functions
      (C : Rpc_parallel_edit.Creator
       with type worker_state := Worker_state.t
        and type connection_state := Connection_state.t) =
  struct
    let eval_query_impl ~worker_state ~conn_state:() job =
      Deque.enqueue_back (Worker_state.q worker_state) job;
      main worker_state
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
        ~bin_input:(Job.bin_t)
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

(* TODO - need to extend the heartbeater timeout time - this is done in the
   start_app function call.
*)

let init_workers n : Worker_info.t list Deferred.t =
    Deferred.List.init n
      ~how:`Parallel
      ~f:(fun _ ->
          let%bind worker = spawn_exn
            ~on_failure:Error.raise
            ~shutdown_on:Heartbeater_connection_timeout
            ~redirect_stdout:(`File_append "/Users/em/Documents/diss_stdout.log")
            ~redirect_stderr:(`File_append "/Users/em/Documents/diss_stderr.log")
            []
            (* TODO - should I initialise workers just before starting a query
               execution, then I can pass the whole db, or do I do it like this? *)
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


let add_dec_to_db dec workers_info =
    match dec with
    | Clause (h, _) -> (
        match h with
        (* don't allow user to add a new definition of true *)
        | TermExp ("true", _) ->
          print_string "Can't reassign true predicate\n"; Deferred.unit
        | TermExp ("is", _) ->
          print_string "Can't reassign 'is' predicate\n"; Deferred.unit
        | TermExp ("list", _) ->
          print_string "Can't reassign 'list' predicate\n"; Deferred.unit
        | TermExp ("empty_list", _) ->
          print_string "Can't reassign 'empty_list' predicate\n"; Deferred.unit
        | TermExp ("equals", _) ->
          print_string "Can't reassign 'equals' predicate\n"; Deferred.unit
        | TermExp ("not_equal", _) ->
          print_string "Can't reassign 'not_equal' predicate\n"; Deferred.unit
        | TermExp ("less_than", _) ->
          print_string "Can't reassign 'less_than' predicate\n"; Deferred.unit
        | TermExp ("greater_than", _) ->
          print_string "Can't reassign 'greater_than' predicate\n"; Deferred.unit
        | _ -> Deferred.List.iter ~how:`Parallel workers_info
                 ~f:(fun worker_info ->
                     Connection.run_exn (Worker_info.conn worker_info) ~f:(functions.update_db) ~arg:dec
                   )
      )
    | Query _ -> return ()
;;

(* TODO - need to think about the fresh variable counter - one per worker? They only
interfere if they occur in the same job, so one per worker is working fine *)

(* TODO - maybe should create the pipes once for the lifetime of the program,
   not once per query, which is what is happening here
*)

let run b worker_info_list =
  let num_workers = List.length worker_info_list in
  (* TODO - these are going to need to be mutable *)
  let have_work = List.init num_workers  ~f:(fun _ -> ref false) in
  let requested_work_from = List.init num_workers  ~f:(fun _ -> ref false) in
  let first_job : Job.t = {goals = b; env = []} in
  don't_wait_for
    (
      Connection.run_exn (Worker_info.conn (List.nth_exn worker_info_list 0)) ~f:(functions.eval_query) ~arg:first_job
    );
  (* TODO set 0th value of have_work to true*)
  Pipe.write_without_pushback  (List.nth_exn worker_info_list 0).writer ();
  (* TODO set 0th value of requested_work_from to true *)

  let rec run_inner results =
    (* TODO - check for updates from workers, handle accordingly. Give any work we have to any
    workers which do not currently have work *)
  in
  run_inner []

  (* monitor reader for results *)
  (* values_available returns a Deferred which becomes determined when there's a
  value available. No guarantees that another process won't have turned up and
  read the value before you get to it, but since we only have one process reading
  from this pipe, that's fine
  *)
  let%bind _ = Pipe.values_available (Worker_info.reader (List.nth_exn worker_info_list 0))
  in
  let%bind _ =
    match%bind Pipe.read (Worker_info.reader (List.nth_exn worker_info_list 0)) with
  | `Eof -> (print_endline "No results from worker"; return ())
  | `Ok msg -> (
      match msg with
      | Worker_to_toplevel.Results _ -> return ()
      | Worker_to_toplevel.Job job ->
        don't_wait_for
          (
            Connection.run_exn (Worker_info.conn (List.nth_exn worker_info_list 1)) ~f:(functions.eval_query) ~arg:job
          ); return ()
      | Request -> print_endline "Was meant to get results, but got\
                                           a request for work instead.";
        return ()
    )
  in
  let%bind res1 =
    match%bind Pipe.read (Worker_info.reader (List.nth_exn worker_info_list 0)) with
  | `Eof -> (print_endline "No results from worker"; return [])
  | `Ok msg -> (
      match msg with
      | Worker_to_toplevel.Results res -> return res
      | Worker_to_toplevel.Job _
      | Request -> print_endline "Was meant to get results, but got\
                                  a request for work instead.";
        return []
    )
  in
  let%bind res2 = 
    match%bind Pipe.read (Worker_info.reader (List.nth_exn worker_info_list 1)) with
    | `Eof -> (print_endline "No results from worker"; return [])
    | `Ok msg -> (
        match msg with
        | Worker_to_toplevel.Results res -> return res
        | Worker_to_toplevel.Job _
        | Request -> print_endline "Was meant to get results, but got\
                                    a request for work instead.";
          return []
      )
  in
  res1@res2 |> return
;;

let main filename =
  let%bind workers_info = init_workers 2 in
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
                        let%bind res = run b workers_info in
                        (* print the result *)
                        print_string "\n";
                        print_endline (string_of_res (res) orig_vars orig_vars_num);
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
      in
      fun () -> main filename
    ]


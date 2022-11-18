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
    | No_work
  [@@deriving bin_io]
end

module Toplevel_to_worker = struct
  type t = Request
  [@@deriving bin_io]
end

module T = struct

  module Worker_state = struct
    type init_arg = dec list
    [@@deriving bin_io]

    type t = {
      q : Job.t Deque.t;
      mutable db : dec list;
      mutable reader : Toplevel_to_worker.t Pipe.Reader.t;
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
      (* ({q; db; results; reader; writer}: Worker_state.t) = *)
    let rec main_inner results =
      let%bind _check_for_update =
        if not (Pipe.is_empty worker_state.reader) then (
          match%bind Pipe.read worker_state.reader with
          | `Eof -> return ()
          | `Ok (Request) -> (
              match Deque.dequeue_front worker_state.q with
              | None -> Pipe.write worker_state.writer No_work
              | Some job -> Pipe.write worker_state.writer (Job job)
            )
        ) else Deferred.unit
      in
      match Deque.dequeue_back worker_state.q with
      | None -> (let%bind _write = Pipe.write worker_state.writer (Results results) in
                 Pipe.write worker_state.writer Request
                   (* Need to wait for a response before we decide to keep looping.
                   Could do something with an ivar? Or we could just return here, and
                   then the toplevel has to call main/eval again to get us to do
                   any more work. That might actually be easiest? But then we need to
                   be able to call this function with additional work to do as an arg.
                      In which case we wouldn't need the toplevel to be able to send work
                      via a pipe - it would only be sent when we call this function
                   *)
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

  type 'worker functions = {eval_query : ('worker, Job.t, unit) Rpc_parallel_edit.Function.t;
                           update_db : ('worker, dec, unit) Rpc_parallel_edit.Function.t}

  module Functions
      (C : Rpc_parallel_edit.Creator
       with type worker_state := Worker_state.t
        and type connection_state := Connection_state.t) =
  struct
    let eval_query_impl ~worker_state ~conn_state:() job =
      Deque.enqueue_back worker_state.q job;
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
        ~bin_update:Toplevel_to_worker.bin_t
        ~bin_response:Unit.bin_t
        ()

    let functions = {eval_query; update_db}
    let init_worker_state init_arg = initialise init_arg |> return
    let init_connection_state ~connection:_ ~worker_state:_ = return

  end
end

include Rpc_parallel_edit.Make (T)

(* NOTE - we need to use functions such that the worker can be interrupted in
   between executions of jobs on the stack. It would therefore probably be useful
   to have some sort of stack structure which `interrupts' the worker when anything on it
   changes - that way, the execution control would be handled by this stack and by
   the toplevel, rather than by the worker, in which case we can't interrupt it.
   At initialisation, we could start a function which waits for these interrupts
   from the stack, and responds to them. This is getting excessively complex for
   an interpreter though. There must be a way to avoid having to do all of that.
   We could also have a recursive main process which checks for updates to its state
   (and we have something in the state to allow the toplevel to make a request for
   work, or to request a status update - maybe just some sort of flag), and it
   handles those other requests before it continues with execution of the Prolog.
   This would rely on the processing model allowing the toplevel to update that state
   even while the worker is running this recursive function. This is probably
   doable with a pipe_rpc, since it just requires this worker to check it periodically,
   and not for the main process to interrupt it.

   The only way to find out is to try it, I guess. Or maybe inspect the parallel.ml
   really thoroughly.

   So I'll need to initialise each worker, which may involve giving it work.
   Then need to set up a pipe between the main process and each worker where
   workers can request work, the toplevel can request work, the worker can send solutions.
   This is likely to require a very strange message format. Maybe we just have `request
   for worker' messages in this pipe, and the main process has an rpc which gives the worker
   work, which the worker adds to its stack, the worker then sends solutions as a response,
   then starts doing the actual work. If that's not a viable layout, we could also
   have a separate `start working' call. Or we could have the pipe take messages
   consisting of a request for work and solutions so far. To be fair, just sending solutions
   so far might be sufficient, since we would only be sending solutions if we didn't
   have any work left.

   I am making some assumptions here about how the pipe_rpc actually works -
   I'm not sure how the worker accesses the reader and writer, exactly, if it
   can at all.

   Could I use the connection state at all?

   The create_pipe takes a function f, which is given an argument and the pipe writer.
   The argument is presumably what has been read from the pipe.

   There is also the create_reverse_pipe, which could work in the other direction,
   giving the worker a pipe reader. This would be more useful. The worker does have to
   send a response, but "It is up to you whether to send a response before or after
   finishing with the pipe". Not exactly sure how you go about sending the response
   without returning from the function though? Unless we call another function, and
   have a don't_wait_for? That seems like it could go wrong

*)

(* TODO - at some point, will need to reformulate this so that we start the
workers to begin with, rather than only when we get a query. At the moment,
we'll be starting a new worker to deal with each query. *)

(* TODO - need to extend the heartbeater timeout time - this is done in the
   start_app function call. Also would need to make sure
the workers are actually being interrupted as needed, and don't just attempt to
finish computation before handling any queries from the main process.
Otherwise, we'll never actually manage to take any work from the workers,
and will end up with one worker doing all the work
*)
let run b db =
  let%bind worker : t Deferred.t =
    spawn_exn
      ~on_failure:Error.raise
      ~shutdown_on:Heartbeater_connection_timeout
      ~redirect_stdout:(`File_append "/Users/em/Documents/diss_stdout.log")
      ~redirect_stderr:(`File_append "/Users/em/Documents/diss_stderr.log")
      {b; db}
  in
  let%bind conn = Connection.client_exn worker () in
  Connection.run_exn conn ~f:(functions.eval_query) ~arg:()



let main filename =
   (
    let%bind () = (
          let rec loop db file_lines =
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
                    let%bind newdb = (
                    match dec with
                    | Clause (_, _) -> add_dec_to_db (dec, db) |> return
                    | Query b -> (
                        print_endline s;
                        (* find all uniq VarExps in query *)
                        let orig_vars = uniq (find_vars b) in
                        (* find num of VarExps in query *)
                        let orig_vars_num = List.length orig_vars in
                        (* evaluate query *)
                        let%bind res = run b db in
                        (* print the result *)
                        print_string "\n";
                        print_endline (string_of_res (res) orig_vars orig_vars_num);
                        print_string "\n\n";
                        (* reset fresh variable counter *)
                        reset ();
                        return db
                      )
                  ) in
                    loop newdb ss
                  ) with
                  | Failure f -> ( (* in case of an error *)
                      print_endline ("Failure: " ^ f ^ "\n");
                      loop db ss
                    )
                  | Parser.Error -> ( (* failed to parse input *)
                      print_endline "\nDoes not parse\n";
                      loop db ss
                    )
                  | Lexer.EndInput -> exit 0 (* EOF *)
                  | _ -> ( (* Any other error *)
                      print_endline "\nUnrecognized error\n";
                      loop db ss
                    )
                )
              | [] -> return ()
            )
          in
          print_endline ("Opening file " ^ filename ^ "\n");
          let file_lines = In_channel.read_lines filename in
          let%bind () = loop [] file_lines in
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

(* TODO - I think this is giving bad output because of the backend I'm
using here - it's possible I would need to use a For_testing backend.
Unsure. See parallel_intf.ml or parallel.ml for info about For_testing.
initialize
I possibly would have to define a separate library which deals with
   the expect tests, which uses For_testing, and then another library
   which could be used by the executable. That sounds like a lot of faff.
   I could maybe just have a separate tests.ml file which calls
   this function with
*)
(* let%expect_test "general test" = *)
(*   let%bind _ = main "nqueensgen.pl" in *)
(*   [%expect {| *)
(*     861 |}]; *)
(*   return () *)
(* ;; *)


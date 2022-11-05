open Core
open Async
open! Rpc_parallel
open Ast
open Util

module Results = struct
  type t = (exp * exp) list list [@@deriving bin_io]
end

module Worker = struct
  module T = struct
    (* TODO - the init_arg needs to give the rules (with any subsitutions needed to
       be able to treat the problem as isolated already done), the query to be
       solved, potentially the `location' of the node it's starting the search from,
       for later aggregation of solutions.

       Worker_state.t itself will need to hold all of this information, plus a stack
       of work to be done (from which work to be given to others can be drawn), plus
       any solutions generated so far.
    *)

    module Worker_state = struct
      type init_arg = {
        b : exp list;
        db : dec list
      }
      [@@deriving bin_io]

      (* TODO - make these mutable, so we can update results etc as we go - don't need
      to be making multiple copies in the eval_inner function *)
      (* TODO - could add a `done' field here, if we end up having to have a polling
      process for giving the worker work. We could then have the main process periodically
      check for results (and take any if there are, resetting results to []), and
      check if the processing has finished yet. And if so, give it more work. *)
      type t = {
        q : (exp list * (exp * exp ) list) Deque.t;
        db : dec list;
        results : (exp * exp) list list
      }
    end

    module Connection_state = struct
      type init_arg = unit [@@deriving bin_io]
      type t = unit
    end

    (* TODO - would it make sense to have the recursive part as an inner function,
       then we don't need to pass the db every time? *)
    (* TODO - might make sense to switch to iteration rather than recursion? *)
    let rec eval_inner ({q; db; results}: Worker_state.t) =
      match Deque.dequeue_back q with
      | None -> return results    (* no more of the tree to search so finished *)
      | Some ([], env) -> eval_inner {q; db; results = (env::results)} (* No further subgoals to prove in this job
                                                            so add the substitution to the results *)
      | Some (g1::gl, env) -> ((
          (* we have at least one more subgoal (g1) to prove in this job *)
          match g1 with
          | TermExp("true", []) -> Deque.enqueue_back q (gl, env)
          | TermExp("equals", [lhs; rhs]) -> (
              match unify [(lhs, rhs)] with
              | Some s -> (
                  match unify (s@env) with
                  | Some env2 -> Deque.enqueue_back q (sub_lift_goals s gl, env2)
                  | None -> ()
                )
              | None -> ()
            )
          | TermExp("not_equal", [lhs;rhs]) -> (
              match unify [(lhs, rhs)] with
              | Some s -> (
                  match unify (s@env) with
                  | Some _ -> ()
                  | None -> Deque.enqueue_back q (gl, env)
                )
              | None -> Deque.enqueue_back q (gl, env)
            )
          | TermExp("greater_than", [lhs; rhs]) -> (
              match lhs, rhs with
              | IntExp i1, IntExp i2 -> if i1 > i2 then Deque.enqueue_back q (gl, env)
              | _ -> () (* arguments insufficiently instantiated *)
            )
          | TermExp("less_than", [lhs; rhs]) ->
            (
              match lhs, rhs with
              | IntExp i1, IntExp i2 -> if i1 < i2 then Deque.enqueue_back q (gl, env)
              | _ -> () (* arguments insufficiently instantiated *)
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
                            Deque.enqueue_back q (
                              sub_lift_goals [(lhs, IntExp result)] gl,
                              env2
                            )
                          | None -> ()
                        )
                      | IntExp i -> if i = result then Deque.enqueue_back q (gl, env)
                      | _ -> ()
                    )
                  | _ -> ()
                )
              | IntExp result -> (
                  match lhs with
                  | VarExp _ ->
                    ( match unify ((lhs, rhs)::env) with
                      | Some env2 ->
                        Deque.enqueue_back q (
                          sub_lift_goals [(lhs, rhs)] gl,
                          env2
                        )
                      | None -> ()
                    )
                  | IntExp i -> if i = result then Deque.enqueue_back q (gl, env)
                  | _ -> ()
                )
              | _ -> ()
            )
          (* if goal is some other predicate *)
          | TermExp(_,_) -> (
              (* iterate over the db, adding matching rules to be checked. Afterwards, call recursively *)
              List.iter db
                ~f:(fun rule ->
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
                                     fact) then recurse on remaining subgoals *)
                                  | ((TermExp ("true", _)) :: _) ->
                                    Deque.enqueue_back q (
                                      sub_lift_goals s gl,
                                      env2
                                    )
                                  | _ ->
                                    Deque.enqueue_back q (
                                      (sub_lift_goals s body) @ (sub_lift_goals s gl),
                                      env2
                                    )
                                )
                                else
                                  Deque.enqueue_back q (
                                    (sub_lift_goals s body) @ (sub_lift_goals s gl),
                                    env2
                                  )
                              )
                            | _ -> ()
                          )
                        (* this rule's head doesn't unify with the subgoal *)
                        | _ -> ()
                      )
                    |  _ -> ()
                  )
            )
          (* subgoal g1 isn't a TermExp *)
          | _ -> Deque.enqueue_back q (gl, env)
        );
         eval_inner {q; db; results}
        )

    let initialise (init_arg : Worker_state.init_arg) : Worker_state.t  =
      let q = Deque.create () in
      Deque.enqueue_front q (init_arg.b, []);
      {q; db = init_arg.db; results = []}

    (* TODO - will need to add functions for updating the worker with new work when
       it runs out. This will be pretty much the same as the spawn function in terms of
       the information it needs to be passed. For now, we're having a sequential interpreter
       in one worker, so we don't need to implement this function immediately.
    *)
    (* TODO - need the worker to be able to inform the main process when it's finished
       working. Not sure if this is gonna have to be a system of polling, where the main
       process periodically checks if the work is done, or if the worker can interrupt
       the main process.
    *)
    type 'worker functions = {eval_query : ('worker, unit, Results.t) Rpc_parallel.Function.t}

    module Functions
        (C : Rpc_parallel.Creator
         with type worker_state := Worker_state.t
          and type connection_state := Connection_state.t) =
    struct
      let eval_query_impl ~worker_state ~conn_state:() _ =
        eval_inner worker_state
      ;;

      let eval_query =
        C.create_rpc
          ~f:eval_query_impl
          ~bin_input:(Unit.bin_t)
          ~bin_output:(Results.bin_t)
          ()

      let functions = {eval_query}
      let init_worker_state init_arg = initialise init_arg |> return
      let init_connection_state ~connection:_ ~worker_state:_ = return
    end

  end

  include Rpc_parallel.Make (T)
end

type t = Worker.Connection.t

(* let spawn b db = *)
(*   let%map worker = *)
(*   Worker.spawn_exn *)
(*     ~redirect_stdout:`Dev_null (\* TODO - switch this to `File_append or `File_truncate at some point*\) *)
(*     ~redirect_stderr:`Dev_null *)
(*     ~on_failure:Error.raise *)
(*     ~shutdown_on:Heartbeater_connection_timeout *)
(*     {b; db} *)
(*   in *)
(*   worker *)


(* let eval_query t = *)
(*   let%bind conn = Worker.Connection.client_exn t () in *)
(*   Worker.Connection.run_exn conn  ~f:(Worker.functions.eval_query) ~arg:() *)

let run b db =
  let%bind worker =
    Worker.spawn_exn
      ~redirect_stdout:`Dev_null (* TODO - switch this to `File_append or `File_truncate at some point*)
      ~redirect_stderr:`Dev_null
      ~on_failure:Error.raise
      ~shutdown_on:Heartbeater_connection_timeout
      {b; db}
  in
  let%bind conn = Worker.Connection.client_exn worker () in
  Worker.Connection.run_exn conn ~f:(Worker.functions.eval_query) ~arg:()

let command : Async.Command.t =
  Async.Command.async
    ~summary:"Parallel Prolog interpreter"
    [%map_open.Command
      let _filename =
        flag
          ~doc:"FILE optional file to read prolog from"
          "file"
          (optional string)
      in
      fun () -> return ()
        (* Interface.main filename ~eval_function:(fun db b -> run b db ) *)
    ]

(* let () =  *)
(* let backend_and_settings = Rpc_parallel.Backend_and_settings.T ((module Backend), ()) in *)
(* Rpc_parallel.start_app *)
(*   backend_and_settings *)
(*   Prolog_interpreter.Main.command *)

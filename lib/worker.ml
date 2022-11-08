open Core
open Async
open Ast
open Parser
open Util

module Results = struct
  type t = (exp * exp) list list [@@deriving bin_io]
end

module T = struct
  type 'worker functions = {eval_query : ('worker, unit, Results.t) Rpc_parallel_edit.Function.t}

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


  module Functions
      (C : Rpc_parallel_edit.Creator
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

include Rpc_parallel_edit.Make (T)

(* TODO - at some point, will need to reformulate this so that we start the
workers to begin with, rather than only when we get a query. At the moment,
we'll be starting a new worker to deal with each query. *)
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
    print_endline "\nWelcome to the Prolog Interpreter\n";
    let%bind () = (
          let rec loop db file_lines =
            (
              match file_lines with
              | s::ss -> (
                  try (
                    let lexbuf = Lexing.from_string s in
                    let dec = clause (
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

let () = Start_app.start_app command

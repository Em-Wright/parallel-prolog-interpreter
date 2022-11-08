open Core
open Ast
open Util

(*
   eval_inner:
     * takes in (all in a triple):
         q - a deque of (exp list * substitution list)
         db - a list of dec
         env - a list of substitutions
               where each substitution is of type (exp * exp)
     * returns a list of lists of substitutions where each
       substitution is of type (exp * exp)
         - if the returned list is empty then no solutions were found for the
           query for the given db
         - otherwise, each element is a list of substitutions for one solution
           to the query with the given db
*)
(* We'll be using the deque like a stack for now (i.e. taking from and adding to
   the back) and will only take from the front later, when we write a
   parallel version
*)
(* TODO - would it make sense to have the recursive part as an inner function,
then we don't need to pass the db every time? *)
(* TODO - might make sense to switch to iteration rather than recursion? *)
let rec eval_inner q db results =
  match Deque.dequeue_back q with
  | None ->  results    (* no more of the tree to search so finished *)
  | Some ([], env) -> eval_inner q db (env::results) (* No further subgoals to prove in this job
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
     eval_inner q db results
    )

let eval_query b db =
  let q = Deque.create () in
  Deque.enqueue_front q (b, []);
  eval_inner q db []

let command =
  Command.basic
    ~summary:"Stack-sequential Prolog interpreter"
    [%map_open.Command
      let filename =
        flag
          ~doc:"FILE optional file to read prolog from"
          "file"
          (optional string)
      in
      fun () -> Interface.main filename ~eval_function:(fun db b -> eval_query b db )
    ]

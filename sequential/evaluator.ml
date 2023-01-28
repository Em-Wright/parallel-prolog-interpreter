open Ast
open Core
open Util


(*
   eval_query:
     * takes in (all in a triple):
         q - a list of exp
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
let rec eval_query (q, db, env) =
    match q with
    | [] -> (
        (* no more subgoals to prove so finished *)
        ([env], false)
    )
    | (g1 :: gl) ->
      (  (* have at least one more subgoal (g1) to prove *)
        match g1 with
        (* if goal is the true predicate *)
        | TermExp("true", []) -> (
          eval_query (
              gl,
              db,
              env
          )
        )
        | TermExp("cut", []) -> (
            let (res, _) = eval_query ( gl, db, env ) in
            (res, true)
          )
        (* if the goal is the 'equals' predicate *)
        | TermExp("equals", [lhs; rhs]) -> (
            (* check if the lhs and rhs can unify *)
            match unify [(lhs, rhs)] with
            | Some s -> (
                match unify (s@env) with
                | Some env2 ->
                  (eval_query (
                      sub_lift_goals s gl,
                      db,
                      env2
                    ))
                | None -> ([], false)
              )
            | None -> ([], false)
          )
        | TermExp("not_equal", [lhs;rhs]) -> (
            (* check if the lhs and rhs can unify. If they can, this is not a
               successful substitution. If they don't, we can continue solving the
               rest of the goals
            *)
            match unify [(lhs, rhs)] with
            | Some s -> (
                match unify (s@env) with
                | Some _ -> ([], false)
                | None -> eval_query (gl, db, env)
              )
            | None -> eval_query (gl, db, env)
          )
        | TermExp("greater_than", [lhs; rhs]) -> (
          match lhs, rhs with
          | IntExp i1, IntExp i2 ->
            if i1 > i2 then
              eval_query (gl, db, env)
            else
              ([], false)
          | _ ->  ([], false) (* arguments insufficiently instantiated *)
        )
        | TermExp("greater_than_or_eq", [lhs; rhs]) -> (
            match lhs, rhs with
            | IntExp i1, IntExp i2 ->
              if i1 >= i2 then
                eval_query (gl, db, env)
              else
                ([], false)
            | _ ->  ([], false) (* arguments insufficiently instantiated *)
          )
        | TermExp("less_than", [lhs; rhs]) -> (
          match lhs, rhs with
          | IntExp i1, IntExp i2 ->
            if i1 < i2 then
              eval_query (gl, db, env)
            else
              ([], false)
          | _ ->  ([], false) (* arguments insufficiently instantiated *)
        )
        | TermExp("less_than_or_eq", [lhs; rhs]) -> (
            match lhs, rhs with
            | IntExp i1, IntExp i2 ->
              if i1 <= i2 then
                eval_query (gl, db, env)
              else
                ([], false)
            | _ ->  ([], false) (* arguments insufficiently instantiated *)
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
                      | VarExp _ ->
                          ( match unify ((lhs, IntExp result)::env) with
                              | Some env2 ->
                                eval_query (
                                  sub_lift_goals [(lhs, IntExp result)] gl,
                                  db,
                                  env2
                                )
                              | None ->  ([], false)
                            )
                      | IntExp i ->
                        if i = result then eval_query (gl, db, env) else  ([], false)
                      | _ ->  ([], false)
                    )
                  | _ ->  ([], false)
              )
            | IntExp result -> (
                match lhs with
                | VarExp _ ->
                    ( match unify ((lhs, rhs)::env) with
                        | Some env2 ->
                          eval_query (
                            sub_lift_goals [(lhs, rhs)] gl,
                            db,
                            env2
                          )
                        | None ->  ([], false)
                      )
                | IntExp i -> (
                    if i = result then eval_query (gl, db, env) else ([], false)
                  )
                | _ -> ([], false)
              )
            | _ -> ([], false)
            )
        (* if goal is some other predicate *)
        | TermExp(_,_) -> (
        (* iterate over the db *)
        let x = ref 0 in
        List.fold_until ~finish:(fun x -> x) ~f:(
            fun (r, _) rule -> (
                x := !x + 1;
                match (rename_vars_in_dec rule) with (* rename vars in rule to completely fresh ones *)
                | Clause (h, b) -> (
                    (* check if this rule can be used for this subgoal *)
                    match unify [(g1, h)] with
                    (* s is a list of substitutions which allows g1 and h to unify *)
                    | Some s -> (
                        match unify (s@env) with
                        (* env2 is the new set of substitutions which is compatible with the original env
                        and with the new set of substitutions s *)
                        | Some env2 -> (
                            if (List.length b = 1)
                            then (
                                match b with
                                (* if the rule proved the subgoal (ie. rule was a
                                   fact) then recurse on remaining subgoals *)
                                | ((TermExp ("true", _)) :: _) ->
                                  let (res, cut) =
                                    (eval_query (
                                        sub_lift_goals s gl,
                                        db,
                                        env2
                                     ))
                                  in
                                  if cut then Stop (res @ r, false)
                                  else Continue (res @ r, false)
                                (* if rule wasn't a fact then we have more
                                   subgoals from the body of the rule
                                   to prove
                                   sub_lift_goals takes our substitution list, and a list of goals,
                                   and returns the goals with the substitution applied.
                                *)
                                | _ ->
                                  (
                                    let (res, cut) = (eval_query (
                                        (sub_lift_goals s b) @ (sub_lift_goals s gl),
                                        db,
                                        env2
                                      ))
                                    in
                                    if cut then Stop (res @ r, false)
                                    else Continue (res @ r, false)
                                  )
                              )
                            else
                                (* if rule wasn't a fact then we have more
                                   subgoals from the body of the rule
                                   to prove
                                   we fold the result of evaluating the query with the other possible
                                   solutions in r
                                *)
                              (
                                let (res, cut) = (eval_query (
                                    (sub_lift_goals s b) @ (sub_lift_goals s gl),
                                    db,
                                    env2
                                  ))
                                in
                                if cut then Stop (res @ r, false)
                                else Continue (res @ r, false)
                              )
                          )
                        (* the substitution from unify the rule head and subgoal
                           doesn't unify with the environment gathered so far *)
                        | _ -> Continue (r, false)
                    )
                    (* this rule's head doesn't unify with the subgoal *)
                    | _ -> Continue (r, false)
                )
                (* found a dec in the db that isn't a Clause *)
                |  _ -> Continue (r, false)
          )) db ~init:([], false) )
        (* subgoal isn't a TermExp (i.e. is a VarExp or a ConstExp) *)
        | _ -> eval_query (gl, db, env)
    )


let command =
  Command.basic
    ~summary:"Sequential Prolog interpreter"
    [%map_open.Command
       let filename =
         flag
           ~doc:"FILE to read prolog from"
           "file"
           (required string)
       in
       fun () ->
         Interface.main filename ~eval_function:(fun db b ->
             let (res,_) = eval_query (b, db, []) in res )
    ]

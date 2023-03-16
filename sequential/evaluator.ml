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

(* TODO switch the true/false cuts for int options, where the int is the depth of the cut,
then make sure cuts are carried on if the depth is lower than yours, and only implement a
cut where the depth matches
   Or the depth is the cut depth - 1? or maybe we set the cut depth as the current depth-1.
   We need to associate a depth with every goal - when we expand a goal, the body elements
   should have the depth of that goal + 1.
   A cut only lasts until the first time it is `used'
*)
let rec eval_query (q, db, env) orig_vars =
    match q with
    | [] -> (
        (* no more subgoals to prove so finished *)
        ([env], None)
    )
    | ((g1, depth) :: gl) ->
      (* TODO - get all vars in the goals, add to orig_vars, filter out any elts of
      the environment which aren't in this list
      *)
      let vars_set_string = String.Set.of_list (find_vars_string q) |> String.Set.union orig_vars
      in
      let env =
        List.filter env ~f:(fun (v, _) ->
            match v with
            | VarExp elt -> String.Set.exists vars_set_string ~f:(fun a -> String.equal elt a)
            | _ -> false
          )
      in
      (  (* have at least one more subgoal (g1) to prove *)
        match g1 with
        (* if goal is the true predicate *)
        | TermExp("true", []) -> (
          eval_query (
              gl,
              db,
              env
          ) orig_vars
        )
        | TermExp("cut", []) -> (
            let (res, _) = eval_query ( gl, db, env ) orig_vars in
            (res, Some (depth-1))
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
                    ) orig_vars )
                | None -> ([], None)
              )
            | None -> ([], None)
          )
        | TermExp("not_equal", [lhs;rhs]) -> (
            (* check if the lhs and rhs can unify. If they can, this is not a
               successful substitution. If they don't, we can continue solving the
               rest of the goals
            *)
            match unify [(lhs, rhs)] with
            | Some s -> (
                match unify (s@env) with
                | Some _ -> ([], None)
                | None -> eval_query (gl, db, env) orig_vars depth
              )
            | None -> eval_query (gl, db, env) orig_vars depth
          )
        | TermExp("greater_than", [lhs; rhs]) -> (
          match lhs, rhs with
          | IntExp i1, IntExp i2 ->
            if i1 > i2 then
              eval_query (gl, db, env) orig_vars depth
            else
              ([], None)
          | _ ->  ([], None) (* arguments insufficiently instantiated *)
        )
        | TermExp("greater_than_or_eq", [lhs; rhs]) -> (
            match lhs, rhs with
            | IntExp i1, IntExp i2 ->
              if i1 >= i2 then
                eval_query (gl, db, env) orig_vars depth
              else
                ([], None)
            | _ ->  ([], None) (* arguments insufficiently instantiated *)
          )
        | TermExp("less_than", [lhs; rhs]) -> (
          match lhs, rhs with
          | IntExp i1, IntExp i2 ->
            if i1 < i2 then
              eval_query (gl, db, env) orig_vars depth
            else
              ([], None)
          | _ ->  ([], None) (* arguments insufficiently instantiated *)
        )
        | TermExp("less_than_or_eq", [lhs; rhs]) -> (
            match lhs, rhs with
            | IntExp i1, IntExp i2 ->
              if i1 <= i2 then
                eval_query (gl, db, env) orig_vars depth
              else
                ([], None)
            | _ ->  ([], None) (* arguments insufficiently instantiated *)
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
                                ) orig_vars depth
                              | None ->  ([], None)
                            )
                      | IntExp i ->
                        if i = result then eval_query (gl, db, env) orig_vars depth else  ([], None)
                      | _ ->  ([], None)
                    )
                  | _ ->  ([], None)
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
                          ) orig_vars depth
                        | None ->  ([], None)
                      )
                | IntExp i -> (
                    if i = result then eval_query (gl, db, env) orig_vars depth else ([], None)
                  )
                | _ -> ([], None)
              )
            | _ -> ([], None)
            )
        (* if goal is some other predicate *)
        | TermExp(_,_) -> (
        (* iterate over the db *)
        let x = ref 0 in
        List.fold_until ~finish:(fun x -> x) ~f:(
          (* TODO - need to actually fold over the cuts? So we can't just ignore it with (r, _) *)
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
                                     ) orig_vars (depth + 1))
                                  in
                                  (
                                    match cut with
                                    | Some d -> if Int.equal d  then Stop (res @ r, None)
                                      else Continue (res @ r, cut)
                                    | None -> Continue (res @ r, None)
                                  )
                                (* if rule wasn't a fact then we have more
                                   subgoals from the body of the rule
                                   to prove
                                   sub_lift_goals takes our substitution list, and a list of goals,
                                   and returns the goals with the substitution applied.
                                *)
                                | _ ->
                                  (
                                    let (res, cut) = (eval_query (
                                        (* TODO if we have a cut in the body b, it needs to be carried
                                        back through all the goals in b
                                           could use some sort of depth/nesting indicator - we pass
                                           cuts back until we hit somewhere with the same depth on that cut
                                           i.e. if one of the subgoals before the cut goal expands, the
                                           depth of those subgoals will be 1 greater than the cut, and so
                                           we won't cut any of those
                                        *)
                                        (sub_lift_goals s b) @ (sub_lift_goals s gl),
                                        db,
                                        env2
                                      ) orig_vars (depth))
                                    in
                                    if cut then Stop (res @ r, None)
                                    else Continue (res @ r, None)
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
                                  ) orig_vars (depth + 1))
                                in
                                if cut then Stop (res @ r, None)
                                else Continue (res @ r, None)
                              )
                          )
                        (* the substitution from unify the rule head and subgoal
                           doesn't unify with the environment gathered so far *)
                        | _ -> Continue (r, None)
                    )
                    (* this rule's head doesn't unify with the subgoal *)
                    | _ -> Continue (r, None)
                )
                (* found a dec in the db that isn't a Clause *)
                |  _ -> Continue (r, None)
          )) db ~init:([], None) )
        (* subgoal isn't a TermExp (i.e. is a VarExp or a ConstExp) *)
        | _ -> eval_query (gl, db, env) orig_vars
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
             let orig_vars = find_vars_string b |> String.Set.of_list in
             let (res,_) = eval_query (b, db, []) orig_vars in res )
    ]

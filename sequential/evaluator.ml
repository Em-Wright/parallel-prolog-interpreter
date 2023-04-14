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

let rec eval_query (q, db, env) orig_vars =
    match q with
    | [] -> (
        (* no more subgoals to prove so finished *)
        ([env], [])
    )
    | ((g1, depth) :: gl) ->
      let q2, _ = List.unzip q in
      let vars_set_string = String.Set.of_list (find_vars_string q2) |> String.Set.union orig_vars
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
            let (res, cut) = eval_query ( gl, db, env ) orig_vars in
            (res, (depth-1)::cut)
          )
        (* if the goal is the 'equals' predicate *)
        | TermExp("equals", [lhs; rhs]) -> (
            (* check if the lhs and rhs can unify *)
            match unify [(lhs, rhs)] with
            | Some s -> (
                match unify (s@env) with
                | Some env2 ->
                  (eval_query (
                      sub_lift_goals_cut s gl,
                      db,
                      env2
                    ) orig_vars )
                | None -> ([], [])
              )
            | None -> ([], [])
          )
        | TermExp("not_equal", [lhs;rhs]) -> (
            (* check if the lhs and rhs can unify. If they can, this is not a
               successful substitution. If they don't, we can continue solving the
               rest of the goals
            *)
            match unify [(lhs, rhs)] with
            | Some s -> (
                match unify (s@env) with
                | Some _ -> ([], [])
                | None -> eval_query (gl, db, env) orig_vars
              )
            | None -> eval_query (gl, db, env) orig_vars
          )
        | TermExp("greater_than", [lhs; rhs]) -> (
          match lhs, rhs with
          | IntExp i1, IntExp i2 ->
            if i1 > i2 then
              eval_query (gl, db, env) orig_vars
            else
              ([], [])
          | _ ->  ([], []) (* arguments insufficiently instantiated *)
        )
        | TermExp("greater_than_or_eq", [lhs; rhs]) -> (
            match lhs, rhs with
            | IntExp i1, IntExp i2 ->
              if i1 >= i2 then
                eval_query (gl, db, env) orig_vars
              else
                ([], [])
            | _ ->  ([], []) (* arguments insufficiently instantiated *)
          )
        | TermExp("less_than", [lhs; rhs]) -> (
          match lhs, rhs with
          | IntExp i1, IntExp i2 ->
            if i1 < i2 then
              eval_query (gl, db, env) orig_vars
            else
              ([], [])
          | _ ->  ([], []) (* arguments insufficiently instantiated *)
        )
        | TermExp("less_than_or_eq", [lhs; rhs]) -> (
            match lhs, rhs with
            | IntExp i1, IntExp i2 ->
              if i1 <= i2 then
                eval_query (gl, db, env) orig_vars
              else
                ([], [])
            | _ ->  ([], []) (* arguments insufficiently instantiated *)
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
                                  sub_lift_goals_cut [(lhs, IntExp result)] gl,
                                  db,
                                  env2
                                ) orig_vars
                              | None ->  ([], [])
                            )
                      | IntExp i ->
                        if i = result then eval_query (gl, db, env) orig_vars else  ([], [])
                      | _ ->  ([], [])
                    )
                  | _ ->  ([], [])
              )
            | IntExp result -> (
                match lhs with
                | VarExp _ ->
                    ( match unify ((lhs, rhs)::env) with
                        | Some env2 ->
                          eval_query (
                            sub_lift_goals_cut [(lhs, rhs)] gl,
                            db,
                            env2
                          ) orig_vars
                        | None ->  ([], [])
                      )
                | IntExp i -> (
                    if i = result then eval_query (gl, db, env) orig_vars else ([], [])
                  )
                | _ -> ([], [])
              )
            | _ -> ([], [])
            )
        (* if goal is some other predicate *)
        | TermExp(_,_) -> (
        (* iterate over the db *)
        List.fold_until ~finish:(fun x -> x) ~f:(
            fun (r, acc_cuts) rule -> (
                match (rename_vars_in_dec rule) with (* rename vars in rule to completely fresh ones *)
                | Clause (h, b) -> (
                    match unify [(g1, h)] with
                    | Some s -> (
                        match unify (s@env) with
                        | Some env2 ->
                              ( let b2 = List.zip_exn b (List.init (List.length b) ~f:(fun _ -> depth+1)) in
                                let (res, cut) = (eval_query (
                                    (sub_lift_goals_cut s b2) @ (sub_lift_goals_cut s gl),
                                    db,
                                    env2
                                  ) orig_vars )
                                in
                                (
                                  match cut with
                                  | d::cuts ->
                                    if Int.equal d depth then Stop (res @ r, cuts@acc_cuts)
                                    else if d < depth then Stop (res @ r, (d::cuts)@acc_cuts)
                                    else (
                                      print_endline "something has gone terribly wrong";
                                      Continue (res @ r, cut@acc_cuts))
                                  | [] -> Continue (res @ r, acc_cuts)
                                )
                              )
                        (* the substitution from unify the rule head and subgoal
                           doesn't unify with the environment gathered so far *)
                        | _ -> Continue (r, acc_cuts)
                    )
                    (* this rule's head doesn't unify with the subgoal *)
                    | _ -> Continue (r, acc_cuts)
                )
                (* found a dec in the db that isn't a Clause *)
                |  _ -> Continue (r, acc_cuts)
          )) db ~init:([], []) )
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
             let b2 = List.zip_exn b (List.init (List.length b) ~f:(fun _ -> 0)) in
             let (res,_) = eval_query (b2, db, []) orig_vars in
             res
           )
    ]

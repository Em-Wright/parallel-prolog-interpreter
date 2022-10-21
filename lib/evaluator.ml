open Ast
open Common

exception FAILED_SUBSTITUTION of string


(*
   fresh:
      * takes in:
          unit
      * returns a string of the increment of the counter
   reset:
      * takes in:
          unit
      * returns unit and the counter is reset
*)
let (fresh, reset) =
    let nxt = ref 0 in
    let f () = (nxt := !nxt + 1; string_of_int (!nxt)) in
    let r () = nxt := 0 in
    (f, r)

(*
   find_vars:
     * takes in:
         q - a list of exp
     * returns a list of all VarExp (and ArithmeticVar as VarExp) in the list
*)
let rec find_vars q  =
    match q with
    | [] -> []
    | (x :: xs) -> (
        match x with
        | VarExp _ -> x :: (find_vars xs)
        | IntExp _ -> (find_vars xs)
        | TermExp (_, el) -> (find_vars el) @ (find_vars xs)
        | ArithmeticExp (_, e1, e2) ->
          match e1,e2 with
          | ArithmeticVar v1, ArithmeticVar v2 -> (VarExp v1)::((VarExp v2):: (find_vars xs))
          | _, ArithmeticVar v2 -> (VarExp v2):: (find_vars xs)
          | ArithmeticVar v1, _ -> (VarExp v1):: (find_vars xs)
          | _ -> (find_vars xs)
    )

(*
   uniq:
     * takes in:
         l - a list
     * returns the list reversed with only one copy of each element
  adapted from https://rosettacode.org/wiki/Remove_duplicate_elements#OCaml
*)

let uniq l =
    let rec tail_uniq a l =
        match l with
        | [] -> a
        | hd :: tl ->
            tail_uniq (hd :: a) (List.filter (fun x -> (x <> hd) ) tl)
    in
    tail_uniq [] l


(*
   sub_lift_goal_arithmetic:
     * takes in:
         sub - a list of substitutions for variables
         a - an arithmetic sub-expression
     * returns the sub-expression with the substitutions applied
*)
let sub_lift_goal_arithmetic sub a =
  match a with
  | ArithmeticVar v -> (
      (* if this variable has a substitution do the substitution *)
      try let i = List.assoc (VarExp v) sub in
        match i with
        | IntExp i2 -> ArithmeticInt i2
        | VarExp v2 -> ArithmeticVar v2
        | _ -> raise (FAILED_SUBSTITUTION "Attempted to substitute an ArithmeticExp or a TermExp for a variable in\
                                          an arithmetic expression. If this has occurred, I've implemented\
                                          arithmetic wrong. Oops. ")
      with Not_found -> a
    )
  | _ -> a

(*
   sub_lift_goal:
     * takes in:
         sub - a list of substitutions for variables
         g - a goal of type exp
     * returns the goal with the substitutions applied
*)
let rec sub_lift_goal sub g =
    match g with
    | VarExp v -> (
        (* if this variable has a substitution do the substitution *)
        try let i = List.assoc g sub in i
        with Not_found -> VarExp v
    )
    | TermExp (s, el) ->
        TermExp (s, List.map (fun g1 -> sub_lift_goal sub g1) el)
    | ArithmeticExp (op, e1, e2) -> ArithmeticExp(op, sub_lift_goal_arithmetic sub e1, sub_lift_goal_arithmetic sub e2)
    | _  -> g

(*
   sub_lift_goals:
     * takes in:
         sub - a list of substitutions for variables
         gl - a list of goals each of type exp
     * returns the list of goals with the substitutions applied to each goal
*)
let sub_lift_goals sub gl =
    List.map (fun g1 -> sub_lift_goal sub g1) gl

(*
   rename_vars_in_dec:
     * takes in:
         d - a dec type
     * returns a dec with all the variables in d renamed to fresh variable names
*)
let rename_vars_in_dec d =
    match d with
    | Clause (h, b) ->
        let head_vars = find_vars [h] in
        let body_vars = find_vars b in
        (* find uniq vars from both head and body *)
        let vars = uniq (head_vars @ body_vars) in
        (* get fresh variable mappings *)
        let sub = List.map (fun x -> (x, VarExp (fresh()))) vars in
        (* substitute new names for variables *)
        Clause (sub_lift_goal sub h, sub_lift_goals sub b)
    | Query (b) ->
        (* find uniq vars in query *)
        let body_vars = find_vars b in
        (* get fresh variable mappings *)
        let vars = uniq (body_vars) in
        let sub = List.map (fun x -> (x, VarExp (fresh()))) vars in
        (* substitute new names for variables *)
        Query (sub_lift_goals sub b)

(*
   pairandcat:
     * takes in:
         sargs - a list of exps
         targs - a list of exps
         c - a list of constraints where each constraint is of type (exp * exp)
     * returns a new list of constraints where c is prepended with each entry
       from sargs is paired with a corresponding entry from targs
       to make a new constraint
     * used for implementing decompose for unification
     * sargs and targs must be the same length, otherwise an exception is thrown
*)
let rec pairandcat sargs targs c =
    match sargs with
    | [] -> (
        if (List.length targs = 0)
        then c
        else raise (Failure "sargs and targs should be the same length")
    )
    | (s :: ss) -> (
        match targs with
        | (t :: ts) -> pairandcat ss ts ((s, t) :: c)
        |  _ -> raise (Failure "sargs and targs should be the same length")
    )

(*
   replace:
     * takes in:
         c - a list of constraints where each constraint is of type (exp * exp)
         sub - a list of substitutions
     * returns a new list of constraints where the substitutions are applied to
       both sides of each constraint
*)
let rec replace c sub =
    match c with
    | [] -> []
    | ((s, t) :: xs) ->
        (sub_lift_goal sub s, sub_lift_goal sub t) :: (replace xs sub)

(*
   occurs:
     * takes in:
         n - a string
         t - an exp
     * returns true if n matches any variable names in t and false otherwise
*)
let rec occurs n t =
     match t with
     | VarExp m -> n = m
     | TermExp (_, el) ->
        List.fold_left (fun acc v -> acc || (occurs n v)) false el
     | ArithmeticExp (_, e1, e2) ->(
       match e1, e2 with
       | ArithmeticVar v1, ArithmeticVar v2 -> n = v1 || n = v2
       | ArithmeticVar v1, _ -> n = v1
       | _, ArithmeticVar v2 -> n = v2
       | _ -> false
     )
     | _ -> false

(*
   unify:
     * takes in:
         constraints - a list of constraints where each constraint
         is of type (exp * exp)
     * returns None if the constraints can't be unified,
       otherwise returns Some(i) where i is a list of substitutions
       that unify the constraints
*)

(* John suggested considering the language guarantee that unifying a variable with anything is O(1).
We have an occurs check in here, however, so it's not O(1), I don't think *)
let rec unify constraints =
    match constraints with
    | [] -> Some []
    | ((s, t) :: c') ->
        if s = t
        then unify c'  (* Delete *)
        else (
            match s with
            | VarExp(n) ->
                (* Eliminate *)
                if (occurs n t)
                then None
                  (* If the var n does not occur in expression t, then
                  generate c'', the new set of constraints with this
                  substitution t for s applied. Then attempt to unify
                  this new set of constraints. If that works, then
                  our substitution (s,t) is valid, and so we add it to
                  the front of the resulting unifier list, with any
                  relevant substitutions applied *)
                else let phi = replace c' [(s,t)] |> unify in (
                        match phi with
                        | None -> None
                        | Some l -> Some ((s, sub_lift_goal l t) :: l)
                     )
            | TermExp (sname, sargs) -> (
                match t with
                (* Orient *)
                | VarExp _ -> unify ((t, s) :: c')
                (* Decompose *)
                | TermExp (tname, targs) ->
                    if (tname = sname && List.length targs = List.length sargs)
                    then pairandcat sargs targs c' |> unify
                    else None
                | _ -> None
              )
            | _ -> ( (* Otherwise, we have s is an int or arithmetic expression, so we
                        can only unify it if t is a variable, and the unification needs
                        to be the other way round
                     *)
                match t with
                (* Orient *)
                | VarExp _ -> unify ((t, s) :: c')
                | _ -> None
            )
        )


let perform_arithmetic (op : arithmetic_operator) i1 i2 : int =
  match op with
  | PLUS  ->  (i1 + i2)
  | MINUS -> (i1 - i2)
  | MULT  -> (i1 * i2)
  | DIV   -> (i1 / i2)

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
        [env]
    )
    | (g1 :: gl) -> (  (* have at least one more subgoal (g1) to prove *)
        match g1 with
        (* if goal is the true predicate *)
        | TermExp("true", []) -> (
          eval_query (
              gl,
              db,
              env
            )
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
                | None -> []
              )
            | None -> []
          )
        | TermExp("not_equal", [lhs;rhs]) -> (
            (* check if the lhs and rhs can unify. If they can, this is not a
               successful substitution. If they don't, we can continue solving the
               rest of the goals
            *)
            match unify [(lhs, rhs)] with
            | Some s -> (
                match unify (s@env) with
                | Some _ -> []
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
              []
          | _ -> [] (* arguments insufficiently instantiated *)
        )
        | TermExp("less_than", [lhs; rhs]) -> (
          match lhs, rhs with
          | IntExp i1, IntExp i2 ->
            if i1 < i2 then
              eval_query (gl, db, env)
            else
              []
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
                      | VarExp _ ->
                          ( match unify ((lhs, IntExp result)::env) with
                              | Some env2 ->
                                eval_query (
                                  sub_lift_goals [(lhs, IntExp result)] gl,
                                  db,
                                  env2
                                )
                              | None -> []
                            )
                      | IntExp i ->
                        if i = result then eval_query (gl, db, env) else []
                      | _ -> []
                    )
                  | _ -> []
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
                        | None -> []
                      )
                | IntExp i -> (
                    if i = result then eval_query (gl, db, env) else []
                  )
                | _ -> []
              )
            | _ -> []
            )
        (* if goal is some other predicate *)
        | TermExp(_,_) -> (
        (* iterate over the db *)
        List.fold_right (
            fun rule r -> (
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
                                    ((eval_query (
                                        sub_lift_goals s gl,
                                        db,
                                        env2
                                     )) @ r)
                                (* if rule wasn't a fact then we have more
                                   subgoals from the body of the rule
                                   to prove
                                   sub_lift_goals takes our substitution list, and a list of goals,
                                   and returns the goals with the substitution applied.
                                *)
                                | _ -> ((eval_query (
                                    (sub_lift_goals s b) @ (sub_lift_goals s gl),
                                    db,
                                    env2
                                )) @ r))
                            else
                                (* if rule wasn't a fact then we have more
                                   subgoals from the body of the rule
                                   to prove
                                   we fold the result of evaluating the query with the other possible
                                   solutions in r
                                *)
                                ((eval_query (
                                    (sub_lift_goals s b) @ (sub_lift_goals s gl),
                                    db,
                                    env2
                                )) @ r)
                        )
                        (* the substitution from unify the rule head and subgoal
                           doesn't unify with the environment gathered so far *)
                        | _ -> r
                    )
                    (* this rule's head doesn't unify with the subgoal *)
                    | _ -> r
                )
                (* found a dec in the db that isn't a Clause *)
                |  _ -> r
          )) db [] )
        (* subgoal isn't a TermExp (i.e. is a VarExp or a ConstExp) *)
        | _ -> eval_query (gl, db, env)
    )

(*
   string_of_res:
     * takes in:
         e - a list of lists of substitutions where each
             substitution is of type (exp * exp)
         orig_query_vars - a list of uniq VarExps that appeared
                           in the original query
         orig_vars_num - number of uniq VarExps that appeared
                         in the original query
     * returns a string consisting of all substitutions of variables
       appearing in the original query of all solutions found and the
       word true if solution(s) were found and false otherwise
*)


let string_of_res e orig_query_vars orig_vars_num =
   (* iterate over e for each solution *)
   List.fold_left (
        fun r2 env ->
        if orig_vars_num > 0
        then
          "====================\n" ^
            (* iterate over original query vars to find their substitution *)
            (List.fold_left (
                 fun r d -> (
                   match d with
                   | VarExp v -> (
                     (* find variable substitution in the solution *)
                     try let f = List.assoc (VarExp v) env in (
                             match f with
                             | VarExp _ ->
                                (v ^ " is free\n") ^ r
                             | _ ->
                                (v ^ " = " ^ (
                                   readable_string_of_exp f) ^ "\n") ^ r
                           )
                     with Not_found -> (v ^ " is free\n") ^ r)
                   | _ -> r
                 )
               ) "" (orig_query_vars) ) ^
              "====================\n"  ^ r2
        else "" ^ r2
     )  (if List.length e > 0 (* if e is empty then there were no solutions *)
         then "true\n"
         else "false\n")
                  e

(*
   add_dec_to_db:
     * takes in (all in a tuple):
         dec - a dec type
         db - a list of dec types
     * returns db prepended with dec if dec is not
       of the pattern TermExp("true",_) as we don't want users to be able
       to redefine the "true" atom
       otherwise, db is returned
*)
let add_dec_to_db (dec, db) =
    match dec with
    | Clause (h, _) -> (
        match h with
        (* don't allow user to add a new definition of true *)
        | TermExp ("true", _) ->
            print_string "Can't reassign true predicate\n"; db
        | TermExp ("is", _) ->
          print_string "Can't reassign 'is' predicate\n"; db
        | TermExp ("list", _) ->
          print_string "Can't reassign 'list' predicate\n"; db
        | TermExp ("empty_list", _) ->
          print_string "Can't reassign 'empty_list' predicate\n"; db
        | TermExp ("equals", _) ->
          print_string "Can't reassign 'equals' predicate\n"; db
        | TermExp ("not_equal", _) ->
          print_string "Can't reassign 'not_equal' predicate\n"; db
        | TermExp ("less_than", _) ->
          print_string "Can't reassign 'less_than' predicate\n"; db
        | TermExp ("greater_than", _) ->
          print_string "Can't reassign 'greater_than' predicate\n"; db
        | _ -> dec :: db
    )
    | Query _ -> (
        dec :: db
    )

(*
   eval_dec:
     * takes in (all in a tuple):
         dec - a dec type
         db - a list of dec types
     * evaluated the dec with the given db
       returns the original db in the case
       dec is a Query type
       otherwise returns db prepended with dec
*)
let eval_dec (dec, db) =
    match dec with
    | Clause (_, _) -> add_dec_to_db (dec, db)
    | Query b -> (
        (* find all uniq VarExps in query *)
        let orig_vars = uniq (find_vars b) in
        (* find num of VarExps in query *)
        let orig_vars_num = List.length orig_vars in
        (* evaluate query *)
        let res = eval_query (b, db, []) in
        (* print the result *)
        print_string (string_of_res (res) orig_vars orig_vars_num);
        (* reset fresh variable counter *)
        reset ();
        db
    )

open Core
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
    let f () = (nxt := !nxt + 1;
                string_of_int (!nxt)) in
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
   find_vars_string:
     * takes in:
         q - a list of exp
     * returns a list of all VarExp (and ArithmeticVar) as strings in the list
*)
let rec find_vars_string q  =
  match q with
  | [] -> []
  | (x :: xs) -> (
      match x with
      | VarExp y -> y :: (find_vars_string xs)
      | IntExp _ -> (find_vars_string xs)
      | TermExp (_, el) -> (find_vars_string el) @ (find_vars_string xs)
      | ArithmeticExp (_, e1, e2) ->
        match e1,e2 with
        | ArithmeticVar v1, ArithmeticVar v2 -> v1::(v2:: (find_vars_string xs))
        | _, ArithmeticVar v2 -> v2:: (find_vars_string xs)
        | ArithmeticVar v1, _ -> v1:: (find_vars_string xs)
        | _ -> (find_vars_string xs)
    )
(*
   uniq:
     * takes in:
         l - an exp list
     * returns the list reversed with only one copy of each element
  adapted from https://rosettacode.org/wiki/Remove_duplicate_elements#OCaml
*)
let uniq (l : exp list) =
    let rec tail_uniq a l =
        match l with
        | [] -> a
        | hd :: tl ->
            tail_uniq (hd :: a)
              (List.filter
                 ~f:(fun x -> not (Ast.equal_exp x hd))
                 tl
              )
    in
    tail_uniq [] l


(*
   sub_lift_goal_arithmetic:
     * takes in:
         sub - a list of substitutions for variables
         a - an arithmetic sub-expression
     * returns the sub-expression with the substitutions applied
*)
let sub_lift_goal_arithmetic (sub : (exp * exp) list) a =
  match a with
  | ArithmeticVar v -> (
      (* if this variable has a substitution do the substitution *)
      match List.Assoc.find sub ~equal:(Ast.equal_exp) (VarExp v) with
        | Some (IntExp i2) -> ArithmeticInt i2
        | Some (VarExp v2) -> ArithmeticVar v2
        | None -> a
        | _ -> raise (FAILED_SUBSTITUTION "Attempted to substitute an ArithmeticExp or a TermExp for a variable in\
                                          an arithmetic expression. If this has occurred, I've implemented\
                                          arithmetic wrong. Oops. ")
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
        match List.Assoc.find sub ~equal:(Ast.equal_exp) g with
        | Some i -> i
        | None -> VarExp v
    )
    | TermExp (s, el) ->
        TermExp (s, List.map ~f:(fun g1 -> sub_lift_goal sub g1) el)
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
    List.map ~f:(fun g1 -> sub_lift_goal sub g1) gl

(*
   sub_lift_goals_cut:
     * takes in:
         sub - a list of substitutions for variables
         gl - a list of (goal, cut) pairs
     * returns the list of goals with the substitutions applied to each goal
*)
let sub_lift_goals_cut sub gl =
  List.map ~f:(fun (g1, c) -> sub_lift_goal sub g1, c) gl
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
        let vars : exp list = uniq (head_vars @ body_vars) in
        (* get fresh variable mappings *)
        let sub = List.map ~f:(fun x -> (x, VarExp (fresh()))) vars in
        (* substitute new names for variables *)
        Clause (sub_lift_goal sub h, sub_lift_goals sub b)
    | Query (b) ->
        (* find uniq vars in query *)
        let body_vars = find_vars b in
        (* get fresh variable mappings *)
        let vars = uniq (body_vars) in
        let sub = List.map ~f:(fun x -> (x, VarExp (fresh()))) vars in
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
let rec occurs (n : string) t =
     match t with
     | VarExp m -> String.equal n m
     | TermExp (_, el) ->
        List.fold_left el ~f:(fun acc v -> (acc || (occurs n v))) ~init:false
     | ArithmeticExp (_, e1, e2) ->(
       match e1, e2 with
       | ArithmeticVar v1, ArithmeticVar v2 -> String.equal n v1 || String.equal n v2
       | ArithmeticVar v1, _ -> String.equal n v1
       | _, ArithmeticVar v2 -> String.equal n v2
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
        if Ast.equal_exp s t
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
                    if ((String.equal tname sname) && List.length targs = List.length sargs)
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
   List.fold_left e
     ~f:(
        fun r2 env ->
        if orig_vars_num > 0
        then
          "====================\n" ^
            (* iterate over original query vars to find their substitution *)
            (List.fold_left
               orig_query_vars
               ~f:(
                 fun r d -> (
                   match d with
                   | VarExp v -> (
                     (* find variable substitution in the solution *)
                       match List.Assoc.find env (VarExp v) ~equal:(Ast.equal_exp) with
                       | Some (VarExp _) -> (v ^ " is free\n") ^ r
                       | Some f -> (v ^ " = " ^ (readable_string_of_exp f) ^ "\n") ^ r
                       | None -> (v ^ " is free\n") ^ r
                     )
                   | _ -> r
                 )
               ) ~init:"" ) ^
              "====================\n"  ^ r2
        else "" ^ r2
      )
     ~init:(if List.length e > 0 (* if e is empty then there were no solutions *)
         then "true\n"
         else "false\n")

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
    let disallowed = ["true"; "is"; "list"; "empty_list"; "equals"; "not_equal"; "less_than";
                     "greater_than"; "less_than_or_eq"; "greater_than_or_eq"; "cut"]
    in
    match dec with
    | Clause (h, _) -> (
        match h with
        | TermExp (name, _) -> if List.exists disallowed ~f:(fun a -> String.equal name a )
            then ( print_string ("Can't reassign '"^name^"' predicate\n"); db)
            else dec::db
        | _ -> dec :: db
    )
    | Query _ -> db


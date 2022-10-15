(* TODO - introduce string constants back in as standalone expressions *)

(* TODO - add other arithmetic expressions i.e. multiply and integer divide *)
type arithmetic_operator = PLUS | MINUS

(* TODO - the system which handles renaming variables isn't going to work for variables which are in arithmetic
expressions, because the types are different. Will need to update that function to handle arithmetics as well.
Also any function that does any substitution *)
type arithmetic_operand =
  | ArithmeticVar of string
  | ArithmeticInt of int

(* Expressions *)
type exp =
    | VarExp of string              (* variables                *)
    | IntExp of int                 (* integers                 *)
    | TermExp of string * exp list  (* functor(arg1, arg2, ...) *)
    | ArithmeticExp of arithmetic_operator * arithmetic_operand * arithmetic_operand
                                    (* arithmetic expressions i.e. 7 + 3 or N - 1
                                    This does not allow for the nesting of arithmetic expressions*)

(* Declarations *)
type dec =
    | Clause of exp * (exp list)  (* Head :- Body. *) (* TODO - this type allows single integers to be the head
                                                      of a rule or a whole query. This should really be limited
                                                         to TermExps.
                                                         For now, we'll leave this as an additional check, rather
                                                         than as part of the type system. Potential to change this
                                                         later, perhaps
                                                      *)
    | Query of (exp list)         (* ?- Body.      *)


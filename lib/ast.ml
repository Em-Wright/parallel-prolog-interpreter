(* TODO - introduce string constants back in as standalone expressions *)

type arithmetic_operator = PLUS | MINUS | MULT | DIV

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


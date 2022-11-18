open! Core

type arithmetic_operator = PLUS | MINUS | MULT | DIV
[@@deriving equal, bin_io]

type arithmetic_operand =
  | ArithmeticVar of string
  | ArithmeticInt of int
[@@deriving equal, bin_io]

(* Expressions *)
type exp =
  | VarExp of string              (* variables                *)
  | IntExp of int                 (* integers                 *)
  | TermExp of string * exp list  (* functor(arg1, arg2, ...) *)
  | ArithmeticExp of arithmetic_operator * arithmetic_operand * arithmetic_operand
  (* arithmetic expressions i.e. 7 + 3 or N - 1
     This does not allow for the nesting of arithmetic expressions*)
[@@deriving equal, bin_io]

(* Declarations *)
module Dec = struct
  type t =
    | Clause of exp * (exp list)  (* Head :- Body. *)
    | Query of (exp list)         (* ?- Body.      *)
  [@@deriving equal, bin_io]
end
type dec = Dec.t
(*   | Clause of exp * (exp list)  (\* Head :- Body. *\) *)
(*   | Query of (exp list)         (\* ?- Body.      *\) *)
(* [@@deriving equal, bin_io] *)

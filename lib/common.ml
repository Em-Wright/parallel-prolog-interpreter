open Ast
open Parser


(* Takes a string s and returns the abstract syntax tree generated by lexing and parsing s *)
let parse s =
    let lexbuf = Lexing.from_string s in
        let ast = clause Lexer.token lexbuf in
            ast

(* Takes a string s and returns Some of an abstract syntax tree or None *)
let try_parse s =
    try Some (parse s) with
    | Error -> None

(* String conversion functions *)
let string_of_token t =
    match t with
    | INT    i -> "INT "      ^ string_of_int i
    | ATOM   a -> "ATOM \""   ^ String.escaped a ^ "\""
    | VAR    v -> "VAR \""    ^ v ^ "\""
    | RULE     -> "RULE"
    | QUERY    -> "QUERY"
    | PERIOD   -> "PERIOD"
    | LPAREN   -> "LPAREN"
    | RPAREN   -> "RPAREN"
    | COMMA    -> "COMMA"
    | EOF      -> "EOF"
    | PLUS     -> "PLUS"
    | MINUS    -> "MINUS"
    | MULT     -> "MULT"
    | DIV      -> "DIV"
    | IS       -> "IS"
    | EQUALS   -> "EQUALS"
    | NOTEQUAL -> "NOTEQUAL"
    | GT       -> "GT"
    | LT       -> "LT"
    | RBRACKET -> "RBRACKET"
    | LBRACKET -> "LBRACKET"
    | PIPE     -> "PIPE"

let string_of_token_list tl =
    "[" ^ (String.concat "; " (List.map string_of_token tl)) ^ "]"

let string_of_arithmetic (op : arithmetic_operator) a1 a2 =
  let op_string =
    match op with
    | PLUS -> "PLUS"
    | MINUS -> "MINUS"
    | MULT     -> "MULT"
    | DIV      -> "DIV"
      in
  let a_to_string a =
    match a with
    | ArithmeticInt i -> "ArithmeticInt " ^ string_of_int i
    | ArithmeticVar v -> "ArithmeticVar \"" ^ v ^ "\""
  in
  "Arithmetic (" ^ op_string ^ ", " ^ (a_to_string a1) ^ ", " ^ (a_to_string a2) ^ ")"

let rec string_of_exp e =
    match e with
    | VarExp v   -> "VarExp \"" ^ v ^ "\""
    | IntExp i   -> "IntExp " ^ string_of_int i
    | TermExp (f, args) ->
        let func = String.escaped f in
            "TermExp (\"" ^ func ^ "\", [" ^
                (String.concat "; " (List.map string_of_exp args)) ^ "])"
    | ArithmeticExp (op, a1, a2) -> string_of_arithmetic op a1 a2


let string_of_exp_list g =
    "[" ^ (String.concat "; " (List.map string_of_exp g)) ^ "]"

let string_of_dec d =
    match d with
    | Clause (e1, g) ->
        "Clause (" ^ (string_of_exp e1) ^ ", " ^
            (string_of_exp_list g) ^ ")"
    | Query g -> "Query (" ^ (string_of_exp_list g) ^ ")"

let string_of_db db =
    "[" ^ (String.concat "; " (List.map string_of_dec db)) ^ "]"


let string_of_subs s =
    "[" ^ (
        String.concat "; " (
            List.map (
                fun (x,y) ->
                    "(" ^ (string_of_exp x) ^ ", " ^ (string_of_exp y) ^ ")"
            )
            s
        )
    ) ^ "]"

let string_of_unify_res s =
    match s with
    | None   -> "None"
    | Some l -> string_of_subs l

(* Convert ConstExp to a readable string *)
let readable_string_of_arithmetic (op : arithmetic_operator) a1 a2 =
  let op_string =
    match op with
    | PLUS -> " + "
    | MINUS -> " - "
    | MULT     -> " * "
    | DIV      -> " / "
  in
  let a_to_string a =
    match a with
    | ArithmeticInt i -> "ArithmeticInt " ^ string_of_int i
    | ArithmeticVar v -> "ArithmeticVar \"" ^ v ^ "\""
  in
   (a_to_string a1) ^ op_string  ^ (a_to_string a2)

(* Convert exp to a readable string *)
let rec readable_string_of_exp e =
    match e with
    | VarExp   v     -> v
    | IntExp   i     -> string_of_int i
    | TermExp (s, l) ->
        s ^ (
            if List.length l > 0
            then "(" ^ (
                String.concat ", " (
                    List.map readable_string_of_exp l
                )
            ) ^ ")"
            else ""
        )
    | ArithmeticExp (op, a1, a2) ->
      readable_string_of_arithmetic op a1 a2


(* Print a db *)
let print_db db =
    print_endline (string_of_db db)

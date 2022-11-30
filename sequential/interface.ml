open Core
open Ast
open Parser
open Util

(* eval_dec takes the existing database, a declaration and an eval_function and
either returns an updated database, if the declaration is a clause, or calls
the evaluation function on the query if the declaration is a query
*)
let eval_dec ~db ~dec ~eval_function : dec list = (
  match dec with
  | Clause (_, _) -> add_dec_to_db (dec, db)
  | Query b -> (
      (* find all uniq VarExps in query *)
      let orig_vars = uniq (find_vars b) in
      (* find num of VarExps in query *)
      let orig_vars_num = List.length orig_vars in
      (* evaluate query *)
      let res = eval_function db b in
      (* print the result *)
      print_string (string_of_res (res) orig_vars orig_vars_num);
      (* reset fresh variable counter *)
      reset ();
      db
    )
)
;;

(* handle_input lexex and parses the input from the file (in lexbuf)
   then calls eval_dec, which decides what to do with this line of input.
*)
let handle_input db lexbuf ~eval_function : dec list = (
  let dec = clause (
      fun lb -> (
          match Lexer.token lb with
          | EOF -> raise Lexer.EndInput
		      | r -> r
		    )
	  ) lexbuf
  in
  eval_dec ~db ~dec ~eval_function
 )
;;

(* main takes reads from the file line by line, accumulating a database and
evaluating queries where needed
*)
let main filename ~eval_function =
  print_endline "\nWelcome to the Prolog Interpreter\n";
  let rec loop db file_lines =
    (
      match file_lines with
      | s::ss -> (
          try (
            print_endline s;
            let lexbuf = Lexing.from_string s in
            let newdb = handle_input db lexbuf ~eval_function in
            loop newdb ss
          ) with
          | Failure f -> ( (* in case of an error *)
              print_endline ("Failure: " ^ f ^ "\n");
              loop db ss
            )
          | Parser.Error -> ( (* failed to parse input *)
              print_endline "\nDoes not parse\n";
              loop db ss
            )
          | Lexer.EndInput -> exit 0 (* EOF *)
          | _ -> ( (* Any other error *)
              print_endline "\nUnrecognized error\n";
              loop db ss
            )
        )
      | [] -> ()
    )
  in
  print_endline ("Opening file " ^ filename ^ "\n");
  let file_lines = In_channel.read_lines filename in
  let () = loop [] file_lines in
  print_endline "\n\nFile contents loaded.\n\n"

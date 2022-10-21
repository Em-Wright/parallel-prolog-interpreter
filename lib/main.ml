(* open Ast *)
(* open Common *)
(* open Lexer *)
open Printf
open Parser
open Evaluator

let handle_input db lexbuf = (
  let dec = clause (
      fun lb -> (
          match Lexer.token lb with
          | EOF -> raise Lexer.EndInput
		      | r -> r
		    )
	  ) lexbuf
  in
  eval_dec (dec, db)
);;

let main () =
  print_endline "\nWelcome to the Prolog Interpreter\n";
  if Array.length Sys.argv > 2 then (
    print_string "Too many arguments.\nExiting...\n";
    flush stdout;
    exit 0;
  );
  let initial_db =
    if Array.length Sys.argv = 2 then (
      printf "Opening file %s\n" Sys.argv.(1);
      let fstream = open_in Sys.argv.(1) in
      let rec loop db = (
        try (
          match In_channel.input_line fstream with
          | Some s -> (
              print_endline s;
            let lexbuf = Lexing.from_string s in
            let newdb = handle_input db lexbuf in
            flush stdout;
            loop newdb
            )
          | None -> db
        ) with
        | Failure s -> ( (* in case of an error *)
            printf "\n Failure: %s \n" s;
            flush stdout;
            loop db
          )
        | Parser.Error -> ( (* failed to parse input *)
            print_endline "\nDoes not parse\n";
            loop db
          )
        | Lexer.EndInput -> exit 0 (* EOF *)
        | _ -> ( (* Any other error *)
            print_endline "\nUnrecognized error\n";
            loop db
          )
        )
      in
      let db = loop [] in
      print_endline "\n\nFile contents loaded.\n\n";
      db
    ) else ( [])
  in
  let rec loop db = (
    try (
      let lexbuf = Lexing.from_channel stdin in
      printf "> ";
      flush stdout;
      let newdb = handle_input db lexbuf in
      loop newdb
    ) with
    | Failure s -> ( (* in case of an error *)
        printf "\n Failure: %s \n" s;
        flush stdout;
        loop db
      )
    | Parser.Error -> ( (* failed to parse input *)
        print_endline "\nDoes not parse\n";
        loop db
      )
    | Lexer.EndInput -> exit 0 (* EOF *)
    | _ -> ( (* Any other error *)
        print_endline "\nUnrecognized error\n";
        loop db
      )
  )
  in loop initial_db

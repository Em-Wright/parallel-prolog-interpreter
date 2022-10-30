(* open Ast *)
(* open Common *)
(* open Lexer *)
open Ast
open Printf
open Parser
open Evaluator

let handle_input db lexbuf ~eval_function = (
  let dec = clause (
      fun lb -> (
          match Lexer.token lb with
          | EOF -> raise Lexer.EndInput
		      | r -> r
		    )
	  ) lexbuf
  in
  match dec with
  | Clause (_, _) -> add_dec_to_db (dec, db)
  | Query b -> (
      (* find all uniq VarExps in query *)
      let orig_vars = uniq (find_vars b) in
      (* find num of VarExps in query *)
      let orig_vars_num = List.length orig_vars in
      (* evaluate query *)
      let res = eval_function db b in
      (* eval_query (b, db, []) in *)
      (* print the result *)
      print_string (string_of_res (res) orig_vars orig_vars_num);
      (* reset fresh variable counter *)
      reset ();
      db
    )
);;

let sequential_eval db b = Evaluator.eval_query (b, db, []);;
let stack_eval db b = Stack_evaluator.eval_query b db;;

(* TODO - make this a command which can take a -parallel or -stack
   flag, and also a -filename flag
*)
let main () =
  let usage_msg = "PLACEHOLDER" in
  let filename = ref "" in
  let parallel = ref false in
  let file_function f = filename := f in
  let speclist = [
    ("-filename", Arg.Set_string filename, "Read prolog file");
    ("-parallel", Arg.Set parallel, "Run this query in parallel")
  ] in
   (
    Arg.parse speclist file_function usage_msg;
    print_endline "\nWelcome to the Prolog Interpreter\n";
    (* if Array.length Sys.argv > 2 then ( *)
    (*   print_string "Too many arguments.\nExiting...\n"; *)
    (*   flush stdout; *)
    (*   exit 0; *)
    (* ); *)
    let eval_function = if !parallel then stack_eval else sequential_eval in
    let initial_db =
      if String.equal !filename "" then []
      else (
        printf "Opening file %s\n" Sys.argv.(1);
        let fstream = open_in Sys.argv.(1) in
        let rec loop db = (
          try (
            match In_channel.input_line fstream with
            | Some s -> (
                print_endline s;
                let lexbuf = Lexing.from_string s in
                let newdb = handle_input db lexbuf ~eval_function in
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
      )
    in
    let rec loop db = (
      try (
        let lexbuf = Lexing.from_channel stdin in
        printf "> ";
        flush stdout;
        let newdb = handle_input db lexbuf ~eval_function in
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
  )
  

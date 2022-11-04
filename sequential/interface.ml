open Core
open Ast
open Async
open Parser
open Util


let eval_dec ~db ~dec ~eval_function : dec list Deferred.t = (
  match dec with
  | Clause (_, _) -> add_dec_to_db (dec, db) |> return
  | Query b -> (
      (* find all uniq VarExps in query *)
      let orig_vars = uniq (find_vars b) in
      (* find num of VarExps in query *)
      let orig_vars_num = List.length orig_vars in
      (* evaluate query *)
      let%bind res = eval_function db b in
      (* print the result *)
      print_string (string_of_res (res) orig_vars orig_vars_num);
      (* reset fresh variable counter *)
      reset ();
      return db
    )
)
        ;;

let handle_input db lexbuf ~eval_function : dec list Deferred.t = (
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

let main filename_opt ~eval_function =
   (
    print_endline "\nWelcome to the Prolog Interpreter\n";
    let%bind initial_db = (
      match filename_opt with
      | None -> return []
      | Some filename -> (
          let rec loop db file_lines =
            (
              match file_lines with
              | s::ss -> (
                  try (
                    print_endline s;
                    let lexbuf = Lexing.from_string s in
                    let%bind newdb = handle_input db lexbuf ~eval_function in
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
              | [] -> return db
            )
          in
          print_endline ("Opening file " ^ filename ^ "\n");
          let file_lines = In_channel.read_lines filename in
          let%bind db = loop [] file_lines in
          print_endline "\n\nFile contents loaded.\n\n";
          return db
        ))
    in
    let rec loop db = (
      try (
        let lexbuf = Lexing.from_channel In_channel.stdin in
        print_string "> ";
        let%bind newdb = handle_input db lexbuf ~eval_function in
        loop newdb
      ) with
      | Failure s -> ( (* in case of an error *)
          print_endline ("\nFailure: " ^ s ^"\n" );
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
  

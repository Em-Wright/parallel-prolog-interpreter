open! Core

let () =
    print_endline "\nWelcome to the Prolog Interpreter\n";
    Parallel_prolog_interpreter.Start_app.start_app Parallel_prolog_interpreter.Worker.command

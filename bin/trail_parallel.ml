open! Core

let () =
    print_endline "\nWelcome to the Prolog Interpreter\n";
    Parallel_trail_prolog_interpreter.Start_app.start_app Parallel_trail_prolog_interpreter.Trail_worker.command

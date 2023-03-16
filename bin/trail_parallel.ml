open! Core

let () =
    print_endline "\nWelcome to the Prolog Interpreter\n";
    Trail_parallel.Start_app.start_app Trail_parallel.Trail_worker.command

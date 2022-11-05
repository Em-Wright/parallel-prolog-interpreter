let command = Core.Command.group ~summary:"A prolog interpreter written in OCaml"
    ["sequential", Evaluator.command; "parallel", Worker.command; "sequential-stack", Stack_evaluator.command]

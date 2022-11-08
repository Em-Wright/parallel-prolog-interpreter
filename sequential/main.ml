let command = Core.Command.group ~summary:"A prolog interpreter written in OCaml"
    ["sequential", Evaluator.command; "stack", Stack_evaluator.command ]

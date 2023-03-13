let command = Core.Command.group ~summary:"A prolog interpreter written in OCaml using a trail stack"
    ["trail", Trail_evaluator.command
    ; "trail-stack", Trail_stack_evaluator.command]

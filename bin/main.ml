(* TODO - figure out why it's only using the parallel command, not the stack and sequential ones *)

(* TODO - this only compiles if we import rpc_parallel in the dune file. Presumably rpc_parallel is importing
something else which we're then using??? *)
let () = Command_unix.run Prolog_interpreter.Main.command

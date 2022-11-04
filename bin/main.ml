open Sequential_interpreter.Main

(* TODO - use the Rpc_parallel_unauthenticated once it gets fixed so that I can actually use it *)

let backend_and_settings = Rpc_parallel.Backend_and_settings.T ((module Backend), ())
let () = Rpc_parallel.start_app
           backend_and_settings
           command

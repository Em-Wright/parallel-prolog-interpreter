open! Core
open! Async

(* let backend = (module Backend : Rpc_parallel.Backend) *)
let backend_and_settings = Rpc_parallel.Backend_and_settings.T ((module Backend), ())

let start_app
      ?rpc_max_message_size
      ?rpc_heartbeat_config
      ?when_parsing_succeeds
      command
  =
  Rpc_parallel.start_app
    ?rpc_max_message_size
    ?rpc_heartbeat_config
    ?when_parsing_succeeds
    backend_and_settings
    command
;;

module For_testing = struct
  let initialize = Rpc_parallel.For_testing.initialize backend_and_settings
end

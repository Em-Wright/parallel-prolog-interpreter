(** See lib/rpc_parallel/src/parallel_intf.ml for documentation. *)
open Core

open Async

(** See lib/rpc_parallel/src/parallel_intf.ml for documentation. *)
val start_app
  :  ?rpc_max_message_size:int
  -> ?rpc_heartbeat_config:Rpc.Connection.Heartbeat_config.t
  -> ?when_parsing_succeeds:(unit -> unit)
  -> Command.t
  -> unit

module For_testing : sig
  (** See lib/rpc_parallel/src/parallel_intf.ml for documentation. *)
  val initialize : Source_code_position.t -> unit
end

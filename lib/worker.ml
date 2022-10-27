open! Core
open! Async
open! Rpc_parallel
module Worker = struct
  module T = struct
    (* TODO - the init_arg needs to give the rules (with any subsitutions needed to
       be able to treat the problem as isolated already done), the query to be
       solved, potentially the `location' of the node it's starting the search from,
       for later aggregation of solutions.

       Worker_state.t itself will need to hold all of this information, plus a stack
       of work to be done (from which work to be given to others can be drawn), plus
       any solutions generated so far.
    *)
    module Worker_state = struct
      type init_arg = unit [@@deriving bin_io]
      type t = unit
    end

    module Connection_state = struct
      type init_arg = unit [@@deriving bin_io]
      type t = unit
    end

    (* TODO - will need to add functions for updating the worker with new work when
       it runs out. This will be pretty much the same as the spawn function in terms of
       the information it needs to be passed. For now, we're having a sequential interpreter
       in one worker, so we don't need to implement this function immediately.
    *)
    (* TODO - need the worker to be able to inform the main process when it's finished
       working. Not sure if this is gonna have to be a system of polling, where the main
       process periodically checks if the work is done, or if the worker can interrupt
       the main process.
    *)
    type 'worker functions = {placeholder : ('worker, int, int) Rpc_parallel.Function.t}

    module Functions
        (C : Rpc_parallel.Creator
         with type worker_state := Worker_state.t
          and type connection_state := Connection_state.t) =
    struct
      let placeholder_impl ~worker_state:() ~conn_state:() arg =
        return arg
      ;;

      let placeholder =
        C.create_rpc
          ~f:placeholder_impl
          ~bin_input:(Int.bin_t)
          ~bin_output:(Int.bin_t)
          ()

      let functions = {placeholder}
      let init_worker_state () = Deferred.unit
      let init_connection_state ~connection:_ ~worker_state:_ = return
    end

  end

  include Rpc_parallel.Make (T)
end

type t = Worker.t

let spawn () = Worker.serve ()

let placeholder t =
  let%bind conn = 
    Worker.Connection.client_exn t ()
  in
  Worker.Connection.run_exn conn  ~f:(Worker.functions.placeholder) ~arg:7

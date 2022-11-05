open! Core
open! Async
open Ast

module Results : sig
  type t = (exp * exp) list list
end

type t

(* val spawn : unit -> t Deferred.t *)

val run : exp list -> dec list -> (exp * exp) list list Deferred.t

val command : Async.Command.t

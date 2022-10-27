open! Core
open! Async

type t

val spawn : unit -> t Deferred.t

val placeholder : t -> int Deferred.t

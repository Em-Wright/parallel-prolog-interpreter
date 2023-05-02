

open Core
module Ast = Prolog_interpreter.Ast

let (fresh, reset, update) =
  let nxt = ref 0 in
  let f () = (nxt := !nxt + 1; !nxt) in
  let r () = nxt := 0 in
  let u n = nxt := Int.max !nxt n in
  (f, r, u)

module Var = struct
  (* This 'a is used so that Var.t can reference Exp.t *)
  type 'a t = {name : string ; mutable instance : 'a ref option}
  [@@deriving fields]

  type 'b serialisable = {name : string; instance : 'b option}
  [@@deriving bin_io, fields]

  let create () : 'a t =
    {name = fresh () |> string_of_int; instance = None}

  let create_named name : 'a t =
    {name ; instance = None}

  let name t = t.name
  let reset (t : 'a t) = t.instance <- None
  let set_instance (t : 'a t) p = t.instance <- Some p

  let has_instance (t : 'a t) = Option.is_some t.instance

  let get_instance (t : 'a t) = t.instance

  let to_string ({name; instance} : 'a t) (f : 'a -> string) =
    match instance with
    | None -> "Var_" ^ name
    | Some x -> (f !x)

  let get_all_var_names ({name;instance} : 'b serialisable) ( f : 'b -> string list -> string list) acc =
    match instance with
    | None -> name::acc
    | Some e -> f e acc

  let serialisable_to_string ({name; instance} : 'b serialisable) (f : 'b -> string) =
    match instance with
    | None -> "Var_" ^ name
    | Some x -> "Var" ^ name ^ " -> "^ (f x)

  let resolve_name ({name; instance} : 'a t) (f : 'a -> string) =
    match instance with
    | None -> name
    | Some x -> f !x

  let equal (v1 : 'a t) (v2 : 'a t) = String.equal v1.name v2.name

  let deep_copy (v : 'a t) copy_f var_translation : 'a t =
    let instance =
      match v.instance with
      | None -> None
      | Some e -> copy_f e |> ref |> Some
    in
    let new_v : 'a t = {name = fresh () |> string_of_int; instance} in
    Hashtbl.set var_translation ~key:v.name ~data:(ref new_v);
    new_v

  let serialise (t : 'a t) (resolve_instance : 'a -> 'a) (serialise_f : 'a -> 'b) : 'b serialisable =
    match t.instance with
    | None -> {name=t.name; instance=None}
    | Some e -> {name=t.name; instance=( resolve_instance !e |> serialise_f |> Some)}

  let deserialise ({name; instance} : 'b serialisable)
      (f : 'b -> 'a t String.Table.t -> 'a) (tbl : 'a t String.Table.t) : 'a t=
    match instance with
    | None -> Hashtbl.find_or_add tbl name ~default:(fun () -> {name; instance=None})
    | Some e -> let inst = f e tbl in {name; instance=Some (ref inst)}

  let reref_vars (v : 'a t ref) (tbl : 'a t ref String.Table.t) reref_f (var_wrap_f : 'a t ref -> 'c) deep_copy_f : 'c =
    match !v.instance with
    | None ->
      (
        match Hashtbl.find tbl !v.name with
        | None -> deep_copy !v deep_copy_f tbl |> ref |> var_wrap_f
        | Some v2 -> var_wrap_f v2
      )
    | Some e -> reref_f !e tbl

end

module Arithmetic_operand = struct
  type 'b serialisable =
    | ArithmeticVarS of 'b Var.serialisable
    | ArithmeticIntS of int
  [@@deriving bin_io]

  type 'a t =
    | ArithmeticVar of 'a Var.t ref
    | ArithmeticInt of int

  let serialise (t : 'a t) serialise_f : 'b serialisable =
    match t with
    | ArithmeticInt i -> ArithmeticIntS i
    | ArithmeticVar v -> Var.serialise !v (fun a -> a) serialise_f |> ArithmeticVarS

  let deserialise s (var_mapping : 'a Var.t String.Table.t) : 'a t =
    match s with
    | ArithmeticIntS i -> ArithmeticInt i
    | ArithmeticVarS v ->
      Hashtbl.find_or_add var_mapping v.name
                           ~default:(fun () -> Var.create_named v.name)
                         |> ref |> ArithmeticVar

  let to_string t (f : 'a -> string) =
    match t with
    | ArithmeticVar v -> Var.to_string !v f
    | ArithmeticInt i -> Int.to_string i

  let serialisable_to_string t to_string_f =
    match t with
    | ArithmeticVarS v -> (Var.serialisable_to_string v to_string_f)
    | ArithmeticIntS i -> Int.to_string i

  let deep_copy (t : 'a t) copy_f var_translation =
    match t with
    | ArithmeticInt _ -> t
    | ArithmeticVar v -> ArithmeticVar (Var.deep_copy !v copy_f var_translation |> ref)

  let reref_vars (t : 'a t) copy_f reref_f tbl : 'a t =
    match t with
    | ArithmeticInt _ -> t
    | ArithmeticVar v -> (
        Var.reref_vars v tbl reref_f (fun v ->  ArithmeticVar v) copy_f
      )

  let get_all_var_names (a : 'b serialisable)
      (f : 'b -> string list -> string list) (acc : string list) : string list =
    match a with
    | ArithmeticVarS v -> Var.get_all_var_names v f acc
    | ArithmeticIntS _ -> acc

end




module Exp = struct
    type t =
      | VarExp of t Var.t ref
      | IntExp of int
      | TermExp of string * t ref list
      | ArithmeticExp of Ast.arithmetic_operator * t Arithmetic_operand.t * t Arithmetic_operand.t

    type serialisable =
      | VarExpS of serialisable Var.serialisable
      | IntExpS of int
      | TermExpS of string * (serialisable list)
      | ArithmeticExpS of Ast.arithmetic_operator
                          * serialisable Arithmetic_operand.serialisable
                          * serialisable Arithmetic_operand.serialisable
    [@@deriving bin_io]

    let rec resolve_instance (e : t) : t =
      match e with
      | VarExp v -> (
          match !v.instance with
          | Some e -> (
              match !e with
              | VarExp _ -> resolve_instance !e
              | _ -> !e
            )
          | None -> e
        )
      | _ -> e

    let operator_to_string (t : Ast.arithmetic_operator) =
      match t with
      | PLUS -> " + "
      | MINUS -> " - "
      | MULT -> " * "
      | DIV -> " / "

    let rec to_string (t : t) =
      let readable_string_of_list list_exp =
        let rec inner_string list_exp =
          match list_exp with
          | TermExp ("empty_list", []) -> ""
          | TermExp ("list", [element; rest]) ->(
            let resolved = resolve_instance !rest in
            match resolved with
            | TermExp ("empty_list", _) -> to_string !element
            | TermExp ("list", _) ->
              let rest_of_string = inner_string resolved in
              (to_string !element) ^ ", " ^ rest_of_string
            | _ -> ""
          )
          | VarExp v -> Var.to_string !v to_string
          | _ -> "This is not a list, but has been given to the readable_string_of_list function"
        in
        "[" ^ (inner_string list_exp) ^ "]"
      in
      match t with
      | VarExp v -> (Var.to_string !v to_string)
      | IntExp i -> Int.to_string i
      | TermExp (name, args) ->
        ( match name with
          | "list" | "empty_list" -> readable_string_of_list t
          | _ -> if List.length args > 0 then
              let arg_string = List.fold args ~init:"" ~f:(fun acc arg -> acc ^ (to_string !arg) ^ ", ") in
              name ^ "(" ^ arg_string ^ ")"
            else
              name
        )
      | ArithmeticExp (operator, op1, op2 ) ->
        (Arithmetic_operand.to_string op1 to_string)
        ^ (operator_to_string operator)
        ^ (Arithmetic_operand.to_string op2 to_string)

    let rec resolve_var_name (t : t) =
      match t with
      | VarExp v -> Var.resolve_name !v resolve_var_name
      | _ -> to_string t

    let rec serialisable_to_string (t : serialisable) =
      match t with
      | VarExpS v -> (Var.serialisable_to_string v serialisable_to_string)
      | IntExpS i -> Int.to_string i
      | TermExpS (name, args) ->
        let arg_string = List.fold args ~init:"" ~f:(fun acc arg -> acc ^ (serialisable_to_string arg) ^ ", ") in
        name ^ "(" ^ arg_string ^ ")"
      | ArithmeticExpS (operator, op1, op2 ) ->
        (Arithmetic_operand.serialisable_to_string op1 serialisable_to_string)
        ^ (operator_to_string operator)
        ^ (Arithmetic_operand.serialisable_to_string op2 serialisable_to_string)


    let rec serialise (t : t) : serialisable =
      match t with
      | VarExp v -> Var.serialise !v resolve_instance serialise |> VarExpS
      | IntExp i -> IntExpS i
      | TermExp (name, args) -> let args = List.map args ~f:(fun a -> serialise !a) in
        TermExpS (name, args)
      | ArithmeticExp (op, a1, a2) -> ArithmeticExpS (op,
                                                     Arithmetic_operand.serialise a1 serialise,
                                                     Arithmetic_operand.serialise a2 serialise
                                                    )

    let rec deserialise (s : serialisable) var_mapping : t =
      match s with
      | VarExpS v ->
        let rec resolve_to_last_var (v : serialisable Var.serialisable) =
          match v.instance with
          | Some e ->
            (match e with
            | VarExpS v2 -> resolve_to_last_var v2
            | _ -> v
            )
          | None -> v
        in
        Var.deserialise (resolve_to_last_var v) deserialise var_mapping |> ref |> VarExp
      | IntExpS i -> IntExp i
      | TermExpS (n, args) -> TermExp (n, List.map args ~f:(fun e -> deserialise e var_mapping |> ref))
      | ArithmeticExpS (op, a1, a2) -> ArithmeticExp (op,
                                                      Arithmetic_operand.deserialise a1 var_mapping,
                                                      Arithmetic_operand.deserialise a2 var_mapping
                                                     )

    let rec get_all_var_names (e : serialisable) acc =
      match e with
      | VarExpS v -> Var.get_all_var_names v get_all_var_names acc
      | IntExpS _ -> acc
      | TermExpS (_, args) -> let acc2 = List.fold args ~init:[]
                                  ~f:(fun acc2 arg -> get_all_var_names arg acc2)
        in
        acc2@acc
      | ArithmeticExpS (_, op1, op2) ->
        let acc1 = Arithmetic_operand.get_all_var_names op1 get_all_var_names [] in
        let acc2 = Arithmetic_operand.get_all_var_names op2 get_all_var_names [] in
        acc1@acc2@acc

    let rec deep_copy (e : t ref) var_translation : t =
      match !e with
      | VarExp v -> Var.deep_copy !v (fun e -> deep_copy e var_translation) var_translation |> ref |> VarExp
      | IntExp _ -> !e
      | TermExp (n, args) ->
        let new_args = List.map args ~f:(fun arg -> deep_copy arg var_translation |> ref) in
        TermExp (n, new_args)
      | ArithmeticExp (operator, op1, op2) ->
        let op1_v2 = Arithmetic_operand.deep_copy op1
            (fun e -> deep_copy e var_translation) var_translation in
        let op2_v2 = Arithmetic_operand.deep_copy op2
            (fun e -> deep_copy e var_translation) var_translation in
        ArithmeticExp (operator, op1_v2, op2_v2)

    let rec shallow_copy (e : t ref) : t ref =
      match !e with
      | IntExp _ -> e
      | VarExp v -> (if not (Var.has_instance !v) then
                       (Var.set_instance !v (ref (VarExp (ref (Var.create ())))));
                     Var.get_instance !v |> Option.value_exn )
      | TermExp (n, args) ->
        let new_args = List.map args ~f:(fun arg -> shallow_copy arg ) in
        ( TermExp (n, new_args) : t) |> ref
      | ArithmeticExp (operator, op1, op2) ->
        let shallow_copy_arith t =
          match t with
          | Arithmetic_operand.ArithmeticInt _ -> t
          | ArithmeticVar v ->
            (
              if not (Var.has_instance !v) then
                (Var.set_instance !v (ref (VarExp (ref (Var.create ())))));
              match !(Var.get_instance !v |> Option.value_exn) with
              | IntExp i -> ArithmeticInt i
              | VarExp v -> ArithmeticVar v
              | _ -> t
            )
        in
        (ArithmeticExp (operator, shallow_copy_arith op1, shallow_copy_arith op2) : t) |> ref


    let rec reref_vars (e : t) tbl =
      match e with
      | VarExp v -> (* need to first check if v has an instance, and if so, apply the replacement to that *)
        Var.reref_vars v tbl reref_vars (fun v -> (VarExp v : t)) (fun e -> deep_copy e tbl)
      | IntExp _ -> e
      | TermExp (n, args) -> let new_args = List.map args ~f:(fun arg -> reref_vars !arg tbl |> ref) in
        TermExp (n, new_args)
      | ArithmeticExp (operator, op1, op2) ->
        let reref_arith_vars e tbl =
          match reref_vars e tbl with
          | VarExp v -> Arithmetic_operand.ArithmeticVar v
          | IntExp i -> ArithmeticInt i
          | _ -> ArithmeticInt 0
        in
        let op1_v2 = Arithmetic_operand.reref_vars op1 (fun e -> deep_copy e tbl) reref_arith_vars tbl in
        let op2_v2 = Arithmetic_operand.reref_vars op2 (fun e -> deep_copy e tbl) reref_arith_vars tbl in
        ArithmeticExp (operator, op1_v2, op2_v2)

end

module Trail = struct
  type t = Exp.t Var.t ref Stack.t

  let undo t = Stack.iter t ~f:(fun elt -> Var.reset !elt)

  let push = Stack.push

  let create () : t = Stack.create ()

end

module Dec = struct
  type t =
    | Clause of Exp.t * (Exp.t list)  (* Head :- Body. *)
    | Query of (Exp.t list)         (* ?- Body.      *)

  type serialisable =
    | ClauseS of Exp.serialisable * (Exp.serialisable list)  (* Head :- Body. *)
    | QueryS of (Exp.serialisable list)         (* ?- Body.      *)
   [@@deriving bin_io]

  let serialise (t : t) : serialisable =
    match t with
    | Clause (h, tl) -> ClauseS (Exp.serialise h, List.map tl ~f:Exp.serialise)
    | Query tl -> QueryS (List.map tl ~f:Exp.serialise)

  let deserialise (s : serialisable) var_mapping : t =
    match s with
    | ClauseS (h, tl) -> Clause (Exp.deserialise h var_mapping, List.map tl ~f:(fun e -> Exp.deserialise e var_mapping) )
    | QueryS tl -> Query (List.map tl ~f:(fun e -> Exp.deserialise e var_mapping) )

end

module Clause = struct
  type t = Exp.t ref * Exp.t ref list

  type serialisable = Exp.serialisable * Exp.serialisable list [@@deriving bin_io]

  let serialise (a,b) = (Exp.serialise !a, List.map b ~f:(fun e -> Exp.serialise !e))

  let deserialise ((a,b) : serialisable) var_mapping : t =
    (
      Exp.deserialise a var_mapping |> ref,
      List.map b ~f:(fun e -> Exp.deserialise e var_mapping |> ref)
    )

  let deep_copy (head, body) : t =
    let head2 = Exp.deep_copy head (String.Table.create ()) |> ref in
    let body2 = List.map body ~f:(fun elt -> Exp.deep_copy elt (String.Table.create ()) |> ref) in
    (head2, body2)

  let copy (head, body) : t =
    let head2 = Exp.shallow_copy head in
    let body2 = List.map body ~f:(fun elt -> Exp.shallow_copy elt) in
    (head2, body2)

  let to_string (head, body) =
    (Exp.to_string !head)^" :- "^(List.to_string ~f:(fun g -> Exp.to_string !g) body )
end

let rec get_furthest_instance (v : Exp.t Var.t ref) =
  match !v.instance with
  | None -> Exp.VarExp v
  | Some e -> (
      match !e with
      | VarExp v2 -> get_furthest_instance v2
      | owt_else -> owt_else
    )

let arithmetic_occurs t1_ref a =
  match a with
  | Arithmetic_operand.ArithmeticVar v ->
    ( match get_furthest_instance v with
      | VarExp v -> Var.equal !t1_ref !v
      | _ -> false
    )
  | ArithmeticInt _ -> false

let rec occurs (t1_ref : Exp.t Var.t ref) (t2_ref : Exp.t ref) =
  match !t2_ref with
  | VarExp v ->
    ( match get_furthest_instance v with
      | VarExp v -> Var.equal !t1_ref !v
      | e -> occurs t1_ref (ref e)
    )
  | TermExp (_, el) -> List.fold el ~init:false ~f:(fun acc e -> acc || (occurs t1_ref e))
  | IntExp _ -> false
  | ArithmeticExp (_, l, r) -> (arithmetic_occurs t1_ref l) || (arithmetic_occurs t1_ref r)



let rec unify (t1_ref : Exp.t ref) (t2_ref : Exp.t ref) (trail : Trail.t) =
  match (!t1_ref) with
  | VarExp v ->
    (
      match Var.get_instance !v with
      | None -> if (occurs v t2_ref) then false
        else (Trail.push trail v; Var.set_instance !v t2_ref; true)
      | Some e -> unify e t2_ref trail
    )
  | TermExp (sname, sargs) ->
    (
      match !t2_ref with
      | VarExp _ -> unify t2_ref t1_ref trail
      | TermExp (tname, targs) ->
        if ((String.equal tname sname) && List.length targs = List.length sargs)
        then (
          List.fold2_exn sargs targs ~init:true ~f:(fun acc s t ->
              (unify s t trail) && acc
            )
        )
        else false
      | _ -> false
    )
  | IntExp i -> (
      match !t2_ref with
      | IntExp j -> i = j
      | VarExp _ -> unify t2_ref t1_ref trail
      | _ -> false
    )
  | _ -> (
      match !t2_ref with
      | VarExp _ -> unify t2_ref t1_ref trail
      | _ -> false
    )


let realise_solution var_mapping =
  Hashtbl.fold var_mapping
    ~init:[]
    ~f:(fun ~key ~data acc -> (key, Var.to_string data Exp.to_string)::acc)

let perform_arithmetic (op : Ast.arithmetic_operator) i1 i2 =
  match op with
  | PLUS -> i1 + i2
  | MINUS -> i1 - i2
  | MULT -> i1 * i2
  | DIV -> i1 / i2

let resolve_arith (a : Exp.t Arithmetic_operand.t) =
  match a with
  | ArithmeticInt _ -> a
  | ArithmeticVar v ->
    let rec resolve_inner (instance : Exp.t ref option) : Exp.t Arithmetic_operand.t =
      match instance with
      | Some e -> ( match !e with
          | IntExp i -> ArithmeticInt i
          | VarExp v -> resolve_inner (Var.get_instance !v)
          | TermExp _ -> a
          | ArithmeticExp _ -> a
        )
      | None -> a
    in
    resolve_inner (Var.get_instance !v)

let rec resolve (e : Exp.t) =
  match e with
  | IntExp _ -> e
  | VarExp v -> (match Var.get_instance !v with
      | None -> e
      | Some v -> resolve !v
    )
  | _ -> e


let arithmetic_convert (t : Ast.arithmetic_operand) (var_mapping : Exp.t Var.t String.Table.t) : Exp.t Arithmetic_operand.t =
  match t with
  | ArithmeticVar v -> (
      match Hashtbl.find var_mapping v with
      | Some v2 -> ArithmeticVar (ref v2)
      | None -> let new_var : Exp.t Var.t = Var.create () in
        Hashtbl.add_exn var_mapping ~key:v ~data:new_var;
        ArithmeticVar (ref new_var)
    )
  | ArithmeticInt i -> ArithmeticInt i

let rec convert (t : Ast.exp) (var_mapping : Exp.t Var.t String.Table.t) : Exp.t =
  match t with
  | VarExp v -> (
      match Hashtbl.find var_mapping v with
      | Some v2 -> VarExp (ref v2)
      | None -> let new_var = Var.create () in
        Hashtbl.add_exn var_mapping ~key:v ~data:new_var;
        VarExp (ref new_var)
    )
  | IntExp i -> IntExp i
  | TermExp (name, args) ->
    let new_args = List.map args ~f:(fun arg -> convert arg var_mapping |> ref) in
    TermExp (name, new_args)
  | ArithmeticExp (op, op1, op2) ->
    let new_op1 = arithmetic_convert op1 var_mapping in let new_op2 = arithmetic_convert op2 var_mapping in
    ArithmeticExp (op, new_op1, new_op2)

let arithmetic_convert_serialisable (t : Ast.arithmetic_operand)
    (var_mapping : Exp.serialisable Var.serialisable String.Table.t)
  : Exp.serialisable Arithmetic_operand.serialisable =
  match t with
  | ArithmeticVar v -> String.Table.set var_mapping ~key:v ~data:({name=v; instance=None});
    ArithmeticVarS {name=v; instance=None}
  | ArithmeticInt i -> ArithmeticIntS i

let rec convert_serialisable (t : Ast.exp) (var_mapping : Exp.serialisable Var.serialisable String.Table.t)
  : Exp.serialisable =
  match t with
  | VarExp v -> String.Table.set var_mapping ~key:v ~data:({name=v; instance=None});
    VarExpS {name=v; instance=None}
  | IntExp i -> IntExpS i
  | TermExp (name, args) ->
    let new_args = List.map args ~f:(fun arg -> convert_serialisable arg var_mapping ) in
    TermExpS (name, new_args)
  | ArithmeticExp (op, op1, op2) ->
    let new_op1 = arithmetic_convert_serialisable op1 var_mapping in
    let new_op2 = arithmetic_convert_serialisable op2 var_mapping in
    ArithmeticExpS (op, new_op1, new_op2)

module Job = struct
  type t = {
    goals : (Exp.t ref * int) list;
    var_mapping : Exp.t Var.t String.Table.t;
    path : (int*int) list
  } [@@deriving fields]

  type serialisable = {
    goals : (Exp.serialisable * int) list;
    var_mapping : Exp.serialisable Var.serialisable String.Table.t;
    path : (int*int) list
  } [@@deriving bin_io]

  let serialise ({goals;var_mapping;path} : t) : serialisable =
    let goals = List.map goals ~f:(fun (g, d) -> Exp.serialise !g, d) in
    let var_mapping = Hashtbl.map var_mapping ~f:(fun v ->
        Var.serialise v Exp.resolve_instance Exp.serialise
      ) in
    {goals; var_mapping; path}


  let deserialise ({goals; var_mapping; path} : serialisable) : t =
    let all_var_names = List.fold goals ~init:[] ~f:(fun acc (g,_) ->
        Exp.get_all_var_names g acc
      ) |> String.Set.of_list
    in
    let temp_var_mapping =
      match String.Table.create_mapped (String.Set.to_list all_var_names) ~get_key:Fn.id
        ~get_data:(fun r -> Var.create_named r) with
      | `Ok tbl -> tbl
      | `Duplicate_keys _ -> raise_s (Sexp.of_string "Duplicate keys when deserialising")
    in
    let var_mapping = Hashtbl.map var_mapping ~f:(fun v_serialised ->
        Var.deserialise v_serialised Exp.deserialise temp_var_mapping
      )
    in
    let goals = List.map goals ~f:(fun (goal, d) ->
        (Exp.deserialise goal temp_var_mapping |> ref , d)
      )
    in
    {goals; var_mapping; path}

  let deep_copy ({goals; var_mapping; path} : t) : t =
    let var_translation = String.Table.create () in
    let new_var_mapping = String.Table.map var_mapping ~f:(fun v ->
        Var.deep_copy v (fun e -> Exp.deep_copy e var_translation) var_translation
      )
    in
    let new_goals = List.map goals ~f:(fun (e,d) -> Exp.reref_vars !e var_translation |> ref, d) in
    {goals=new_goals; var_mapping=new_var_mapping; path}
end

module Job_and_nxt = struct
  type t = Job.serialisable * int [@@deriving bin_io]
end

module Job_and_bool = struct
  type t = Job.serialisable * int * bool [@@deriving bin_io]
end

module Results = struct
  type t = ((string * string) list * (int*int) list) list [@@deriving bin_io]

  let reverse_path_order t : t =
    List.map t ~f:( fun (env, path) -> (env, List.rev path))
end

module Worker_to_toplevel = struct
  type t =
    Results_and_cuts of Results.t * ((int*int) list list)
    | Job of Job_and_nxt.t
  [@@deriving bin_io]
end

module Toplevel_to_worker = struct
  type t =
    Work_request
    | Cuts of (int*int) list list
  [@@deriving bin_io]
end

let remove_due_to_cut path cut_path =
  let rec loop p cp =
    match p, cp with
    | (x,dx)::_, (y, dy)::[] -> if x > y && dx=dy then true else false
    | (x,dx)::xs, (y, dy)::ys -> if x = y && dx=dy then loop xs ys else false
    | _,_ -> false
  in
  loop path (List.rev cut_path)

let rec truncate path depth =
  match path with
  | (_, d)::p -> if d > depth then truncate p depth else  path
  | [] -> []

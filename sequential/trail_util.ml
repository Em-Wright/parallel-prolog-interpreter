open Core

let (fresh, reset, update) =
  let nxt = ref 0 in
  let f () = (nxt := !nxt + 1; !nxt) in
  let r () = nxt := 0 in
  let u n = nxt := Int.max !nxt n in
  (f, r, u)

module Var = struct
  (* This 'a is used so that Var.t can reference Exp.t *)
  type 'a t = {name : string ; mutable instance : 'a ref option}
  [@@deriving bin_io]

  let create () =
    {name = fresh () |> string_of_int; instance = None}

  let name t = t.name
  let reset t = t.instance <- None
  let set_instance t p = t.instance <- Some p

  let has_instance t = Option.is_some t.instance

  let get_instance t = t.instance

  let to_string {name; instance} (f : 'a -> string) =
    match instance with
    | None -> "Var" ^ name
    | Some x -> "Var" ^ name ^ " -> "^ (f !x)

  let equal v1 v2 = String.equal v1.name v2.name

  let deep_copy v copy_f var_translation =
    let instance =
      match v.instance with
      | None -> None
      | Some e -> copy_f e |> ref |> Some
    in
    let new_v = {name = fresh () |> string_of_int; instance} in
    Hashtbl.set var_translation ~key:v.name ~data:(ref new_v);
    new_v

  let reref_vars v tbl reref_f (var_wrap_f : 'a t ref -> 'b) deep_copy_f : 'b =
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
  type 'a t =
    | ArithmeticVar of 'a Var.t ref
    | ArithmeticInt of int
  [@@deriving bin_io]

  let to_string t (f : 'a -> string) =
    match t with
    | ArithmeticVar v -> Var.to_string !v f
    | ArithmeticInt i -> Int.to_string i

  let deep_copy t copy_f var_translation =
    match t with
    | ArithmeticInt _ -> t
    | ArithmeticVar v -> ArithmeticVar (Var.deep_copy !v copy_f var_translation |> ref)


  let reref_vars t copy_f reref_f tbl =
    match t with
    | ArithmeticInt _ -> t
    | ArithmeticVar v -> (
        Var.reref_vars v tbl reref_f (fun v ->  ArithmeticVar v) copy_f
      )
end




module Exp = struct
    type t =
      | VarExp of t Var.t ref
      | IntExp of int
      | TermExp of string * t ref list
      | ArithmeticExp of Ast.arithmetic_operator * t Arithmetic_operand.t * t Arithmetic_operand.t
      [@@deriving bin_io]

    let operator_to_string (t : Ast.arithmetic_operator) =
      match t with
      | PLUS -> " + "
      | MINUS -> " - "
      | MULT -> " * "
      | DIV -> " / "

    let rec to_string t =
      match t with
      | VarExp v -> Var.to_string !v to_string
      | IntExp i -> Int.to_string i
      | TermExp (name, args) ->
        let arg_string = List.fold args ~init:"" ~f:(fun acc arg -> acc ^ (to_string !arg) ^ ", ") in
        name ^ "(" ^ arg_string ^ ")"
      | ArithmeticExp (operator, op1, op2 ) ->
        (Arithmetic_operand.to_string op1 to_string)
        ^ (operator_to_string operator)
        ^ (Arithmetic_operand.to_string op2 to_string)

    let rec deep_copy e var_translation =
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

    let rec shallow_copy e =
      match !e with
      | VarExp v -> (if not (Var.has_instance !v) then
                       (Var.set_instance !v (ref (VarExp (ref (Var.create ())))));
                     Var.get_instance !v |> Option.value_exn )
      | IntExp _ -> e
      | TermExp (n, args) ->
        let new_args = List.map args ~f:(fun arg -> shallow_copy arg ) in
        TermExp (n, new_args) |> ref
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
        ArithmeticExp (operator, shallow_copy_arith op1, shallow_copy_arith op2) |> ref


    let rec reref_vars e tbl =
      match e with
      | VarExp v -> (* need to first check if v has an instance, and if so, apply the replacement to that *)
        Var.reref_vars v tbl reref_vars (fun v -> VarExp v) (fun e -> deep_copy e tbl)
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

  [@@deriving bin_io]
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


module Clause = struct
  type t = Exp.t ref * Exp.t ref list [@@deriving bin_io]

  (* type for_sending = Exp.for_sending * Exp.for_sending list [@@deriving bin_io] *)

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

let rec resolve_to_var (e : Exp.t) =
  match e with
  | IntExp _ -> None
  | VarExp v -> (match Var.get_instance !v with
      | None -> Some v
      | Some v -> resolve_to_var !v
    )
  | _ -> None

module Job = struct
  type t = {
    goals : Exp.t ref list;
    var_mapping : Exp.t Var.t String.Table.t
  }

  let deep_copy {goals; var_mapping} =
    let var_translation = String.Table.create () in
    let new_var_mapping = String.Table.map var_mapping ~f:(fun v ->
        Var.deep_copy v (fun e -> Exp.deep_copy e var_translation) var_translation
      )
    in
    let new_goals = List.map goals ~f:(fun e -> Exp.reref_vars !e var_translation |> ref) in
    {goals=new_goals; var_mapping=new_var_mapping}
end

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


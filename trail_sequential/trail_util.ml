
open Core
open Include

let (fresh, reset, update) =
  let nxt = ref 0 in
  let f () = (nxt := !nxt + 1; !nxt) in
  let r () = nxt := 0 in
  let u n = nxt := Int.max !nxt n in
  (f, r, u)

module Var = struct
  (* This 'a is used so that Var.t can reference Exp.t *)
  type 'a t = {name : string ; mutable instance : 'a ref option}

  let create () = {name = Util.fresh (); instance = None}

  let name t = t.name
  let reset t = t.instance <- None
  let set_instance t p = t.instance <- Some p

  let has_instance t = Option.is_some t.instance

  let get_instance t = t.instance

  let to_string {name; instance} (f : 'a -> string) =
    match instance with
    | None -> "Var_" ^ name
    | Some x -> f !x

  let to_soln_string {name=_; instance} (f : 'a -> string) =
    match instance with
    | None -> "is free"
    | Some x -> f !x

  let equal v1 v2 = String.equal v1.name v2.name

  let deep_copy (v : 'a t) copy_f var_translation : 'a t =
    let instance =
      match v.instance with
      | None -> None
      | Some e -> copy_f e |> ref |> Some
    in
    let new_v : 'a t = {name = fresh () |> string_of_int; instance} in
    Hashtbl.set var_translation ~key:v.name ~data:(ref new_v);
    new_v

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

let operator_to_string (t : Ast.arithmetic_operator) =
  match t with
  | PLUS -> " + "
  | MINUS -> " - "
  | MULT -> " * "
  | DIV -> " / "

module Arithmetic_operand = struct
  type 'a t =
    | ArithmeticVar of 'a Var.t ref
    | ArithmeticInt of int

  let to_string t (f : 'a -> string) =
    match t with
    | ArithmeticVar v -> Var.to_string !v f
    | ArithmeticInt i -> Int.to_string i

  let deep_copy (t : 'a t) copy_f var_translation =
    match t with
    | ArithmeticInt _ -> t
    | ArithmeticVar v -> ArithmeticVar (Var.deep_copy !v copy_f var_translation |> ref);;

  let reref_vars (t : 'a t) copy_f reref_f tbl : 'a t =
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
      let rec resolve (e : t) =
        match e with
        | VarExp v -> (
            match !v.instance with
            | None -> e
            | Some e -> resolve !e
          )
        | _ -> e


    let rec to_string (t : t) =
      let readable_string_of_list list_exp =
        let rec inner_string list_exp =
          match list_exp with
          | TermExp ("empty_list", []) -> ""
          | TermExp ("list", [element; rest]) ->(
            let resolved = resolve !rest in
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
      | VarExp v -> (Var.to_soln_string !v to_string)
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
    ;;

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

module Dec = struct
  type t =
    | Clause of Exp.t * (Exp.t list)  (* Head :- Body. *)
    | Query of (Exp.t list)         (* ?- Body.      *)
end

module Trail = struct
  type t = Exp.t Var.t ref Stack.t
  type marker = int

  let mark t = Stack.length t

  let undo t marker =
    let num_to_undo = (Stack.length t) - marker in
    let rec loop n =
      if n > 0 && (n <= Stack.length t) then (
        let elt = Stack.pop_exn t in
        Var.reset (!elt);
        loop (n-1)
      )
    in
    loop num_to_undo

  let push = Stack.push

  let create () : t = Stack.create ()

end


let copy_arithmetic (a : Exp.t Arithmetic_operand.t) trail : Exp.t Arithmetic_operand.t =
  match a with
  | ArithmeticInt i -> ArithmeticInt i
  | ArithmeticVar v ->
    (
      if not (Var.has_instance !v) then
        (Trail.push trail v; Var.set_instance !v (ref (Exp.VarExp (ref (Var.create ())))));
      match !(Var.get_instance !v |> Option.value_exn) with
      | IntExp i -> ArithmeticInt i
      | VarExp v -> ArithmeticVar v
      | _ -> a
    )

(* NOTE we don't unify an ArithmeticVar with anything at any point (except on the rhs), so
    we should never need to reset it, and therefore don't need to properly copy it, or add it to
    the trail stack *)
let rec copy (t_ref : Exp.t ref ) trail : Exp.t ref = match !t_ref with
  | VarExp v -> (if not (Var.has_instance !v) then
                   (Trail.push trail v; Var.set_instance !v (ref (Exp.VarExp (ref (Var.create ())))));
                 Var.get_instance !v |> Option.value_exn )
  | TermExp (name, args) ->
    (* need to retain link to original variable? *)
    let args2 = List.map args ~f:(fun arg -> copy arg trail) in
    Exp.TermExp (name, args2) |> ref
  | IntExp i -> Exp.IntExp i |> ref
  | ArithmeticExp (operator, op1, op2) ->
    Exp.ArithmeticExp (operator, (copy_arithmetic op1 trail), (copy_arithmetic op2 trail)) |> ref

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
      | None -> if (occurs v t2_ref) then false else (Trail.push trail v; Var.set_instance !v t2_ref; true)
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
  type t = Exp.t ref * Exp.t ref list

  let copy (head, body) trail : t =
    let head2 = copy head trail in
    let body2 = List.map body ~f:(fun elt -> copy elt trail) in
    (head2, body2)
end

let print_solution var_mapping =
  print_endline "====================";
  Hashtbl.iteri var_mapping
    ~f:(fun ~key ~data ->
        let line = key ^ " = " ^ (Var.to_string data Exp.to_string) in
        print_endline line
      );
  print_endline "===================="

let solution_to_string var_mapping =
  let soln_str =
  (
    Hashtbl.fold ~init:"" var_mapping
    ~f:(fun ~key ~data acc ->
        acc ^
        key ^ " = " ^ (Var.to_soln_string data Exp.to_string) ^"\n"
      )
  )in
  ( if Hashtbl.length var_mapping > 0 then
      "====================\n"^soln_str^"====================" else "")

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

let arithmetic_convert_back (t : Exp.t Arithmetic_operand.t) : Ast.arithmetic_operand =
  let resolved = resolve_arith t in
  match resolved with
  | ArithmeticVar v -> ArithmeticVar (Var.name !v)
  | ArithmeticInt i -> ArithmeticInt i

let rec convert_back (t : Exp.t) : Ast.exp =
  let resolved = Exp.resolve t in
  match resolved with 
  | VarExp v ->  VarExp (Var.name !v)
  | IntExp i -> IntExp i
  | TermExp (name, args) -> 
    let new_args = List.map args ~f:(fun arg -> convert_back !arg ) in
    TermExp (name, new_args)
  | ArithmeticExp (op, op1, op2) ->
    let new_op1 = arithmetic_convert_back op1 in
    let new_op2 = arithmetic_convert_back op2 in 
    ArithmeticExp (op, new_op1, new_op2)

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

let realise_solution var_mapping =
  Hashtbl.fold var_mapping
    ~init:[]
    ~f:(fun ~key ~data acc -> (key, Var.to_string data Exp.to_string)::acc)
;;

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

let rec convert (t : Ast.exp) var_mapping : Exp.t =
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

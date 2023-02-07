open Core

open Util


module Var = struct
  (* This 'a is used so that Var.t can reference Exp.t *)
  type 'a t = {name : string ; mutable instance : 'a ref option}

  let create () = {name = fresh (); instance = None}

  let name t = t.name
  let reset t = t.instance <- None
  let set_instance t p = t.instance <- Some p

  let has_instance t = Option.is_some t.instance

  let get_instance t = t.instance

  let to_string {name; instance} (f : 'a -> string) =
    match instance with
    | None -> "Var" ^ name
    | Some x -> f !x

  let equal v1 v2 = String.equal v1.name v2.name

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
end

module Exp = struct
    type t =
      | VarExp of t Var.t ref
      | IntExp of int
      | TermExp of string * t ref list
      | ArithmeticExp of Ast.arithmetic_operator * t Arithmetic_operand.t * t Arithmetic_operand.t

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
  | ArithmeticVar v -> (
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
  print_endline "============";
  Hashtbl.iteri var_mapping
    ~f:(fun ~key ~data ->
        let line = key ^ " = " ^ (Var.to_string data Exp.to_string) in
        print_endline line
      );
    print_endline "============"

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


let rec eval_query q db (trail : Trail.t) var_mapping =
  match q with
  | [] -> print_solution var_mapping
  | g1::gl ->
      (
        match !g1 with
        (* if goal is the true predicate *)
        | Exp.TermExp("true", []) -> eval_query gl db trail var_mapping
        | TermExp("equals", [lhs; rhs]) -> (
            (* check if the lhs and rhs can unify *)
            let t = Trail.mark trail in
            if unify lhs rhs trail then
              eval_query gl db trail var_mapping;
            Trail.undo trail t
          )
        | TermExp("not_equal", [lhs;rhs]) -> (
            (* check if the lhs and rhs can unify. If they can, this is not a
               successful substitution. If they don't, we can continue solving the
               rest of the goals
            *)
            let t = Trail.mark trail in
            if not (unify lhs rhs trail) then (
              Trail.undo trail t;
              eval_query gl db trail var_mapping;
            );
            Trail.undo trail t
          )
        | TermExp("greater_than", [lhs; rhs]) -> (
          match (resolve !lhs), (resolve !rhs) with
          | IntExp i1, IntExp i2 ->
            if i1 > i2 then
              eval_query gl db trail var_mapping
          | _ -> () (* arguments insufficiently instantiated *)
        )
        | TermExp("greater_than_or_eq", [lhs; rhs]) -> (
            match (resolve !lhs), (resolve !rhs) with
            | IntExp i1, IntExp i2 ->
              if i1 >= i2 then
                eval_query gl db trail var_mapping
            | _ -> () (* arguments insufficiently instantiated *)
          )
        | TermExp("less_than", [lhs; rhs]) -> (
            match (resolve !lhs), (resolve !rhs) with
            | IntExp i1, IntExp i2 ->
              if i1 < i2 then
                eval_query gl db trail var_mapping
            | _ -> () (* arguments insufficiently instantiated *)
          )
        | TermExp("less_than_or_eq", [lhs; rhs]) -> (
            match (resolve !lhs), (resolve !rhs) with
            | IntExp i1, IntExp i2 ->
              if i1 <= i2 then
                eval_query gl db trail var_mapping
            | _ -> () (* arguments insufficiently instantiated *)
          )
        | TermExp("is", [lhs; rhs]) -> (
            (* evaluate the arithmetic expressions with current substitutions, then check if it is
               possible to unify them with any additional substitutions *)
            match !rhs with
            | ArithmeticExp (op, t1, t2) -> (
                match (resolve_arith t1), (resolve_arith t2) with
                | ArithmeticInt i1, ArithmeticInt i2 -> (
                    let result = perform_arithmetic op i1 i2 in
                    let t = Trail.mark trail in
                    (
                      match !lhs with
                      | VarExp _ -> if unify lhs (ref (Exp.IntExp result)) trail then
                          eval_query gl db trail var_mapping
                      | IntExp i -> if i = result then eval_query gl db trail var_mapping
                      | _ -> ()
                    ); Trail.undo trail t
                  )
                | _ -> ()
              )
            | IntExp result -> (
                let t = Trail.mark trail in
                (
                  match !lhs with
                  | VarExp _ -> if unify lhs (ref (Exp.IntExp result)) trail then
                      eval_query gl db trail var_mapping
                  | IntExp i -> if i = result then eval_query gl db trail var_mapping
                  | _ -> ()
                ); Trail.undo trail t
              )
            | _ -> ()
          )
        | TermExp(_,_) -> (
            let db_copy = List.map db ~f:(fun clause -> Clause.copy clause trail) in
            let rec loop db_copy =
              match db_copy with
              | [] -> ()
              | c::dbs -> (let t = Trail.mark trail in
                           let (head, body) = Clause.copy c trail in
                           Trail.undo trail t;
                           if unify head g1 trail then (
                             eval_query (body@gl) db trail var_mapping
                           );
                           Trail.undo trail t;
                           loop dbs
                          )
            in
            loop db_copy )
        | _ -> eval_query gl db trail var_mapping
      )

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


let command =
  Command.basic
    ~summary:"Sequential Prolog interpreter using a trail stack"
    [%map_open.Command
      let filename =
        flag
          ~doc:"FILE to read prolog from"
          "file"
          (required string)
      in
      fun () ->
        Interface.main filename
          ~eval_function:(fun db b ->
              (* convert the db and b into the required formats then feed to the eval function *)
              let var_mapping = String.Table.create () in
              let db_converted : Clause.t list = List.map db
                  ~f:(fun dec -> match dec with
                      | Clause (h, b) -> let h2 = convert h var_mapping in
                        let b2 = List.map b ~f:(fun e -> convert e var_mapping |> ref) in
                        (ref h2, b2)
                      | Query _ -> Error.raise (Error.of_string "There should be no queries in the database")
                    )
              in
              let var_mapping = String.Table.create () in
              let b_converted : Exp.t ref list = List.map b ~f:(fun e -> convert e var_mapping |> ref ) in
              let trail = Stack.create () in
              eval_query b_converted db_converted trail var_mapping;
              []
            )
    ]

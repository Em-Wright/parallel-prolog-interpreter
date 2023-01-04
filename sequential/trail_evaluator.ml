open Core
open Util


module Var = struct
  (* This 'a is used so that Var.t can reference Exp.t *)
  type 'a t = {name : string ; mutable instance : 'a ref option}

  let create () = {name = fresh (); instance = None}

  let reset t = t.instance <- None
  let set_instance t p = t.instance <- Some p

  let has_instance t = Option.is_some t.instance

  let get_instance t = t.instance

  let to_string {name; instance} (f : 'a -> string) =
    match instance with
    | None -> name
    | Some x -> f !x
end

module Arithmetic_operator = struct
  type t = PLUS | MINUS | MULT | DIV [@@deriving sexp]

  let to_string t =
    match t with
    | PLUS -> " + "
    | MINUS -> " - "
    | MULT -> " * "
    | DIV -> " / "
end

module Arithmetic_operand = struct
  type 'a t =
    | ArithmeticVar of 'a Var.t
    | ArithmeticInt of int

  let to_string t (f : 'a -> string) =
    match t with
    | ArithmeticVar v -> Var.to_string v f
    | ArithmeticInt i -> Int.to_string i
end

module Exp = struct
    type t =
      | VarExp of t Var.t
      | IntExp of int
      | TermExp of string * t ref list
      | ArithmeticExp of Arithmetic_operator.t * t Arithmetic_operand.t * t Arithmetic_operand.t

    let rec to_string t =
      match t with
      | VarExp v -> Var.to_string v to_string
      | IntExp i -> Int.to_string i
      | TermExp (name, args) ->
        let arg_string = List.fold args ~init:"" ~f:(fun acc arg -> acc ^ (to_string !arg) ^ ", ") in
        name ^ "(" ^ arg_string ^ ")"
      | ArithmeticExp (operator, op1, op2 ) ->
        (Arithmetic_operand.to_string op1 to_string)
        ^ (Arithmetic_operator.to_string operator)
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


(* NOTE we don't unify an ArithmeticVar with anything at any point (except on the rhs), so
    we should never need to reset it, and therefore don't need to properly copy it, or add it to
    the trail stack *)
let rec copy (t_ref : Exp.t ref ) trail : Exp.t ref = match !t_ref with
  | VarExp v -> (if not (Var.has_instance v) then
                   (Trail.push trail v; Var.set_instance v (ref (Exp.VarExp (Var.create ()))));
                 Var.get_instance v |> Option.value_exn )
  | TermExp (name, args) ->
    let args2 = List.map args ~f:(fun arg -> copy arg trail) in
    Exp.TermExp (name, args2) |> ref
  | IntExp i -> Exp.IntExp i |> ref
  | ArithmeticExp (operator, op1, op2) -> Exp.ArithmeticExp (operator, op1, op2) |> ref


let rec unify (t1_ref : Exp.t ref) (t2_ref : Exp.t ref) trail =
  match (!t1_ref) with
  | VarExp v -> (* TODO occurs check *)
    (
      match Var.get_instance v with
      | None -> Trail.push trail (ref v); Var.set_instance v t2_ref; true
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
  | _ -> (
      match !t2_ref with
      | VarExp _ -> unify t2_ref t1_ref trail
      | _ -> false
    )


module Clause = struct
  type t = Exp.t ref * Exp.t ref list

  let copy (head, body) trail_ref : t =
    let head2 = copy head trail_ref in
    let body2 = List.map body ~f:(fun elt -> copy elt trail_ref) in
    (head2, body2)
end

let print_solution var_mapping =
  Hashtbl.iteri var_mapping
    ~f:(fun ~key ~data ->
        let line = key ^ " = " ^ (Exp.to_string !data) in
        print_endline line
      )

let perform_arithmetic (op : Arithmetic_operator.t) i1 i2 =
  match op with
  | PLUS -> i1 + i2
  | MINUS -> i1 - i2
  | MULT -> i1 * i2
  | DIV -> i1 / i2

let rec eval_query q db trail var_mapping =
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
          match !lhs, !rhs with
          | IntExp i1, IntExp i2 ->
            if i1 > i2 then
              eval_query gl db trail var_mapping
          | _ -> () (* arguments insufficiently instantiated *)
        )
        | TermExp("less_than", [lhs; rhs]) -> (
            match !lhs, !rhs with
            | IntExp i1, IntExp i2 ->
              if i1 < i2 then
                eval_query gl db trail var_mapping
            | _ -> () (* arguments insufficiently instantiated *)
          )
        | TermExp("is", [lhs; rhs]) -> (
            (* evaluate the arithmetic expressions with current substitutions, then check if it is
               possible to unify them with any additional substitutions *)
            match !rhs with
            | ArithmeticExp (op, t1, t2) -> (
                match t1, t2 with
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
            let db_copy = List.map db ~f:(fun clause -> Clause.copy clause (ref trail)) in
            let rec loop db_copy =
              match db_copy with
              | [] -> eval_query q db trail var_mapping
              | c::dbs -> (let t = Trail.mark trail in
                           let (head, body) = Clause.copy c (ref trail) in
                           Trail.undo trail t;
                           if unify head g1 trail then (
                             eval_query (body@gl) db trail var_mapping;
                           );
                           Trail.undo trail t;
                           loop dbs
                          )
            in
            loop db_copy )
        | _ -> eval_query gl db trail var_mapping
      )

let arithmetic_convert (t : Exp.t Arithmetic_operand.t) var_mapping =
  match t with
  | ArithmeticVar v -> (
      match Hashtbl.find var_mapping v with
      | Some v2 -> v2
      | None -> let new_var : Exp.t Var.t = VarExp (Var.create ()) in
        Hashtbl.add_exn var_mapping ~key:v ~data:new_var;
        new_var
    )
  | ArithmeticInt i -> ArithmeticInt i

let convert (t : Ast.exp) var_mapping : Exp.t =
  match t with
  | VarExp v -> (
      match Hashtbl.find var_mapping v with
      | Some v2 -> v2
      | None -> let new_var : Exp.t Var.t = VarExp (Var.create ()) in
        Hashtbl.add_exn var_mapping ~key:v ~data:new_var;
        new_var
    )
  | IntExp i -> IntExp i
  | TermExp (name, args) ->
    let new_args = List.iter args ~f:(fun arg -> convert arg var_mapping |> ref) in
    TermExp (name, args)
  | ArithmeticExp (op, op1, op2) ->
    let new_op1 = 


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
              (* let db_converted = List.map db *)
              (*     ~f:(fun dec -> match dec with *)
              (*         | Clause (h, b) ->  *)
              (*       ) *)
              let trail = Stack.create () in
              eval_query db b trail
            )
    ]

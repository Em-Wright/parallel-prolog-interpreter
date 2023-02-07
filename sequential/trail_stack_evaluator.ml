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

  let deep_copy v copy_f =
    let instance =
      match v.instance with
      | None -> None
      | Some e -> copy_f e |> ref |> Some
    in
    {name = v.name; instance}

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

  let deep_copy t copy_f =
    match t with
    | ArithmeticInt _ -> t
    | ArithmeticVar v -> ArithmeticVar (Var.deep_copy !v copy_f |> ref)


  let reref_vars t copy_f tbl =
    match t with
    | ArithmeticInt _ -> t
    | ArithmeticVar v -> (
        match Hashtbl.find tbl (Var.name !v) with
        | None -> Var.deep_copy !v copy_f |> ref |> ArithmeticVar
        | Some v2 -> ArithmeticVar (ref v2)
      )
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

    let rec deep_copy e =
      match !e with
      | VarExp v -> Var.deep_copy !v (fun e -> deep_copy e) |> ref |> VarExp
      | IntExp _ -> !e
      | TermExp (n, args) ->
        let new_args = List.map args ~f:(fun arg -> deep_copy arg |> ref) in
        TermExp (n, new_args)
      | ArithmeticExp (operator, op1, op2) ->
        let op1_v2 = Arithmetic_operand.deep_copy op1 (fun e -> deep_copy e) in
        let op2_v2 = Arithmetic_operand.deep_copy op2 (fun e -> deep_copy e) in
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
      | VarExp v ->
        (
          match Hashtbl.find tbl (Var.name !v) with
          | None -> Var.deep_copy !v deep_copy |> ref |> VarExp
          | Some v2 -> VarExp (ref v2)
        )
      | IntExp _ -> e
      | TermExp (n, args) -> let new_args = List.map args ~f:(fun arg -> reref_vars !arg tbl |> ref) in
        TermExp (n, new_args)
      | ArithmeticExp (operator, op1, op2) ->
        let op1_v2 = Arithmetic_operand.reref_vars op1 (fun e -> deep_copy e) tbl in
        let op2_v2 = Arithmetic_operand.reref_vars op2 (fun e -> deep_copy e) tbl in
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

  let deep_copy (head, body) : t =
    let head2 = Exp.deep_copy head |> ref in
    let body2 = List.map body ~f:(fun elt -> Exp.deep_copy elt |> ref) in
    (head2, body2)

  let copy (head, body) : t =
    let head2 = Exp.shallow_copy head in
    let body2 = List.map body ~f:(fun elt -> Exp.shallow_copy elt) in
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

module Job = struct
  type t = {goals : Exp.t list; var_mapping : Exp.t Var.t String.Table.t }

  let deep_copy {goals; var_mapping} =
    (* TODO - need vars to be compatible when copied i.e. if we have a V273 in the
       var_mapping, and referenced somewhere in the goals, we need them to point to
       the same place. Maybe we build a hashmap of all variable names, and use that to
       find vars in the goals?

       Maybe we have the var_mapping be such a structure to begin with i.e. it doesn't
       only map the original variables, but also any additional variables we create as we go.
       Not sure if that would just be really inefficient tho.
    *)

    let new_var_mapping = String.Table.map var_mapping ~f:(fun v ->
        Var.deep_copy v (fun e -> Exp.deep_copy e)
      )
    in
    let new_goals = List.map goals ~f:(fun e -> Exp.reref_vars e new_var_mapping) in
    {goals=new_goals; var_mapping=new_var_mapping}

end


let rec eval_inner (q : Job.t Deque.t) db results =
  (* TODO why dequeue_back and not dequeue_front? *)
  match (Deque.dequeue_back q) with
  | None -> results
  | Some job -> (
      match job.goals with
      | [] -> let soln = realise_solution job.var_mapping in eval_inner q db (soln::results)
      | g1::gl -> (
          (
            match g1 with
            (* if goal is the true predicate *)
            | Exp.TermExp("true", []) -> Deque.enqueue_back q {goals=gl;var_mapping=job.var_mapping}
            | TermExp("equals", [lhs; rhs]) ->
              (* check if the lhs and rhs can unify *)
              (* TODO - we now need the unify function to not cause permanent changes - I guess we
              can use a mini trail to keep track of stuff? then discard the trail again after *)
              let trail = Trail.create () in
              if (unify lhs rhs trail) then (
                Deque.enqueue_back q {goals=gl; var_mapping=job.var_mapping}
              ) else Trail.undo trail
            | TermExp("not_equal", [lhs;rhs]) -> (
                (* check if the lhs and rhs can unify. If they can, this is not a
                   successful substitution. If they don't, we can continue solving the
                   rest of the goals
                *)
                let trail = Trail.create () in
                if not (unify lhs rhs trail) then (
                  Trail.undo trail;
                  Deque.enqueue_back q {goals=gl; var_mapping=job.var_mapping}
                ) else Trail.undo trail
              )
            | TermExp("greater_than", [lhs; rhs]) -> (
                match (resolve !lhs), (resolve !rhs) with
                | IntExp i1, IntExp i2 ->
                  if i1 > i2 then
                    Deque.enqueue_back q {goals=gl; var_mapping=job.var_mapping}
                | _ -> () (* arguments insufficiently instantiated *)
              )
            | TermExp("greater_than_or_eq", [lhs; rhs]) -> (
                match (resolve !lhs), (resolve !rhs) with
                | IntExp i1, IntExp i2 ->
                  if i1 >= i2 then
                    Deque.enqueue_back q {goals=gl; var_mapping=job.var_mapping}
                | _ -> () (* arguments insufficiently instantiated *)
              )
            | TermExp("less_than", [lhs; rhs]) -> (
                match (resolve !lhs), (resolve !rhs) with
                | IntExp i1, IntExp i2 ->
                  if i1 < i2 then
                    Deque.enqueue_back q {goals=gl; var_mapping=job.var_mapping}
                | _ -> () (* arguments insufficiently instantiated *)
              )
            | TermExp("less_than_or_eq", [lhs; rhs]) -> (
                match (resolve !lhs), (resolve !rhs) with
                | IntExp i1, IntExp i2 ->
                  if i1 <= i2 then
                    Deque.enqueue_back q {goals=gl; var_mapping=job.var_mapping}
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
                        (
                          match !lhs with
                          | VarExp _ -> let trail = Trail.create () in
                            if unify lhs (ref (Exp.IntExp result)) trail then
                              Deque.enqueue_back q {goals=gl; var_mapping=job.var_mapping}
                            else Trail.undo trail
                          | IntExp i -> if i = result then
                              Deque.enqueue_back q {goals=gl; var_mapping=job.var_mapping}
                          | _ -> ()
                        )
                      )
                    | _ -> ()
                  )
                | IntExp result -> (
                    (
                      match !lhs with
                      | VarExp _ -> let trail = Trail.create () in
                        if unify lhs (ref (Exp.IntExp result)) trail then
                          Deque.enqueue_back q {goals=gl; var_mapping=job.var_mapping }
                        else Trail.undo trail
                      | IntExp i -> if i = result then
                          Deque.enqueue_back q {goals=gl; var_mapping=job.var_mapping}
                      | _ -> ()
                    )
                  )
                | _ -> ()
              )
            | TermExp(_,_) -> (
                (* TODO - wait - can't just deep_copy, cause we need fresh variable names *)
                let db_copy = List.map db ~f:(fun clause -> Clause.copy clause ) in
                let rec loop db_copy =
                  match db_copy with
                  | [] -> ()
                  | c::dbs -> (
                               let (head, body) = Clause.deep_copy c trail in
                               let trail = Trail.create () in
                               if unify head g1 trail then (
                                 (* TODO - do I need to deep_copy each of the goals??? And then also
                                 would need to make sure the var_mapping matched it argh *)
                                 Deque.enqueue_back q {goals=(body@gl); var_mapping=____??????}
                               ) else Trail.undo trail;
                               (* TODO this is where we're going to have a problem - we have to undo the trail
                                  again before we can consider any more clauses, but we're relying on the trail
                                  remaining constant across jobs. Maybe we are also gonna have to
                                  pass a trail as part of the job? Seems a bit inefficient, but might not actually
                                  be that much slower? Probably worth a check, at the very least.
                                  The issue then also is that, since so many things are refs, how deep a copy do
                                  we need to do?
                                  Is there a way to have, instead of a marker, something that identifies a branch
                                  in a tree? i.e. the trail becomes a tree of tracking assignments. But
                                  we need that sort of structure for the variables as well, in that case. Hm
                                  So I need separate copies of some of the variables here. But separate copies
                                  are only needed in the case where we have OR-parallelism.
                                  Could attempt to identify which variables are only affected in this round, and
                                  then copy those Vars, and keep just the end of the trail in the job as well.
                                  So when we start a job, we potentially need to undo part of the trail, then
                                  add some more stuff back on.
                                  Maybe it would be best to try a version which copies everything, see how well
                                  that works, then only after that see what we can go back to sharing.
                                  So we'll need to remove a lot of refs? Maybe each job needs its own var_mapping,
                                  which in turn leads it to its own set of variables.
                                Tamara Norman's version says the trail becomes obsolete, since we just switch
                                  environments instead.
                               *)
                               Trail.undo trail t;
                               loop dbs
                              )
                in
                loop db_copy )
            | _ -> eval_query gl db trail var_mapping
          );
          eval_inner q db var_mapping results
        )
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

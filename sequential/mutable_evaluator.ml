open Ast
open Core
open Util
(* TODO - copy this text to a file in "Diss writing"
   Need to write an evaluator which uses a trail stack and mutability (so probably refs).
   Unification and stuff is already handled, so the main issue is going to be figuring out how to
   modify and then be able to undo assignments. Probably useful to use the stack version of
   the evaluator as the basis for this.
   We use 3 stacks:
   - local stack - stores env frames used to call predicates, and choice points. Stores
   Prolog variables and return addresses. Space on this stack is allocated during execution
   of a clause, and deallocated before the last subgoal is solved (due to tail-call optim).
   - control stack - stores choice points (I guess instead of the local stack storing them)
   Add choicepoints here when there are many possible clauses which apply to a goal.
   - global stack - might not actually need for a high-level implementation
   - trail stack - for storing assignments. Records information needed for backtracking. Is
   therefore closely related to the control stack.

   So we need to implement a loop which uses the local stack to figure out what work to do
   We need to figure out how much to pop from the top of the trail stack when we backtrack -
   determined by which assignments occurred at what depth of the tree - not exactly sure how
   we keep track of this.
*)

let (fresh, reset) =
  let nxt = ref 0 in
  let f () = (nxt := !nxt + 1; string_of_int (!nxt)) in
  let r () = nxt := 0 in
  (f, r)

module Var = struct
  (* TODO kinda need a circular definition to be able to have this as a stack of Exps *)
  type t = {subs : string Stack.t ;
           original : string
          }[@@deriving sexp]

  let reset (t : t) = Stack.pop_exn t.subs |> ignore

  let original_value (t : t) = t.original

  let value t = let value = Stack.pop_exn t.subs in
    Stack.push t.subs value; value

  let equal t1 t2 =
    let v1 = value t1 in
    let v2 = value t2 in
    String.equal v1 v2

  let equal_original t1 t2 = String.equal (original_value t1) (original_value t2)

  let compare t1 t2 =
    let v1 = value t1 in
    let v2 = value t2 in
    String.compare v1 v2

  let create () =
    let og_var = fresh () in
    let s = Stack.create () in
    Stack.push s og_var;
    {subs = s; original = og_var}
end

module Var_table = Hashtbl.Make (String)

type arithmetic_operator = PLUS | MINUS | MULT | DIV
[@@deriving equal, sexp, compare]

module Arithmetic_operand = struct
  type t =
      ArithmeticVar of (Var.t ref)
    | ArithmeticInt of int
  [@@deriving equal, sexp, compare]

  let copy t : t =
    match t with
    | ArithmeticVar _ -> ArithmeticVar (Var.create () |> ref)
    | ArithmeticInt i -> ArithmeticInt i
end


module Exp = struct
  type t = VarExp of (Var.t ref)             (* variables                *)
         | IntExp of int                 (* integers                 *)
         | TermExp of string * t list  (* functor(arg1, arg2, ...) *)
         | ArithmeticExp of arithmetic_operator * Arithmetic_operand.t * Arithmetic_operand.t
  [@@deriving equal, compare, sexp]

  let rec copy (t : t) = match t with
    | VarExp _ -> VarExp (Var.create () |> ref)
    (* TODO - should this be a new var?/new variable name?
                           If so, arithmetic variables probably should be as well *)
    | IntExp i -> IntExp i
    | TermExp (a, b) ->
      let c = List.map b ~f:(fun elt -> copy elt) in
      TermExp (a,c)
    | ArithmeticExp (operator, op1, op2) ->
      ArithmeticExp (operator,
                     Arithmetic_operand.copy op1,
                     Arithmetic_operand.copy op2
                    )

end
(* AM just has the trail as a list of variables - the base variables. Then each time an
   assignment/unification occurs, we push this original variable name to the trail stack.
   When we go to undo, we therefore pop a variable name from the stack, find it in the map
   which gives the solutions, and remove the most recent assignment to that variable
   (probably by popping from another stack). We perform assignment/unification by ...
*)
module Trail = struct
  type t = (Var.t ref) Stack.t
  type pointer = int

  let mark t = Stack.length t

  let undo t p =
    let to_remove = Stack.length t - p in
    for _ = 0 to to_remove do
      let var_ref = Stack.pop_exn t in
      Var.reset !var_ref
    done
  ;;

  let append t assignment = Stack.push t assignment
end

module Dec = struct
  type t =
    | Clause of (Exp.t ref) * (Exp.t ref list)
    | Query of (Exp.t ref list) [@@deriving equal, sexp]

  let rec copy t =
    match t with
    | Clause (h, t) -> let h2 = Exp.copy !h |> ref in
      let t2 = List.map t ~f:(fun elt -> Exp.copy !elt |> ref) in
      Clause (h2, t2)
    | Query l -> let l2 = List.map l ~f:(fun elt -> Exp.copy !elt |> ref) in
      Query l2

end

let sub_lift_goal_arithmetic sub a =
  match a with
  | ArithmeticVar v -> (
      (* if this variable has a substitution do the substitution *)
      match Var_table.find sub v with
      | Some (IntExp i2) -> ArithmeticInt i2
      | Some (VarExp v2) -> ArithmeticVar v2
      | None -> a
      | _ -> raise (FAILED_SUBSTITUTION "Attempted to substitute an ArithmeticExp or a TermExp for a variable in\
                                         an arithmetic expression. If this has occurred, I've implemented\
                                         arithmetic wrong. Oops. ")
    )
  | _ -> a

let rec sub_lift_goal sub g =
    match g with
    | VarExp v -> (
        (* if this variable has a substitution do the substitution *)
        match Var_table.find sub v with
        | Some i -> i
        | None -> VarExp v
      )
    | TermExp (s, el) ->
      TermExp (s, List.map ~f:(fun g1 -> sub_lift_goal sub g1) el)
    | ArithmeticExp (op, e1, e2) -> ArithmeticExp(op, sub_lift_goal_arithmetic sub e1, sub_lift_goal_arithmetic sub e2)
    | _  -> g

let rec unify trail (assignments : Exp.t Var_table.t) (s : Exp.t) (t : Exp.t) =
  (* we unify by assignment, then noting this assignment on the trail *)
  (* we need to check if the goal and rule unify wrt all the previous asignments as well *)
  (* this is why we need to have copied variables beforehand - so that we won't have the
  same variables in the rule as ones in the goal, when they don't refer to the same thing *)
  if Exp.equal s t
  then true
  else (
    let success = ref false in
    (
      match s with
      | VarExp(v) -> (* TODO do we need an occurs check? *)
        (* sub 'rule' in for v, add v to trail (or v's original value???) *)
        (* TODO - in the case where a variable in the goal already has a substitution, we need
        to have performed the equivalent of sub_lift_goal so that it's already set to whatever
        value it ought to be? Since we perform updates by assignment, we can just update the
        goal as it is? We will already have copied clauses from the original program, so we
        won't be editing the original program anyway *)
        Var_table.update assignments v ~f:(fun prev_opt ->
            match prev_opt with
            | None -> success := true; Trail.append trail v; t
            | Some (VarExp x) -> (* if x != v, we have an issue. *)
              if String.equal x v then ( success := true; Trail.append trail v; t )
              (* TODO - if there's already a substitution, is that fine so long as we can unify
              with that substitution? *)
              else (print_endline "variable already has substitution."; t)
            | Some x -> (print_endline "variable already has non-variable substitution."; x )
          )
      | TermExp (sname, sargs) -> (
          match t with
          | VarExp _ -> success := (unify trail assignments t s)
          | TermExp (tname, targs) -> (
              if (String.equal tname sname) && (List.length targs = List.length sargs)
              then (* check all of the targs and sargs unify as well *)
                (* can we do this with List.iter? Or do I need recursion? *)
                success := List.fold
                    (List.zip_exn sargs targs)
                    ~init:true
                    ~f:(fun acc (s,t) -> (unify trail assignments s t) && acc)
              else success := false
            )
          | _ -> success := false
        )
      | _ -> (
        match t with
          | VarExp _ -> success := (unify trail assignments t s)
          | _ -> success := false
      )
    ); !success
  )

let rec eval_query db _q trail =
  (* TODO - copy the db and treat it as a stack??? *)
  let rec loop db solns =
    let new_solns = 
      match db with
      | [] -> solns
      | r::dbs ->
        (
          let t_pointer = Trail.mark trail in
          match r with
          | Clause (head, body) ->
            (
            match q with
            | g1:gl ->
            | [] -> 
          )
          (* take a copy of the head, with fresh variables - these fresh variable assignments
             get added to the trail, so we need to remember to remove them after
          *)
          (* call unify [(head, g1)] - if it works, add the body to the list of
             goals (presumably with variable names changed as needed)
          *)
          (* if the list of remaining goals is empty
             then add the current substitutions to solns else call loop again
          *)
          | Query _ -> print_endline "Error: Query in the database"; solns
        )
    in
    ()
    (* undo the trail - do we just reset things to original values??? *)
    (* call eval_query on the tail of q ??? *)
  in
  loop db []
;;

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
         Interface.main filename ~eval_function:(fun db b -> eval_query db b [])
    ]

(* open Ast *)
open Core
open Util

let (fresh, current, reset) =
  let nxt = ref 0 in
  let f () = (nxt := !nxt + 1; !nxt) in
  let c () = !nxt in
  let r () = nxt := 0 in
  (f, c, r)

class expr () =
  object
    method copy = {< >}
  end

class exp_var () =
  object
    inherit expr ()

    val varno = fresh ()
    val mutable instance = None

    method get_varno = varno

    method equal (t : exp_var) =
      Int.equal varno (t#get_varno)

    method set_instance (p : expr ref option) =
      instance <- p

    method [@warning "-7"] copy =
      let cp = {< varno = fresh (); instance = instance >} in
      cp

    method reset : unit = instance <- None

  end

class exp_int value = object
  inherit expr ()

  val value : int = value

  method get_value : int = value

end

class exp_term operator_init args_init =
  object
    inherit expr ()

    val operator : string = operator_init
    val args : (#expr) list = args_init

    method get_operator = operator

    method [@warning "-7"] copy =
      (* copy each of the args, then return another exp_term with the copies *)
      let args2 = List.map args ~f:(fun a -> a#copy) in
      {< operator = operator; args = args2 >}

  end

module Trail = struct
  type t = exp_var ref Stack.t
  type pointer = int

  let mark t = Stack.length t

  let undo t p =
    let to_remove = Stack.length t - p in
    for _ = 0 to to_remove do
      let v = Stack.pop_exn t in
      v#reset
    done
  ;;

  let append t assignment = Stack.push t assignment
end

module Var_table = Hashtbl.Make (String)

type arithmetic_operator = PLUS | MINUS | MULT | DIV
[@@deriving equal, sexp, compare]



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

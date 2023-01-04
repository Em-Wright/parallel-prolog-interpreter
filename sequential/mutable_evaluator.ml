open Core

let (fresh, current, reset) =
  let nxt = ref 0 in
  let f () = (nxt := !nxt + 1; !nxt) in
  let c () = !nxt in
  let r () = nxt := 0 in
  (f, c, r)

module Trail = struct
  type 'a t = 'a Stack.t
  type pointer = int

  let mark t = Stack.length t

  let undo t p =
    let to_remove = Stack.length t - p in
    for _ = 0 to to_remove do
      let v : 'a = Stack.pop_exn t in
      v#reset
    done
  ;;

  let append t assignment = Stack.push t assignment
end

class expr () =
  object (_self : 'self)

    method copy : 'self = {< >}

    method unify (_ : 'self) : bool = false

    method unify2 (_ : 'self) : bool = false
  end

class exp_var trail_ref
  =
  object (self : 'self)
    inherit expr ()

    val varno = fresh ()
    val mutable instance = None
    val trail_ref : 'self Trail.t ref = trail_ref

    method get_varno = varno

    (* these are here for compatibility with exp_term's unify2 function *)
    method get_operator = ""
    method get_args
      : (< copy : 'a; unify : 'a -> bool; unify2 : 'a -> bool; get_operator : string; get_arity: int; .. > as 'a) list
          = []
    method get_arity = -1


    method [@warning "-7"] copy =
      match instance with
      | None ->
        (Trail.append (!trail_ref) self;
         let cp = {< varno = fresh (); instance = None; trail_ref = trail_ref >} in
         instance <- Some cp;
         cp
        )
      | Some instance -> instance

    method reset : unit = instance <- None

    method [@warning "-7"] unify
        (t2 : (<copy : 'a; unify: 'a -> bool; unify2 : 'a -> bool; .. > as 'a) ) : bool
      =
        match instance with
        | Some instance -> instance#unify t2
        | None -> (Trail.append (!trail_ref) self; instance <- (Some t2); true )

    method [@warning "-7"] unify2 = self#unify

  end


class exp_term operator_init args_init =
  object (self : 'self)
    inherit expr ()

    val operator : string = operator_init
    val args
      : (< copy : 'a; unify : 'a -> bool; unify2 : 'a -> bool; get_operator : string; get_arity: int; .. > as 'a) list
      = args_init
    val arity : int = List.length args_init

    method get_operator = operator
    method get_args
      : (< copy : 'a; unify : 'a -> bool; unify2 : 'a -> bool; get_operator : string; get_arity: int; .. > as 'a) list
      = args
    method get_arity = arity

    method [@warning "-7"] copy : 'self =
      (* copy each of the args, then return another exp_term with the copies *)
      let args2 = List.map args ~f:(fun a -> a#copy) in
      {< operator = operator; args = args2 >}

    method [@warning "-7"] unify
      (t2 : (<copy : 'a; unify: 'a -> bool; unify2 : 'a -> bool; .. > as 'a) ) : bool
      =
      t2#unify2 self

    method [@warning "-7"] unify2
        (t : (<copy : 'a; unify: 'a -> bool; unify2 : 'a -> bool; get_operator : string
               ; get_arity : int ; get_args :
                                     (< copy : 'b;
                                      unify : 'b -> bool;
                                      unify2 : 'b -> bool;
                                      get_operator : string;
                                      get_arity: int; .. > as 'b) list
                ; .. > as 'a) ) : bool
      =
      String.equal operator (t#get_operator) &&
      Int.equal arity t#get_arity
      &&
      List.fold2_exn args (t#get_args) ~init:true
        ~f:(fun acc a1 a2 ->
            let result = a1#unify a2 in
              acc && result
          )

  end

class exp_int value = object
  inherit expr ()

  val value : int = value

  method get_value : int = value

  (* TODO - finish this and also exp_arithmetic *)

end

class exp_arithmetic operator op1 op2 = object
  inherit expr ()

  val operator : Ast.arithmetic_operator = operator
  val operand1 : (<copy : 'a; unify :'a -> bool; unify2 : 'a -> bool> as 'a) = op1
  val operand2 : (<copy : 'a; unify :'a -> bool; unify2 : 'a -> bool> as 'a) = op2

end

class clause head body = object
  val head : exp_term = head
  val body : exp_term list = body

  method copy = let head2 = head#copy in
    let body2 = List.map body ~f:(fun elt -> elt#copy) in
    {<head = head2; body = body2>}

  method get_head = head

  method get_body = body
end

type exp =
  | ExpVar of exp_var
  | ExpTerm of exp_term
  | ExpInt of exp_int
  | ExpArithmetic of exp_arithmetic

let arith_exp_to_class (e : Ast.arithmetic_operand)
    (var_mapping : exp_var String.Map.t) (trail_ref : exp_var Trail.t ref )
  : ( exp * exp_var String.Map.t) =
  match e with
  | ArithmeticVar s ->
    let existing = Map.find var_mapping s in
    (
      match existing with
      | Some v -> (ExpVar v, var_mapping)
      | None -> let v = new exp_var trail_ref in
        let updated_map = Map.add_exn var_mapping ~key:s ~data:( v) in
        (ExpVar v, updated_map)
    )
  | ArithmeticInt i -> ( ExpInt (new exp_int i), var_mapping)

let rec exp_to_class (e : Ast.exp) (var_mapping : exp_var String.Map.t) (trail_ref : exp_var Trail.t ref )
  : exp * (exp_var String.Map.t) =
  match e with
  | IntExp i -> (ExpInt (new exp_int i), var_mapping)
  | VarExp s ->
    let existing = Map.find var_mapping s in
    (
      match existing with
      | Some v -> (ExpVar v, var_mapping)
      | None -> let v = new exp_var trail_ref in
        let updated_map = Map.add_exn var_mapping ~key:s ~data:( v) in
        (ExpVar v, updated_map)
    )
  | TermExp (operator, args) -> let (args2, updated_map) = List.fold args ~init:([], var_mapping)
                                    ~f:(fun (new_args, new_var_mapping) arg ->
                                        let new_arg, updated_map = exp_to_class arg new_var_mapping trail_ref in
                                        (new_args@[new_arg], updated_map)
                                      )
                                    in
    (ExpTerm (new exp_term operator args2), updated_map)
  | ArithmeticExp (operator, op1, op2) ->
    let (new_op1, var_mapping2) = arith_exp_to_class op1 var_mapping trail_ref in
    let (new_op2, var_mapping3) = arith_exp_to_class op2 var_mapping2 trail_ref in
    (ExpArithmetic (new exp_arithmetic operator new_op1 new_op2), var_mapping2)


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
               let trail : exp_var Trail.t = Stack.create () in
               let t1 = new exp_term "true" [] in
               let t2 = new exp_var (ref trail) in
               let t3 = new exp_term "testing" [t1; t2] in
               eval_query db b []
                          )
    ]

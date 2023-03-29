open OUnit2
open Trail_parallel.Trail_util
open Core

let identity_func s = s
let turn_to_unit _ = ()

let trail_util_test_suite =
  "Trail_util" >::: (
    List.map ~f:(
      fun (arg, res) ->
        let title =
          res
        in
        title >:: (
          fun _test_ctxt ->
            assert_equal
              ~printer:identity_func
              res arg
        )
    )

      [
        (* Fresh variables *)
        (turn_to_unit (reset());
         turn_to_unit (fresh());
         fresh() |> string_of_int
        ), "2";

        (turn_to_unit (fresh());
         turn_to_unit (fresh());
         turn_to_unit (reset());
         fresh() |> string_of_int
        ), "1";


        (reset ();
         let v1 = Var.create () in
         let v2 = Exp.VarExp (Var.create () |> ref) in
         Var.set_instance v1 (ref v2);
           Var.to_string v1 Exp.to_string), "Var_2";

        (reset ();
         let v1 = Var.create () in
         let v2 = Exp.VarExp (Var.create_named "B" |> ref) in
         Var.set_instance v1 (ref v2);
         let var_translation = String.Table.create () in
         let v3 = Var.deep_copy v1 (fun e -> Exp.deep_copy e var_translation) var_translation in
         Var.to_string v3 Exp.to_string), "Var_2";

        (
          reset ();
          let v1 = Exp.VarExp (Var.create () |> ref ) |> ref in
          let v2 = Exp.VarExp (Var.create () |> ref ) |> ref in
          let v3 = Var.create_named "X" |> ref in
          let term = Exp.TermExp ("predicate", [v1; v2; ref (Exp.IntExp 4)]) in
          let tbl = String.Table.create () in
          String.Table.add_exn tbl ~key:"1" ~data:v3;
          let term2 = Exp.reref_vars term tbl in
          Exp.to_string term2
        ), "predicate(Var_X, Var_3, 4, )";

        (
          reset ();
          let v1 = Exp.VarExp (Var.create () |> ref ) |> ref in
          let v2 = Exp.VarExp (Var.create () |> ref ) |> ref in
          let v3 = Exp.VarExp (Var.create_named "X" |> ref) |> ref in
          let term = Exp.TermExp ("predicate", [v1; v2; v3; ref (Exp.IntExp 4)]) in
          let serialised = Exp.serialise term in
          Exp.serialisable_to_string serialised
        ), "predicate(Var_1, Var_2, Var_X, 4, )";

        (
          reset ();
          let v1 = Arithmetic_operand.ArithmeticVar (Var.create () |> ref ) in
          let v2 = Arithmetic_operand.ArithmeticVar (Var.create () |> ref ) in
          let term = Exp.ArithmeticExp (PLUS, v1, v2) in
          let serialised = Exp.serialise term in
          Exp.serialisable_to_string serialised
        ), "Var_1 + Var_2";

        (
          reset ();
          let v1 = Exp.VarExpS  {name="X"; instance=None} in
          let v2 = Exp.VarExpS  {name= "Y"; instance=Some (Exp.VarExpS {name= "Z"; instance= None})} in
          let term = Exp.TermExpS ("predicate", [v1; v2; (Exp.IntExpS 4)]) in
          let deserialised = Exp.deserialise term (String.Table.create ()) in
          Exp.to_string deserialised
        ), "predicate(Var_X, Var_Z, 4, )";

        (
          reset ();
          let v1 = Arithmetic_operand.ArithmeticVarS {name="X"; instance=None} in
          let v2 = Arithmetic_operand.ArithmeticVarS {name="Y"; instance=None} in
          let term = Exp.ArithmeticExpS (PLUS, v1, v2) in
          let deserialised = Exp.deserialise term (String.Table.create ()) in
          Exp.to_string deserialised
        ), "Var_X + Var_Y";



        (* TODO - actually write the tests *)

        (* need testing for get_furthest_instance, occurs, unify, resolve,
        Clause.deep_copy, Clause.serialise, Clause.deserialise, Job.deep_copy, Dec.serialise,
        Dec.deserialise; Trail.push, Trail.undo *)

    ]
  )

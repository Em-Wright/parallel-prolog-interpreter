open OUnit2
open Trail_sequential.Trail_util
open Trail_sequential.Trail_evaluator
open Prolog_interpreter.Util
open Core


let identity_func s = s
let turn_to_unit _ = ()

let eval_query (b, db, _ ) _vars =
  let db_converted : Clause.t list = List.map db
      ~f:(fun dec ->
          let var_mapping = String.Table.create () in
          match (dec : Prolog_interpreter.Ast.dec) with
          | Clause (h, b) -> let h2 = convert h var_mapping in
            let b2 = List.map b ~f:(fun e -> convert e var_mapping |> ref) in
            (ref h2, b2)
          | Query _ -> Error.raise (Error.of_string "There should be no queries in the database")
        )
  in
  let var_mapping = String.Table.create () in
  let b_converted : (Exp.t ref * int) list = List.map b ~f:(fun e -> convert e var_mapping |> ref , 0) in
  let trail = Stack.create () in
  let res, _ = eval_query b_converted db_converted trail var_mapping in
  res

let trail_evaluator_test_suite =
    "TrailEvaluator" >::: (
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
            (* Evaluating results of a query with a given db *)
            ( string_of_res
                (eval_query
                    (
                        [],
                        [],
                        []
                    ) String.Set.empty
                ) 
                [] 0
            ), "true\n";

            (
                string_of_res
                (eval_query
                    (
                        [TermExp ("true", [])],
                        [],
                        []
                      ) String.Set.empty
                )
                [] 0
            ), "true\n";


            (
                string_of_res
                (eval_query
                    (
                        [TermExp ("male", [TermExp ("elizabeth", [])])],
                        [],
                        []
                    ) String.Set.empty
                )
                [] 0
            ), "false\n";

            (
                string_of_res
                (eval_query
                    (
                        [TermExp ("parent", [VarExp "X"; TermExp ("charles1", [])])],
                        [],
                        []
                    ) (String.Set.of_list ["X"])
                )
                [VarExp "X"] 1
            ), "false\n";

            (
                string_of_res
                (eval_query
                    (
                        [TermExp ("male", [TermExp ("elizabeth", [])])],
                        [Clause (TermExp("female", [TermExp("elizabeth", [TermExp ("true", [])])]), [])],
                        []
                    ) String.Set.empty
                )
                [] 0
            ), "false\n";

            (
                string_of_res
                (eval_query
                    (
                        [TermExp ("male", [TermExp ("elizabeth", [])])],
                        [Clause (TermExp("elizabeth", [TermExp("male", [])]), [TermExp ("true", [])])],
                        []
                    ) String.Set.empty
                )
                [] 0
            ), "false\n";

            (
                string_of_res
                (eval_query
                    (
                        [TermExp ("female", [TermExp ("elizabeth", [])])],
                        [Clause (TermExp("female", [TermExp("elizabeth", [])]), [TermExp ("true", [])])],
                        []
                    ) String.Set.empty
                )
                [] 0
            ), "true\n";

            (
                string_of_res
                (eval_query
                    (
                        [TermExp ("female", [TermExp ("elizabeth", [])])],
                        [Clause (TermExp("female", [TermExp("elizabeth", [])]), [TermExp("true", [])])],
                        []
                    ) String.Set.empty
                )
                [] 0
            ), "true\n";

            (
                string_of_res
                (eval_query
                    (
                        [TermExp ("female", [TermExp ("elizabeth", [])])],
                        [Clause (TermExp("female", [TermExp("elizabeth", [])]), [TermExp("true", [])])],
                        []
                    ) String.Set.empty
                )
                [] 0
            ), "true\n";

            (
                string_of_res
                (eval_query
                    (
                        [TermExp("age", [TermExp("zaid",[]); VarExp "Y"])],
                        [],
                        []
                    )
                    (String.Set.of_list ["Y"])
                )
                [VarExp "Y"] 1
            ), "false\n";

            (
                string_of_res
                (eval_query
                    (
                        [TermExp("age", [TermExp("zaid",[]); VarExp "Y"])],
                        [Clause (TermExp ("age", [ TermExp ("adam", []);
                              IntExp 10]), [TermExp ("true", [])])],
                        []
                    )
                  (String.Set.of_list ["Y"])
                )
                [VarExp "Y"] 1
            ), "false\n";


            (
                string_of_res
                (eval_query
                    (
                        [TermExp("age", [VarExp "E"; VarExp "Z"])],
                        [Clause (TermExp ("age", [TermExp ("adam", []);
                              IntExp 10]), [TermExp ("true", [])]);Clause (TermExp ("age", [TermExp ("zaid", []);  (IntExp 5)]), [TermExp ("true", [])])],
                        []
                    )
                  (String.Set.of_list ["E"; "Z"])
                )
                [VarExp "E"; VarExp "Z"] 2
            ), "====================\nZ = 10\nE = adam\n====================\n====================\nZ = 5\nE = zaid\n====================\ntrue\n";

            (
                string_of_res
                (eval_query
                    (
                        [TermExp("age", [VarExp "X";  (IntExp 5)])],
                        [Clause (TermExp ("age", [TermExp ("adam", []);
                            IntExp 10]), [TermExp ("true", [])]);Clause (TermExp ("age", [TermExp ("zaid", []);  (IntExp 5)]), [TermExp ("true", [])])],
                        []
                    )
                  (String.Set.of_list ["X"])
                )
                [VarExp "X"] 1
            ), "====================\nX = zaid\n====================\ntrue\n";

            (
                string_of_res
                (eval_query
                    (
                        [TermExp ("a", [])],
                        [Clause (TermExp ("a", []), [TermExp ("true", [])])],
                        []
                    )
                    String.Set.empty
                )
                [] 0
            ), "true\n";

            (
                string_of_res
               (eval_query
                  (
                    [TermExp ("prepend", [
                         IntExp 1;
                         TermExp ("list", [
                             IntExp 2;
                             TermExp ("empty_list", [])
                           ]);
                         VarExp "X"
                       ])],
                    [
                      Clause (TermExp ("prepend", [VarExp "H"; VarExp "T";
                                                   TermExp ("list", [
                                                       VarExp "H";
                                                       VarExp "T"
                                                     ])
                                                  ]),
                              [ TermExp ("true", []) ]
                             )
                    ],
                    []
                  )
                  (String.Set.of_list ["X"])
               )
                [VarExp "X"] 1
            ), "====================\nX = [1, 2]\n====================\ntrue\n";

            (
                string_of_res
               (eval_query
                  (
                    [TermExp("nat1", [VarExp "Z"])],
                    [
                      Clause (TermExp("nat", [IntExp 0]), [TermExp("true", [])]);
                      Clause (TermExp("nat1", [VarExp "X"]), [
                          TermExp("nat", [VarExp "Y"]);
                          TermExp("is", [ VarExp "X"; ArithmeticExp(PLUS, ArithmeticVar "Y", ArithmeticInt 1)])
                        ])
                    ],
                    []
                  )
                  (String.Set.of_list ["Z"])
               )
                [VarExp "Z"] 1
            ), "====================\nZ = 1\n====================\ntrue\n";

            (
                string_of_res
               (eval_query
                  (
                    [TermExp("is_ten", [VarExp "Z"])],
                    [
                      Clause (TermExp("is_one", [IntExp 1]), [TermExp("true", [])]);
                      Clause (TermExp("is_ten", [VarExp "X"]), [
                          TermExp("is_one", [VarExp "Y"]);
                          TermExp("is", [ VarExp "X"; ArithmeticExp(MULT, ArithmeticVar "Y", ArithmeticInt 10)])
                        ])
                    ],
                    []
                  )
                  (String.Set.of_list ["Z"])
               )
                [VarExp "Z"] 1
            ), "====================\nZ = 10\n====================\ntrue\n";

            (
                string_of_res
               (eval_query
                  (
                    [TermExp("is_five", [VarExp "Z"])],
                    [
                      Clause (TermExp("is_minus_ten", [IntExp (-10)]), [TermExp("true", [])]);
                      Clause (TermExp("is_five", [VarExp "X"]), [
                          TermExp("is_minus_ten", [VarExp "Y"]);
                          TermExp("is", [ VarExp "X"; ArithmeticExp(DIV, ArithmeticVar "Y",
                                                                    ArithmeticInt (-2))])
                        ])
                    ],
                    []
                  )
                  (String.Set.of_list ["Z"])
               )
                [VarExp "Z"] 1
            ), "====================\nZ = 5\n====================\ntrue\n";

            (
                string_of_res
               (eval_query
                  (
                    [TermExp("nat", [VarExp "Z"])],
                    [
                      Clause (TermExp("nat", [VarExp "X"]), [
                            TermExp("equals", [VarExp "X"; IntExp 0])
                        ]
                             );
                      Clause (TermExp("nat", [VarExp "X"]), [
                          TermExp("equals", [VarExp "X"; IntExp 7])
                        ]
                        )
                    ],
                    []
                  )
                  (String.Set.of_list ["Z"])
               )
                [VarExp "Z"] 1
            ), "====================\n\
                Z = 0\n\
                ====================\n\
                ====================\n\
                Z = 7\n\
                ====================\n\
                true\n";

            (
                string_of_res
               (eval_query
                  (
                    [TermExp("not_two", [VarExp "Z"])],
                    [
                      Clause (TermExp("nat", [IntExp (1)]), [TermExp("true", [])]);
                      Clause (TermExp("nat", [IntExp (2)]), [TermExp("true", [])]);
                      Clause (TermExp("nat", [IntExp (3)]), [TermExp("true", [])]);
                      Clause (TermExp("nat", [IntExp (4)]), [TermExp("true", [])]);
                      Clause (TermExp("not_two", [VarExp "X"]), [
                          TermExp("nat", [VarExp "X"]);
                          TermExp("not_equal", [ VarExp "X"; IntExp 2])
                        ])
                    ],
                    []
                  )
                  (String.Set.of_list ["Z"])
               )
                [VarExp "Z"] 1
            ), "====================\n\
                Z = 1\n\
                ====================\n\
                ====================\n\
                Z = 3\n\
                ====================\n\
                ====================\n\
                Z = 4\n\
                ====================\ntrue\n";

            (
                string_of_res
               (eval_query
                  (
                    [TermExp("nat1", [VarExp "Z"])],
                    [
                      Clause (TermExp("nat", [IntExp (-2)]), [TermExp("true", [])]);
                      Clause (TermExp("nat", [IntExp (-1)]), [TermExp("true", [])]);
                      Clause (TermExp("nat", [IntExp 3]), [TermExp("true", [])]);
                      Clause (TermExp("nat", [IntExp 5]), [TermExp("true", [])]);
                      Clause (TermExp("nat", [IntExp 6]), [TermExp("true", [])]);
                      Clause (TermExp("nat1", [VarExp "X"]), [
                          TermExp("nat", [VarExp "X"]);
                          TermExp("less_than", [ VarExp "X"; IntExp 5 ]);
                          TermExp("greater_than", [ VarExp "X"; IntExp (-2) ])
                        ])
                    ],
                    []
                  )
                  (String.Set.of_list ["Z"])
               )
                [VarExp "Z"] 1
            ), "====================\n\
                Z = -1\n\
                ====================\n\
                ====================\n\
                Z = 3\n\
                ====================\n\
                true\n";

            (
                string_of_res
                (eval_query
                    (
                        [TermExp("age", [VarExp "X"; VarExp "Y"]); TermExp("female", [VarExp "X"])],
                        [Clause (TermExp ("age", [ TermExp("adam", []); IntExp 10]), [TermExp ("true", [])]);Clause (TermExp ("age", [TermExp ("zaid", []);  (IntExp 5)]), [TermExp ("true", [])]); Clause (TermExp ("age", [TermExp ("ann", []);  (IntExp 12)]), [TermExp ("true", [])]); Clause (TermExp ("male", [TermExp ("zaid", [])]), [TermExp ("true", [])]); Clause (TermExp ("male", [ TermExp("adam", [])]), [TermExp ("true", [])]); Clause (TermExp ("female", [TermExp ("ann",[])]),[TermExp ("true", [])])],
                        []
                    )
                  (String.Set.of_list ["X"; "Y"])
                )
                [VarExp "X"; VarExp "Y"] 2
            ), "====================\nY = 12\nX = ann\n====================\ntrue\n";

            (
                string_of_res
                (eval_query
                    (
                        [TermExp("sibling", [TermExp("sally",[]); TermExp("erica",[])])],
                        [Clause (TermExp ("parent_child", [VarExp "X"; VarExp "Y"]), [TermExp ("mother_child", [VarExp "X"; VarExp "Y"])]); Clause (TermExp ("parent_child", [VarExp "X"; VarExp "Y"]), [TermExp ("father_child", [VarExp "X"; VarExp "Y"])]); Clause (TermExp ("sibling", [VarExp "X"; VarExp "Y"]), [TermExp ("parent_child", [VarExp "Z"; VarExp "X"]); TermExp ("parent_child", [VarExp "Z"; VarExp "Y"])]); Clause (TermExp ("father_child", [TermExp ("mike", []); TermExp ("tom", [])]), [TermExp ("true", [])]); Clause (TermExp ("father_child", [TermExp ("tom", []); TermExp ("erica", [])]), [TermExp ("true", [])]); Clause (TermExp ("father_child", [TermExp ("tom", []); TermExp ("sally", [])]), [TermExp ("true", [])]); Clause (TermExp ("mother_child", [TermExp ("trude", []); TermExp ("sally", [])]), [TermExp ("true", [])])],
                        []
                    )
                  String.Set.empty
                )
                [] 0
            ), "true\n";

            (
                string_of_res
                (eval_query
                    (
                        [TermExp("sibling", [VarExp "Z"; VarExp "E"])],
                        [Clause (TermExp ("parent_child", [VarExp "X"; VarExp "Y"]), [TermExp ("mother_child", [VarExp "X"; VarExp "Y"])]); Clause (TermExp ("parent_child", [VarExp "X"; VarExp "Y"]), [TermExp ("father_child", [VarExp "X"; VarExp "Y"])]); Clause (TermExp ("sibling", [VarExp "X"; VarExp "Y"]), [TermExp ("parent_child", [VarExp "Z"; VarExp "X"]); TermExp ("parent_child", [VarExp "Z"; VarExp "Y"])]); Clause (TermExp ("father_child", [TermExp ("mike", []); TermExp ("tom", [])]), [TermExp ("true", [])]); Clause (TermExp ("father_child", [TermExp ("tom", []); TermExp ("erica", [])]), [TermExp ("true", [])]); Clause (TermExp ("father_child", [TermExp ("tom", []); TermExp ("sally", [])]), [TermExp ("true", [])]); Clause (TermExp ("mother_child", [TermExp ("trude", []); TermExp ("sally", [])]), [TermExp ("true", [])])],
                        []
                    )
                  (String.Set.of_list ["Z"; "E"])
                )
                [VarExp "Z"; VarExp "E"] 2
            ),
            "====================
E = sally
Z = sally
====================
====================
E = tom
Z = tom
====================
====================
E = erica
Z = erica
====================
====================
E = sally
Z = erica
====================
====================
E = erica
Z = sally
====================
====================
E = sally
Z = sally
====================
true
";

            (
                string_of_res
                (eval_query
                    (
                        [TermExp("animal", [VarExp "X"; VarExp "Y"])],
                        [Clause (TermExp ("animal", [VarExp "X"; VarExp "Y"]), [TermExp ("cat", [VarExp "X"])]); Clause (TermExp ("cat", [TermExp ("tom", [])]), [TermExp ("true", [])])],
                        []
                    )
                  (String.Set.of_list ["X"; "Y"])
                )
                [VarExp "X"; VarExp "Y"] 2
            ), "====================\nY is free\nX = tom\n====================\ntrue\n";

            (
                string_of_res
                (eval_query
                    (
                        [TermExp("animal", [VarExp "X"; VarExp "Y"]); VarExp "Z"],
                        [Clause (TermExp ("animal", [VarExp "X"; VarExp "Y"]), [TermExp ("cat", [VarExp "X"])]); Clause (TermExp ("cat", [TermExp ("tom", [])]), [TermExp ("true", [])])],
                        []
                    )
                  (String.Set.of_list ["X"; "Y"; "Z"])
                )
                [VarExp "X"; VarExp "Y"; VarExp "Z"] 3
            ), "====================\nZ is free\nY is free\nX = tom\n====================\ntrue\n";

            (
                string_of_res
                (eval_query
                    (
                        [VarExp "X"],
                        [Clause (TermExp ("animal", [VarExp "X"; VarExp "Y"]), [TermExp ("cat", [VarExp "X"])]); Clause (TermExp ("cat", [TermExp ("tom", [])]), [TermExp ("true", [])])],
                        []
                    )
                  (String.Set.of_list ["X"])
                )
                [VarExp "X"] 1
            ), "====================\nX is free\n====================\ntrue\n";

            (
                string_of_res
                (eval_query
                    (
                        [TermExp("animal", [VarExp "X"; VarExp "Y"]); VarExp "Z"],
                        [Clause (TermExp ("animal", [VarExp "X"; VarExp "Y"]), [TermExp ("cat", [VarExp "X"])]); Clause (TermExp ("cat", [TermExp ("tom", [])]), [TermExp ("true", [])])],
                        []
                    )
                  (String.Set.of_list ["X"; "Y"; "Z"])
                )
                [VarExp "X"; VarExp "Y"; VarExp "Z"] 3
            ), "====================\nZ is free\nY is free\nX = tom\n====================\ntrue\n";

            (
                string_of_res
                (eval_query
                    (
                        [TermExp("b", [TermExp("a", [TermExp("true",[])])])],
                        [Clause (TermExp("b",[VarExp "X"]), [TermExp("a", [VarExp "X"])]); Clause (TermExp("a",[TermExp("true",[])]), [TermExp ("true", [])])],
                        []
                    )
                  String.Set.empty
                )
                [] 0
            ), "false\n";

        ]
    )

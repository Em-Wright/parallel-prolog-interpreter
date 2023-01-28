open OUnit2
open Prolog_interpreter.Ast
open Prolog_interpreter.Util
open Prolog_interpreter.Evaluator


let identity_func s = s
let turn_to_unit _ = ()

let eval_query arg = let (res, _) = eval_query arg in res

let evaluator_test_suite =
    "Sequential Evaluator" >::: (
        List.map (
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
             fresh()
            ), "2";

            (turn_to_unit (fresh());
             turn_to_unit (fresh());
             turn_to_unit (reset());
             fresh()
            ), "1";


            (* Evaluating results of a query with a given db *)
            (string_of_res
                (eval_query
                    (
                        [],
                        [],
                        []
                    )
                )
                []
                0
            ), "true\n";

            (string_of_res
                (eval_query
                    (
                        [TermExp ("true", [])],
                        [],
                        []
                    )
                )
                []
                0
            ), "true\n";


            (string_of_res
                (eval_query
                    (
                        [TermExp ("male", [TermExp ("elizabeth", [])])],
                        [],
                        []
                    )
                )
                []
                0
            ), "false\n";

            (string_of_res
                (eval_query
                    (
                        [TermExp ("parent", [VarExp "X"; TermExp ("charles1", [])])],
                        [],
                        []
                    )
                )
                []
                0
            ), "false\n";

            (string_of_res
                (eval_query
                    (
                        [TermExp ("male", [TermExp ("elizabeth", [])])],
                        [Clause (TermExp("female", [TermExp("elizabeth", [TermExp ("true", [])])]), [])],
                        []
                    )
                )
                []
                0
            ), "false\n";

            (string_of_res
                (eval_query
                    (
                        [TermExp ("male", [TermExp ("elizabeth", [])])],
                        [Clause (TermExp("elizabeth", [TermExp("male", [])]), [TermExp ("true", [])])],
                        []
                    )
                )
                []
                0
            ), "false\n";

            (string_of_res
                (eval_query
                    (
                        [TermExp ("female", [TermExp ("elizabeth", [])])],
                        [Clause (TermExp("female", [TermExp("elizabeth", [])]), [TermExp ("true", [])])],
                        []
                    )
                )
                []
                0
            ), "true\n";

            (string_of_res
                (eval_query
                    (
                        [TermExp ("female", [TermExp ("elizabeth", [])])],
                        [Clause (TermExp("female", [TermExp("elizabeth", [])]), [TermExp("true", [])])],
                        []
                    )
                )
                []
                0
            ), "true\n";

            (string_of_res
                (eval_query
                    (
                        [TermExp ("female", [TermExp ("elizabeth", [])])],
                        [Clause (TermExp("female", [TermExp("elizabeth", [])]), [TermExp("true", [])])],
                        []
                    )
                )
                []
                0
            ), "true\n";

            (string_of_res
                (eval_query
                    (
                        [TermExp ("male", [TermExp ("elizabeth", [])])],
                        [Query([TermExp ("male", [TermExp ("elizabeth", [])])]);
                         Clause (TermExp("female", [TermExp("elizabeth", [])]), [TermExp("true", [])])],
                        []
                    )
                )
                []
                0
            ), "false\n";

            (string_of_res
                (eval_query
                    (
                        [TermExp("age", [TermExp("zaid",[]); VarExp "Y"])],
                        [],
                        []
                    )
                )
                [VarExp "Y"]
                1
            ), "false\n";

            (string_of_res
                (eval_query
                    (
                        [TermExp("age", [TermExp("zaid",[]); VarExp "Y"])],
                        [Clause (TermExp ("age", [ TermExp ("adam", []);
                              IntExp 10]), [TermExp ("true", [])])],
                        []
                    )
                )
                [VarExp "Y"]
                1
            ), "false\n";


            (string_of_res
                (eval_query
                    (
                        [TermExp("age", [VarExp "E"; VarExp "Z"])],
                        [Clause (TermExp ("age", [TermExp ("adam", []);
                              IntExp 10]), [TermExp ("true", [])]);Clause (TermExp ("age", [TermExp ("zaid", []);  (IntExp 5)]), [TermExp ("true", [])])],
                        []
                    )
                )
                [VarExp "Z"; VarExp "E"]
                2
            ), "====================\nE = adam\nZ = 10\n====================\n====================\nE = zaid\nZ = 5\n====================\ntrue\n";

            (string_of_res
                (eval_query
                    (
                        [TermExp("age", [VarExp "X";  (IntExp 5)])],
                        [Clause (TermExp ("age", [TermExp ("adam", []);
                            IntExp 10]), [TermExp ("true", [])]);Clause (TermExp ("age", [TermExp ("zaid", []);  (IntExp 5)]), [TermExp ("true", [])])],
                        []
                    )
                )
                [VarExp "X"]
                1
            ), "====================\nX = zaid\n====================\ntrue\n";

            (string_of_res
                (eval_query
                    (
                        [TermExp ("a", [])],
                        [Clause (TermExp ("a", []), [TermExp ("true", [])])],
                        []
                    )
                )
                []
                0
            ), "true\n";

            (string_of_res
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
               )
               [VarExp "X"]
               1
            ), "====================\nX = [1, 2]\n====================\ntrue\n";

            (string_of_res
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
               )
               [VarExp "Z"]
               1
            ), "====================\nZ = 1\n====================\ntrue\n";

            (string_of_res
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
               )
               [VarExp "Z"]
               1
            ), "====================\nZ = 10\n====================\ntrue\n";

            (string_of_res
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
               )
               [VarExp "Z"]
               1
            ), "====================\nZ = 5\n====================\ntrue\n";

            (string_of_res
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
               )
               [VarExp "Z"]
               1
            ), "====================\n\
                Z = 0\n\
                ====================\n\
                ====================\n\
                Z = 7\n\
                ====================\n\
                true\n";

            (string_of_res
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
               )
               [VarExp "Z"]
               1
            ), "====================\n\
                Z = 1\n\
                ====================\n\
                ====================\n\
                Z = 3\n\
                ====================\n\
                ====================\n\
                Z = 4\n\
                ====================\ntrue\n";

            (string_of_res
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
               )
               [VarExp "Z"]
               1
            ), "====================\n\
                Z = -1\n\
                ====================\n\
                ====================\n\
                Z = 3\n\
                ====================\n\
                true\n";

            (string_of_res
                (eval_query
                    (
                        [TermExp("age", [VarExp "X"; VarExp "Y"]); TermExp("female", [VarExp "X"])],
                        [Clause (TermExp ("age", [ TermExp("adam", []); IntExp 10]), [TermExp ("true", [])]);Clause (TermExp ("age", [TermExp ("zaid", []);  (IntExp 5)]), [TermExp ("true", [])]); Clause (TermExp ("age", [TermExp ("ann", []);  (IntExp 12)]), [TermExp ("true", [])]); Clause (TermExp ("male", [TermExp ("zaid", [])]), [TermExp ("true", [])]); Clause (TermExp ("male", [ TermExp("adam", [])]), [TermExp ("true", [])]); Clause (TermExp ("female", [TermExp ("ann",[])]),[TermExp ("true", [])])],
                        []
                    )
                )
                [VarExp "Y"; VarExp "X"]
                2
            ), "====================\nX = ann\nY = 12\n====================\ntrue\n";

            (string_of_res
                (eval_query
                    (
                        [TermExp("sibling", [TermExp("sally",[]); TermExp("erica",[])])],
                        [Clause (TermExp ("parent_child", [VarExp "X"; VarExp "Y"]), [TermExp ("mother_child", [VarExp "X"; VarExp "Y"])]); Clause (TermExp ("parent_child", [VarExp "X"; VarExp "Y"]), [TermExp ("father_child", [VarExp "X"; VarExp "Y"])]); Clause (TermExp ("sibling", [VarExp "X"; VarExp "Y"]), [TermExp ("parent_child", [VarExp "Z"; VarExp "X"]); TermExp ("parent_child", [VarExp "Z"; VarExp "Y"])]); Clause (TermExp ("father_child", [TermExp ("mike", []); TermExp ("tom", [])]), [TermExp ("true", [])]); Clause (TermExp ("father_child", [TermExp ("tom", []); TermExp ("erica", [])]), [TermExp ("true", [])]); Clause (TermExp ("father_child", [TermExp ("tom", []); TermExp ("sally", [])]), [TermExp ("true", [])]); Clause (TermExp ("mother_child", [TermExp ("trude", []); TermExp ("sally", [])]), [TermExp ("true", [])])],
                        []
                    )
                )
                []
                0
            ), "true\n";

            (string_of_res
                (eval_query
                    (
                        [TermExp("sibling", [VarExp "Z"; VarExp "E"])],
                        [Clause (TermExp ("parent_child", [VarExp "X"; VarExp "Y"]), [TermExp ("mother_child", [VarExp "X"; VarExp "Y"])]); Clause (TermExp ("parent_child", [VarExp "X"; VarExp "Y"]), [TermExp ("father_child", [VarExp "X"; VarExp "Y"])]); Clause (TermExp ("sibling", [VarExp "X"; VarExp "Y"]), [TermExp ("parent_child", [VarExp "Z"; VarExp "X"]); TermExp ("parent_child", [VarExp "Z"; VarExp "Y"])]); Clause (TermExp ("father_child", [TermExp ("mike", []); TermExp ("tom", [])]), [TermExp ("true", [])]); Clause (TermExp ("father_child", [TermExp ("tom", []); TermExp ("erica", [])]), [TermExp ("true", [])]); Clause (TermExp ("father_child", [TermExp ("tom", []); TermExp ("sally", [])]), [TermExp ("true", [])]); Clause (TermExp ("mother_child", [TermExp ("trude", []); TermExp ("sally", [])]), [TermExp ("true", [])])],
                        []
                    )
                )
                [VarExp "E"; VarExp "Z"]
                2
            ),
            "====================
Z = sally
E = sally
====================
====================
Z = tom
E = tom
====================
====================
Z = erica
E = erica
====================
====================
Z = erica
E = sally
====================
====================
Z = sally
E = erica
====================
====================
Z = sally
E = sally
====================
true
";

            (string_of_res
                (eval_query
                    (
                        [TermExp("animal", [VarExp "X"; VarExp "Y"])],
                        [Clause (TermExp ("animal", [VarExp "X"; VarExp "Y"]), [TermExp ("cat", [VarExp "X"])]); Clause (TermExp ("cat", [TermExp ("tom", [])]), [TermExp ("true", [])])],
                        []
                    )
                )
                [VarExp "Y"; VarExp "X"]
                2
            ), "====================\nX = tom\nY is free\n====================\ntrue\n";

            (string_of_res
                (eval_query
                    (
                        [TermExp("animal", [VarExp "X"; VarExp "Y"]); VarExp "Z"],
                        [Clause (TermExp ("animal", [VarExp "X"; VarExp "Y"]), [TermExp ("cat", [VarExp "X"])]); Clause (TermExp ("cat", [TermExp ("tom", [])]), [TermExp ("true", [])])],
                        []
                    )
                )
                [VarExp "Z"; VarExp "Y"; VarExp "X"]
                3
            ), "====================\nX = tom\nY is free\nZ is free\n====================\ntrue\n";

            (string_of_res
                (eval_query
                    (
                        [VarExp "X"],
                        [Clause (TermExp ("animal", [VarExp "X"; VarExp "Y"]), [TermExp ("cat", [VarExp "X"])]); Clause (TermExp ("cat", [TermExp ("tom", [])]), [TermExp ("true", [])])],
                        []
                    )
                )
                [VarExp "X"]
                1
            ), "====================\nX is free\n====================\ntrue\n";

            (string_of_res
                (eval_query
                    (
                        [TermExp("animal", [VarExp "X"; VarExp "Y"]); VarExp "Z"],
                        [Clause (TermExp ("animal", [VarExp "X"; VarExp "Y"]), [TermExp ("cat", [VarExp "X"])]); Clause (TermExp ("cat", [TermExp ("tom", [])]), [TermExp ("true", [])])],
                        []
                    )
                )
                [VarExp "Z"; VarExp "Y"; VarExp "X"; IntExp 10; TermExp("blah", [])]
                3
            ), "====================\nX = tom\nY is free\nZ is free\n====================\ntrue\n";

            (string_of_res
                (eval_query
                    (
                        [TermExp("animal", [VarExp "X"; VarExp "Y"]); VarExp "Z"],
                        [Clause (TermExp ("animal", [VarExp "X"; VarExp "Y"]), [TermExp ("cat", [VarExp "X"])]); Clause (TermExp ("cat", [TermExp ("tom", [])]), [TermExp ("true", [])])],
                        [(VarExp "X", TermExp("eh",[VarExp "X"]))]
                    )
                )
                [VarExp "Z"; VarExp "Y"; VarExp "X"; IntExp 10; TermExp("blah", [])]
                3
            ), "false\n";

            (string_of_res
                (eval_query
                    (
                        [TermExp("b", [TermExp("a", [TermExp("true",[])])])],
                        [Clause (TermExp("b",[VarExp "X"]), [TermExp("a", [VarExp "X"])]); Clause (TermExp("a",[TermExp("true",[])]), [TermExp ("true", [])])],
                        []
                    )
                )
                []
                0
            ), "false\n";

            (string_of_res
               (eval_query
                  (
                    [TermExp("fib", [IntExp 5; VarExp "X"])],
                    [
                      Clause (TermExp("fib", [IntExp 0; IntExp 1]), [ TermExp ("cut", [])]);
                      Clause (TermExp("fib", [IntExp 1; IntExp 1]), [ TermExp ("cut", [])]);
                      Clause (TermExp("fib", [VarExp "N"; VarExp "M"]), [
                          TermExp("is", [VarExp "N1"; ArithmeticExp(MINUS, ArithmeticVar "N", ArithmeticInt 1)]);
                          TermExp("is", [VarExp "N2"; ArithmeticExp(MINUS, ArithmeticVar "N", ArithmeticInt 2)]);
                          TermExp("fib", [VarExp "N1"; VarExp "K1"]);
                          TermExp("fib", [VarExp "N2"; VarExp "K2"]);
                          TermExp("is", [VarExp "M"; ArithmeticExp(PLUS, ArithmeticVar "K1", ArithmeticVar "K2")])
                        ]);
                    ],
                    []
                  )
               )
               []
               0
            ), "====================\nX = 8\n====================\ntrue\n";
        ]
    )

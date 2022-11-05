open OUnit2
open Prolog_interpreter.Ast
open Prolog_interpreter.Common


let parser_test_suite =
    "Parser" >::: (
        List.map (
            fun (arg, res) ->
                let title =
                    arg
                in
                title >:: (
                    fun _test_ctxt ->
                        assert_equal
                        ~printer:string_of_dec
                        res (parse arg)
                )
        )
        [
            (* Facts *)
            "cat.", (
                Clause (TermExp ("cat", []), [TermExp ("true", [])])
            );
            "cat().", (
                Clause (TermExp ("cat", []), [TermExp ("true", [])])
            );
            "cat(tom).", (
                Clause (
                    TermExp (
                        "cat", [TermExp ("tom", [])]
                    ), [
                        TermExp ("true", [])
                    ]
                )
            );
            "cat(tom()).", (
                Clause (
                    TermExp (
                        "cat", [TermExp ("tom", [])]
                    ), [
                        TermExp ("true", [])
                    ]
                )
            );
            "cat(X).", (
                Clause (
                    TermExp (
                        "cat", [VarExp "X"]
                    ),
                    [
                        TermExp ("true", [])
                    ]
                )
            );
            "len([],0).", (
              Clause (
                TermExp (
                  "len", [
                    TermExp (
                      "empty_list", []
                    );
                    IntExp 0
                  ]
                ),
                [
                  TermExp ("true", [])
                ]
              )
            );
            "l(H, T, [H|T]).", (
              Clause (
                TermExp (
                  "l", [
                    VarExp "H";
                    VarExp "T";
                    TermExp (
                      "list", [
                        VarExp "H";
                        VarExp "T"
                      ]
                    )
                  ]
                ), [
                  TermExp ("true", [])
                ]
              )
            );
            "coord(X, Y, Z).", (
                Clause (
                    TermExp (
                        "coord", [
                            VarExp "X";
                            VarExp "Y";
                            VarExp "Z"
                        ]
                    ), [
                        TermExp ("true", [])
                    ]
                )
            );
            "coord(1, 2, 3).", (
                Clause (
                    TermExp (
                        "coord", [
                            (IntExp 1);
                            (IntExp 2);
                            (IntExp 3)
                        ]
                    ), [
                        TermExp ("true", [])
                    ]
                )
            );

            (* Rules *)
            "cat :- true.", (
                Clause (TermExp ("cat", []), [TermExp ("true", [])])
            );
            "animal(X) :- cat(X).", (
                Clause (
                    TermExp (
                        "animal", [VarExp "X"]
                    ), [
                        TermExp ("cat", [VarExp "X"])
                    ]
                )
            );
            "len( [A, B | T], N) :- len(T, M), N is M + 2.", (
              Clause (
                TermExp (
                  "len", [
                    TermExp (
                      "list", [
                        VarExp "A";
                        TermExp (
                          "list", [
                            VarExp "B";
                            VarExp "T"
                          ]
                        )
                      ]
                    );
                    VarExp "N"
                  ]
                ), [
                  TermExp (
                    "len", [
                      VarExp "T";
                      VarExp "M"
                    ]
                  );
                  TermExp (
                    "is", [
                      VarExp "N";
                      ArithmeticExp (
                        PLUS,
                        ArithmeticVar "M",
                        ArithmeticInt 2
                      )
                    ]
                  )
                ]
              )
            );
            "len([H|T], N) :- len(T, M), N is M + 1.", (
              Clause (
                TermExp (
                  "len", [
                    TermExp (
                      "list", [
                        VarExp "H";
                        VarExp "T"
                      ]
                    );
                    VarExp "N"
                  ]
                ), [
                TermExp (
                  "len", [
                    VarExp "T";
                    VarExp "M"
                  ]
                );
                TermExp (
                  "is", [
                    VarExp "N";
                    ArithmeticExp (
                      PLUS,
                      ArithmeticVar "M",
                      ArithmeticInt 1
                    )
                  ]
                )
                ]
              )
            );
            "sibling(X, Y) :- parent_child(Z, X), parent_child(Z, Y).", (
                Clause (
                    TermExp (
                        "sibling", [VarExp "X"; VarExp "Y"]
                    ), [
                        TermExp (
                            "parent_child", [VarExp "Z"; VarExp "X"]
                        );
                        TermExp (
                            "parent_child", [VarExp "Z"; VarExp "Y"]
                        )
                    ]
                )
            );
            "nonsense_words :- foo, bar, baz.", (
                Clause (
                    TermExp (
                        "nonsense_words", []
                    ), [
                        TermExp (
                            "foo", []
                        );
                        TermExp (
                            "bar", []
                        );
                        TermExp (
                            "baz", []
                        )
                    ]
                )
            );
            "arithmetic_expression(X, Y) :- is(X, Y + 1).",
                Clause (
                   TermExp ("arithmetic_expression", [VarExp "X"; VarExp "Y"]),
                   [TermExp ("is", [
                        VarExp "X";
                        ArithmeticExp (PLUS,
                                      ArithmeticVar "Y",
                                      ArithmeticInt 1)
                      ])]
              );
            "arithmetic_expression_infix(X, Y) :- X is Y * -3.",
            Clause (
              TermExp ("arithmetic_expression_infix", [VarExp "X"; VarExp "Y"]),
              [TermExp ("is", [
                   VarExp "X";
                   ArithmeticExp (MULT,
                                  ArithmeticVar "Y",
                                  ArithmeticInt (-3))
                 ])]
            );
            "equals_infix(X, Y) :- X = Y.",
            Clause (
              TermExp ("equals_infix", [VarExp "X"; VarExp "Y"]),
              [TermExp ("equals", [
                   VarExp "X";
                   VarExp "Y"
                 ])]
            );
            "equals_infix(X) :- X = 2.",
            Clause (
              TermExp ("equals_infix", [VarExp "X"]),
              [TermExp ("equals", [
                   VarExp "X";
                   IntExp 2
                 ])]
            );
            "neq(X) :- 1 != 2.",
            Clause (
              TermExp ("neq", [VarExp "X"]),
              [TermExp ("not_equal", [
                   IntExp 1;
                   IntExp 2
                 ])]
            );
            "gt(X) :- X > 2.",
            Clause (
              TermExp ("gt", [VarExp "X"]),
              [TermExp ("greater_than", [
                   VarExp "X";
                   IntExp 2
                 ])]
            );
            "lt(X) :- X < 2.",
            Clause (
              TermExp ("lt", [VarExp "X"]),
              [TermExp ("less_than", [
                   VarExp "X";
                   IntExp 2
                 ])]
            );


            (* Queries *)
            "?- cat(tom).", (
                Query ([TermExp ("cat", [TermExp ("tom", [])])])
            );
            "?- cat(X).", (
                Query ([TermExp ("cat", [VarExp "X"])])
            );
            "?- sibling(sally, erica).", (
                Query ([
                    TermExp (
                        "sibling", [
                            TermExp ("sally", []);
                            TermExp ("erica", [])
                        ]
                    )
                ])
            );
            "?- sibling(sally, erica), sibling(john, joe).", (
                Query ([
                   TermExp (
                       "sibling", [
                           TermExp ("sally", []);
                           TermExp ("erica", [])
                       ]
                   );
                   TermExp (
                       "sibling", [
                           TermExp ("john", []);
                           TermExp ("joe", [])
                       ]
                   )
                ])
            );
            "?- len([2],1).", (
              Query ([
                TermExp (
                  "len", [
                    TermExp("list", [
                        IntExp 2;
                        TermExp("empty_list", [])
                      ]);
                    (IntExp 1);
                  ]
                )
              ])
            );

            (* Combinations *)
            "cat(tom). animal(X) :- cat(X). ?- animal(X).", (
                Clause (
                    TermExp (
                        "cat", [
                            TermExp ("tom", [])
                        ]
                    ), [
                        TermExp ("true", [])
                    ]
                )
            );
        ]
    )

let parser_failure_test_suite =
    "Parser_failure" >::: (
        List.map (
            fun arg ->
                let title =
                    arg
                in
                title >:: (
                    fun _test_ctxt ->
                        assert_equal
                        None (try_parse arg)
                )
        )
        [
            (* Empty string *)
            "";

            (* Constants *)
            "9";
            "VAR";

            (* Facts *)
            ".";
            "cat";
            "cat 9";
            "cat,";
            "cat:-";
            "cat((";
            "cat(X.";
            "cat(, X).";
            "(cat).";
            "cat, dog.";
            "coord(X, Y, Z)";
            "coord(X, Y, Z.";
            "coord X, Y, Z).";
            "coord X, Y, Z.";
            "coord(X Y Z).";
            "coord(X, Y, Z, ).";
            "coord(, X, Y, Z).";
            "VAR().";

            (* Rules *)
            ":-";
            ":- cat(X).";
            "cat(X) :-.";
            "cat() :- cat() cat().";
            "parent_child(Z, X), parent_child(Z, Y) :- sibling(X, Y).";

            (* Queries *)
            "?-";
            "?- 9.";
            "cat(tom) ?-";
            "cat(tom) ?- mouse(jerry).";
            "cat(tom), dog(spike) ?- mouse(jerry).";
        ]
    )

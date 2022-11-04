open OUnit2
open Sequential_interpreter.Ast
open Sequential_interpreter.Common
open Sequential_interpreter.Util

let identity_func s = s
let turn_to_unit _ = ()

let util_test_suite =
  "Util" >::: (
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
        
        (* Finding variables in declarations *)
        (string_of_exp_list
           (find_vars
              ([VarExp "X"; IntExp 10; TermExp("blah",[]); ArithmeticExp (PLUS, (ArithmeticVar "Y"), (ArithmeticInt 1))])
           )
        ), "[VarExp \"X\"; VarExp \"Y\"]";
        
        (string_of_exp_list
           (find_vars
              ([VarExp "X"; IntExp 10; TermExp("blah",[VarExp "X"; VarExp "Y"])])
           )
        ), "[VarExp \"X\"; VarExp \"X\"; VarExp \"Y\"]";
        
        (* Finding unique members (in this case variables) in a list *)
        (string_of_exp_list
           (uniq
              ([VarExp "X"; VarExp "X"; VarExp "Y"])
           )
        ), "[VarExp \"Y\"; VarExp \"X\"]";
        
        (* Lifting a goal with a substituion *)
        (string_of_exp
           (sub_lift_goal
              ([(VarExp "X", VarExp "1")])
              (VarExp "X")
           )
        ), "VarExp \"1\"";
        
        (string_of_exp
           (sub_lift_goal
              ([(VarExp "X", VarExp "1")])
              (VarExp "Y")
           )
        ), "VarExp \"Y\"";
        
        (string_of_exp
           (sub_lift_goal
              ([(VarExp "X", IntExp 7)])
              (ArithmeticExp(PLUS, ArithmeticVar "X", ArithmeticInt 1) )
           )
        ), "Arithmetic (PLUS, ArithmeticInt 7, ArithmeticInt 1)"
        ;
        
        (string_of_exp
                (sub_lift_goal
                   ([(VarExp "X", VarExp "1")])
                   (IntExp 10)
                )
        ), "IntExp 10";
        
        (* Lifting goals with a substitution *)
        (string_of_exp_list
           (sub_lift_goals
              ([(VarExp "X", VarExp "1")])
              ([VarExp("X"); IntExp 10; TermExp("blah", [VarExp "X"; VarExp "Y";IntExp 1]);
                ArithmeticExp(PLUS, ArithmeticVar "X", ArithmeticInt 2)])
           )
        ), "[VarExp \"1\"; IntExp 10; TermExp (\"blah\", [VarExp \"1\"; VarExp \"Y\"; IntExp 1]); \
            Arithmetic (PLUS, ArithmeticVar \"1\", ArithmeticInt 2)]";
        
        (string_of_exp_list
           (sub_lift_goals
              ([])
              ([VarExp("X"); IntExp 10; TermExp("blah", [VarExp "X"; VarExp "Y"; IntExp 1])])
           )
        ), "[VarExp \"X\"; IntExp 10; TermExp (\"blah\", [VarExp \"X\"; VarExp \"Y\"; IntExp 1])]";
        
        (string_of_exp_list
           (sub_lift_goals
              ([(VarExp "X", VarExp "1"); (VarExp "Z", VarExp "blu")])
              ([VarExp("X"); IntExp 10; TermExp("blah", [VarExp "X"; VarExp "Y"; IntExp 1])])
           )
        ), "[VarExp \"1\"; IntExp 10; TermExp (\"blah\", [VarExp \"1\"; VarExp \"Y\"; IntExp 1])]";
        
        (* Renaming variables in a declaration*)
        (string_of_dec
           (rename_vars_in_dec
              (Clause(TermExp("age",[TermExp("zaid",[]);IntExp 10 ]), [(IntExp 1)]))
           )
        ), "Clause (TermExp (\"age\", [TermExp (\"zaid\", []); IntExp 10]), [IntExp 1])";
        
        (turn_to_unit (reset());
         string_of_dec
           (rename_vars_in_dec
              (Clause (TermExp ("sibling", [VarExp "X"; VarExp "Y"]), [TermExp ("parent_child", [VarExp "Z"; VarExp "X"]); TermExp ("parent_child", [VarExp "Z"; VarExp "Y"])]))
           )
        ), "Clause (TermExp (\"sibling\", [VarExp \"3\"; VarExp \"2\"]), [TermExp (\"parent_child\", [VarExp \"1\"; VarExp \"3\"]); TermExp (\"parent_child\", [VarExp \"1\"; VarExp \"2\"])])";
        
        (string_of_dec
           (rename_vars_in_dec
              (Query ([TermExp ("age", [TermExp ("zaid", [])])]))
           )
        ), "Query ([TermExp (\"age\", [TermExp (\"zaid\", [])])])";
        
        (turn_to_unit (reset());
         string_of_dec
                (rename_vars_in_dec
                   (Query ([TermExp ("parent", [VarExp "X"; VarExp "Y"]); TermExp ("male", [VarExp "X"]);
                            ArithmeticExp(PLUS, ArithmeticVar "X", ArithmeticVar "Z")]))
                )
        ), "Query ([TermExp (\"parent\", [VarExp \"3\"; VarExp \"2\"]); TermExp (\"male\", [VarExp \"3\"]); Arithmetic (PLUS, ArithmeticVar \"3\", ArithmeticVar \"1\")])";
        
        (* Pairandcat function for handling decompose case of unification *)
        (* TODO - do I need to add cases for arithmetic expressions in here? *)
        (string_of_subs
           (pairandcat
              ([TermExp ("trude", []); TermExp ("sally", [])])
              ([VarExp "X"; VarExp "Y"])
              ([])
           )
        ), "[(TermExp (\"sally\", []), VarExp \"Y\"); (TermExp (\"trude\", []), VarExp \"X\")]";
        
        (string_of_subs
           (pairandcat
              ([])
              ([])
              ([(VarExp "Z", IntExp 10)])
           )
        ), "[(VarExp \"Z\", IntExp 10)]";
        
        (string_of_subs
           (pairandcat
              ([TermExp ("trude", []); TermExp ("sally", [])])
              ([VarExp "X"; VarExp "Y"])
              ([(VarExp "Z", IntExp 10)])
           )
        ), "[(TermExp (\"sally\", []), VarExp \"Y\"); (TermExp (\"trude\", []), VarExp \"X\"); (VarExp \"Z\", IntExp 10)]";
        
        (try
           string_of_subs
             (pairandcat
                ([VarExp "X"; VarExp "Y"])
                ([])
                ([(VarExp "Z", IntExp 10)])
             )
         with Failure s -> s
        ), "sargs and targs should be the same length";
        
        (try
           string_of_subs
             (pairandcat
                ([])
                ([VarExp "X"; VarExp "Y"])
                ([(VarExp "Z", IntExp 10)])
             )
         with Failure s -> s
        ), "sargs and targs should be the same length";
        
        (* replace function for the elimination case of unification *)
        (* TODO - do I need to add cases for arithmetic expressions in here? *)
        (string_of_subs
           (replace
              ([(VarExp "Z", IntExp 10)])
              ([])
           )
        ), "[(VarExp \"Z\", IntExp 10)]";

        (string_of_subs
           (replace
              ([(VarExp "Z", IntExp 10)])
                    ([(VarExp "X", VarExp "1")])
           )
        ), "[(VarExp \"Z\", IntExp 10)]";

        (string_of_subs
           (replace
              ([(VarExp "Z", IntExp 10)])
              ([(VarExp "Z", VarExp "1")])
           )
        ), "[(VarExp \"1\", IntExp 10)]";

        (string_of_subs
           (replace
              ([])
              ([(VarExp "X", VarExp "1")])
           )
        ), "[]";

        (string_of_subs
           (replace
              ([])
              ([])
           )
            ), "[]";

        (string_of_subs
           (replace
              ([(VarExp "Z", IntExp 10); (VarExp "X", TermExp("blah", [VarExp "X"; VarExp "Z"]))])
              ([(VarExp "Z", VarExp "1"); (VarExp "X", TermExp("and",[]))])
           )
        ), "[(VarExp \"1\", IntExp 10); (TermExp (\"and\", []), TermExp (\"blah\", [TermExp (\"and\", []); VarExp \"1\"]))]";

        (* occurs function for elimination case of unification *)
        (string_of_bool
           (occurs
              ("1")
              (TermExp ("name", []))
           )
        ), "false";

        (string_of_bool
           (occurs
              ("1")
              (VarExp "X")
           )
        ), "false";

        (string_of_bool
           (occurs
              ("1")
              (VarExp "1")
           )
        ), "true";

        (string_of_bool
           (occurs
              ("1")
              (TermExp ("1",[VarExp"10"; TermExp("blah", []);IntExp 1]))
           )
        ), "false";

        (string_of_bool
           (occurs
              ("1")
              (TermExp ("1",[VarExp"1"; TermExp("blah", []);IntExp 1]))
           )
        ), "true";

            (string_of_bool
               (occurs
                  ("1")
                  (ArithmeticExp (MINUS, ArithmeticVar "1", ArithmeticInt 7))
               )
            ), "true";
            (string_of_bool
               (occurs
                  ("1")
                  (ArithmeticExp (MINUS, ArithmeticInt 1, ArithmeticInt 7))
               )
            ), "false";
            (string_of_bool
               (occurs
                  ("1")
                  (ArithmeticExp (MINUS, ArithmeticVar "X", ArithmeticInt 1))
               )
            ), "false";

            (string_of_bool
                (occurs
                    ("1")
                    (TermExp ("1",[VarExp"10"; TermExp("blah", [VarExp "1"]);IntExp 1]))
                )
            ), "true";

            (* Unification *)
            (string_of_unify_res
                (unify
                    ([])
                )
            ), "[]";

            (string_of_unify_res
                (unify
                    ([(VarExp "X", VarExp "X")])
                )
            ), "[]";

            (string_of_unify_res
                (unify
                    ([( IntExp 10, IntExp 10)])
                )
             ), "[]";

            (string_of_unify_res
                (unify
                    ([(VarExp "X", TermExp("blah", [VarExp "X"]))])
                )
            ), "None";
            (string_of_unify_res
               (unify
                  ([(VarExp "X", ArithmeticExp(PLUS, ArithmeticVar "X", ArithmeticInt 2))])
               )
            ), "None";

            (string_of_unify_res
               (unify
                  ([( ArithmeticExp(PLUS, ArithmeticVar "Y", ArithmeticInt 2)), VarExp "X"])
               )
            ), "[(VarExp \"X\", Arithmetic (PLUS, ArithmeticVar \"Y\", ArithmeticInt 2))]";
            (string_of_unify_res
               (unify
                  ([(VarExp "X", ArithmeticExp(PLUS, ArithmeticVar "Y", ArithmeticInt 2))])
               )
            ), "[(VarExp \"X\", Arithmetic (PLUS, ArithmeticVar \"Y\", ArithmeticInt 2))]";

            (string_of_unify_res
                (unify
                    ([(VarExp "X", TermExp("blah", [TermExp("and", [])]))])
                )
            ), "[(VarExp \"X\", TermExp (\"blah\", [TermExp (\"and\", [])]))]";

            (string_of_unify_res
                (unify
                    ([(VarExp "X", TermExp("blah", [TermExp("and", [])])); (VarExp "Z", TermExp("blah", [VarExp "X"; VarExp "Z"]))])
                )
            ), "None";

            (string_of_unify_res
                (unify
                    ([(VarExp "X", TermExp("blah", [TermExp("and", [])])); (VarExp "Z", TermExp("blah", [VarExp "X"]))])
                )
            ), "[(VarExp \"X\", TermExp (\"blah\", [TermExp (\"and\", [])])); (VarExp \"Z\", TermExp (\"blah\", [TermExp (\"blah\", [TermExp (\"and\", [])])]))]";

            (string_of_unify_res
                (unify
                    ([(TermExp("blah", [TermExp("and", [])]), VarExp "X")])
                )
            ), "[(VarExp \"X\", TermExp (\"blah\", [TermExp (\"and\", [])]))]";

            (string_of_unify_res
                (unify
                    ([(TermExp("blah", [VarExp "X"]), TermExp("hah", []))])
                )
            ), "None";

            (string_of_unify_res
                (unify
                    ([(TermExp("blah", [VarExp "X"]), TermExp("hah", [VarExp "Z"]))])
                )
            ), "None";

            (string_of_unify_res
                (unify
                    ([(TermExp("blah", [VarExp "X"]), TermExp("blah", []))])
                )
            ), "None";

            (string_of_unify_res
                (unify
                    ([(TermExp("blah", [IntExp 10]), TermExp("blah", [VarExp "X"]))])
                )
            ), "[(VarExp \"X\", IntExp 10)]";

            (string_of_unify_res
                (unify
                    ([(TermExp("blah", [TermExp("hah", [])]), TermExp("blah", [VarExp "X"]))])
                )
            ), "[(VarExp \"X\", TermExp (\"hah\", []))]";

            (string_of_unify_res
                (unify
                    ([(TermExp("blah", [VarExp "X"]), IntExp 10)])
                )
            ), "None";

            (string_of_unify_res
                (unify
                    ([( IntExp 10, TermExp("blah", []))])
                )
            ), "None";

            (string_of_unify_res
                (unify
                    ([( IntExp 10, VarExp "X")])
                )
            ), "[(VarExp \"X\", IntExp 10)]";

            (string_of_unify_res
                (unify
                    ([( IntExp 10,  IntExp 100)])
                )
            ), "None";

            (string_of_unify_res
               (unify
                  ([( IntExp 10,  IntExp 10)])
               )
            ), "[]";

            (string_of_unify_res
                (unify
                    ([(TermExp("sibling", [VarExp "1"; VarExp "2"]), TermExp("sibling", [VarExp "X"; VarExp "Y"]))])
                )
            ), "[(VarExp \"2\", VarExp \"Y\"); (VarExp \"1\", VarExp \"X\")]";

            (* Adding declarations to db *)
            (string_of_db
                (add_dec_to_db
                    (
                        Clause (TermExp ("cat", [TermExp ("tom", [])]), [TermExp ("true", [])]),
                        []
                    )
                )
            ), "[Clause (TermExp (\"cat\", [TermExp (\"tom\", [])]), [TermExp (\"true\", [])])]";

            (string_of_db
                (add_dec_to_db
                    (
                        Clause (TermExp ("cat", [TermExp ("tom", [])]), [TermExp ("true", [])]),
                        []
                    )
                )
            ), "[Clause (TermExp (\"cat\", [TermExp (\"tom\", [])]), [TermExp (\"true\", [])])]";

            (string_of_db
                (add_dec_to_db
                    (
                        Clause (TermExp ("true", []), [TermExp ("true", [])]),
                        []
                    )
                )
            ), "[]";

            (string_of_db
                (add_dec_to_db
                    (
                        Clause (TermExp ("true", [TermExp ("blah",[])]), [TermExp ("true", [])]),
                        []
                    )
                )
            ), "[]";

            (string_of_db
                (add_dec_to_db
                    (
                        Query ([TermExp ("parent", [VarExp "X"; TermExp ("charles1", [])]); TermExp ("male", [VarExp "X"])]),
                        []
                    )
                )
            ), "[Query ([TermExp (\"parent\", [VarExp \"X\"; TermExp (\"charles1\", [])]); TermExp (\"male\", [VarExp \"X\"])])]";


    ]
  )

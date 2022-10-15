open OUnit2
open Sequential_interpreter.Ast
open Sequential_interpreter.Common
open Sequential_interpreter.Parser


let string_of_string s = s

let common_test_suite =
    "Common" >::: (
        List.map (
            fun (arg, res) ->
                let title =
                    res
                in
                title >:: (
                    fun _test_ctxt ->
                        assert_equal
                        ~printer:string_of_string
                        res arg
                )
        )
        [
            (* Tokens *)
            string_of_token (INT 7),        "INT 7";
            string_of_token (ATOM "\t"),    "ATOM \"\\t\"";
            string_of_token (VAR "FOO"),    "VAR \"FOO\"";
            string_of_token RULE,           "RULE";
            string_of_token QUERY,          "QUERY";
            string_of_token PERIOD,         "PERIOD";
            string_of_token LPAREN,         "LPAREN";
            string_of_token RPAREN,         "RPAREN";
            string_of_token COMMA,          "COMMA";
            string_of_token EOF,            "EOF";

            string_of_token_list [
                ATOM "cat"; LPAREN; ATOM "tom"; RPAREN; PERIOD
            ], "[ATOM \"cat\"; LPAREN; ATOM \"tom\"; RPAREN; PERIOD]";

            (* Expressions *)
            string_of_exp (VarExp "X"),             "VarExp \"X\"";
            string_of_exp (IntExp 5),  "IntExp 5";
            string_of_exp (
                TermExp ("coord", [VarExp "X"; VarExp "Y"; VarExp "Z"])
            ), "TermExp (\"coord\", [VarExp \"X\"; VarExp \"Y\"; VarExp \"Z\"])";
            string_of_exp_list (
                [VarExp "X";  IntExp 10; TermExp ("blah", [VarExp "Y"; TermExp ("end", [])])]
            ), "[VarExp \"X\"; IntExp 10; TermExp (\"blah\", [VarExp \"Y\"; TermExp (\"end\", [])])]";


            (* Declarations *)
            string_of_dec (
                Clause (TermExp ("cat", []), [TermExp ("true", [])])
            ), "Clause (TermExp (\"cat\", []), [TermExp (\"true\", [])])";
            string_of_dec (
                Query ([TermExp ("cat", [TermExp ("tom", [])])])
            ), "Query ([TermExp (\"cat\", [TermExp (\"tom\", [])])])";

            (* Database *)
            string_of_db [
                Clause (TermExp ("foo", []), [TermExp ("true", [])]);
                Query ([TermExp ("bar", [])])
            ], "[Clause (TermExp (\"foo\", []), [TermExp (\"true\", [])]); Query ([TermExp (\"bar\", [])])]";

            (print_db [
                Clause (TermExp ("foo", []), [TermExp ("true", [])]);
                Query ([TermExp ("bar", [])])
               ]; "print_db"), "print_db";

            (* Readable Expression Strings *)
            readable_string_of_exp (VarExp "X"),             "X";
            readable_string_of_exp ( IntExp 5),  "5";
            readable_string_of_exp (
                TermExp ("coord", [VarExp "X"; VarExp "Y"; VarExp "Z"])
            ), "coord(X, Y, Z)";
            readable_string_of_exp (
                TermExp ("zaid", [])
            ), "zaid";

            (* Substitutions *)
            string_of_subs (
                []
            ), "[]";

            string_of_subs (
                [(VarExp "X", TermExp ("hah", []))]
            ), "[(VarExp \"X\", TermExp (\"hah\", []))]";

            string_of_subs (
                [(VarExp "X", TermExp ("hah", [])); (VarExp "Y",  IntExp 10)]
            ), "[(VarExp \"X\", TermExp (\"hah\", [])); (VarExp \"Y\", IntExp 10)]";

            string_of_unify_res (
                None
            ), "None";

            string_of_unify_res (
                Some([(VarExp "X", TermExp ("hah", [])); (VarExp "Y",  IntExp 10)])
            ), "[(VarExp \"X\", TermExp (\"hah\", [])); (VarExp \"Y\", IntExp 10)]";
        ]
    )

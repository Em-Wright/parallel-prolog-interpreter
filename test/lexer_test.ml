open OUnit2
open Sequential_interpreter.Common
open Sequential_interpreter.Lexer
open Sequential_interpreter.Parser


let lexer_test_suite =
    "Lexer" >::: (
        List.map (
            fun (arg, res) ->
                let title =
                    arg
                in
                title >:: (
                    fun _test_ctxt ->
                        assert_equal
                        ~printer:string_of_token_list
                        res (get_all_tokens arg)
                )
        )
        [
            (* Empty string *)
            "",                         [];
            "\n",                       [];
            "\t",                       [];

            (* Atoms *)
            "x",                        [ATOM "x"];
            "red",                      [ATOM "red"];
            "blueBook",                 [ATOM "blueBook"];
            "mother_child",             [ATOM "mother_child"];
            "'Taco'",                   [ATOM "Taco"];
            "'some atom'",              [ATOM "some atom"];
            "foobar123",                [ATOM "foobar123"];
            "'foo\"bar'",               [ATOM "foo\"bar"];
            "'foo\"\\'bar'",            [ATOM "foo\"'bar"];
            "' \\t\\n '",               [ATOM " \t\n "];
            "'\\a\\b\\f\\n\\r\\t\\v\\e\\d'", [
                ATOM "\007\b\012\n\r\t\011\027\127"
            ];
            "'\\\\'",                   [ATOM "\\"];
            "'\\\n'",                   [ATOM ""];
            "'\\c   \n   \n  '",        [ATOM ""];
            "'\\125\\111\\125\\103'",   [ATOM "UIUC"];
            "'\\x43\\\\x53\\'",         [ATOM "CS"];

            (* Numbers *)
            "1",        [INT 1];
            "39",       [INT 39];
            "-320",     [INT (-320)];

            (* Variables *)
            "Cats",     [VAR "Cats"];
            "_dogs",    [VAR "_dogs"];
            "FOOBAR",   [VAR "FOOBAR"];

            (* Symbols *)
            ":-",       [RULE];
            "?-",       [QUERY];
            ".",        [PERIOD];
            "(",        [LPAREN];
            ")",        [RPAREN];
            ",",        [COMMA];
            "+",        [PLUS];
            "-",        [MINUS];
            "*",        [MULT];
            "/",        [DIV];
            ">",        [GT];
            "<",        [LT];
            ":- ?- ()", [RULE; QUERY; LPAREN; RPAREN];

            (* Comments *)
            "cat(tom). % tom is a cat\nmouse(jerry). % jerry is a mouse", [
                ATOM "cat";   LPAREN; ATOM "tom";   RPAREN; PERIOD;
                ATOM "mouse"; LPAREN; ATOM "jerry"; RPAREN; PERIOD
            ];
            "this line /* contains a\nmulti-line */ comment.", [
                ATOM "this"; ATOM "line"; ATOM "comment"; PERIOD
            ];
            "this /* line /* contains /* several */ nested */ comments */ in a row", [
                ATOM "this"; ATOM "in"; ATOM "a"; ATOM "row"
            ];

            (* Combinations *)
            "cat(tom).", [
                ATOM "cat"; LPAREN; ATOM "tom"; RPAREN; PERIOD
            ];
            "cat(tom) :- true.", [
                ATOM "cat"; LPAREN; ATOM "tom"; RPAREN; RULE; ATOM "true"; PERIOD
            ];
            "cat(tom):-true.", [
                ATOM "cat"; LPAREN; ATOM "tom"; RPAREN; RULE; ATOM "true"; PERIOD
            ];
            "?- cat(tom).", [
                QUERY; ATOM "cat"; LPAREN; ATOM "tom"; RPAREN; PERIOD
            ];
            "?- cat(X).", [
                QUERY; ATOM "cat"; LPAREN; VAR "X"; RPAREN; PERIOD
            ];
            "?-cat(X).", [
                QUERY; ATOM "cat"; LPAREN; VAR "X"; RPAREN; PERIOD
            ];
            "maths(X, Y) :- is(Y, X + 1)", [
              ATOM "maths"; LPAREN; VAR "X"; COMMA; VAR "Y"; RPAREN; RULE; ATOM "is";
                    LPAREN; VAR "Y"; COMMA; VAR "X"; PLUS; INT 1; RPAREN
            ];
            "maths(X, Y) :- Y is X - 1", [
              ATOM "maths"; LPAREN; VAR "X"; COMMA; VAR "Y"; RPAREN; RULE; VAR "Y"; IS;
                    VAR "X"; MINUS; INT 1
            ];
            "maths(X, Y) :- Y is X * 1", [
              ATOM "maths"; LPAREN; VAR "X"; COMMA; VAR "Y"; RPAREN; RULE; VAR "Y"; IS;
              VAR "X"; MULT; INT 1
            ];
            "maths(X, Y) :- Y is X / -1", [
              ATOM "maths"; LPAREN; VAR "X"; COMMA; VAR "Y"; RPAREN; RULE; VAR "Y"; IS;
              VAR "X"; DIV; INT (-1)
            ];
            "eq(X, Y) :- X = Y", [
              ATOM "eq"; LPAREN; VAR "X"; COMMA; VAR "Y"; RPAREN; RULE; VAR "X"; EQUALS;
                        VAR "Y"
            ];
            "gt(X, Y) :- X > Y", [
              ATOM "gt"; LPAREN; VAR "X"; COMMA; VAR "Y"; RPAREN; RULE; VAR "X"; GT;
              VAR "Y"
            ];
            "lt(X, Y) :- X < Y", [
              ATOM "lt"; LPAREN; VAR "X"; COMMA; VAR "Y"; RPAREN; RULE; VAR "X"; LT;
              VAR "Y"
            ];
            "l(X, Y) :- [X | Y]", [
              ATOM "l"; LPAREN; VAR "X"; COMMA; VAR "Y"; RPAREN; RULE; LBRACKET; VAR "X"; PIPE; VAR "Y"; RBRACKET
            ];
            "l([H | T], Y).", [
              ATOM "l"; LPAREN; LBRACKET; VAR "H"; PIPE; VAR "T"; RBRACKET; COMMA; VAR "Y"; RPAREN; PERIOD
            ];
            "l([H1, H2 | T], Y).", [
              ATOM "l"; LPAREN; LBRACKET; VAR "H1"; COMMA; VAR "H2"; PIPE; VAR "T"; RBRACKET; COMMA; VAR "Y"; RPAREN; PERIOD
            ];
            "sibling(X, Y) :- parent_child(Z, X), parent_child(Z, Y).", [
                ATOM "sibling";      LPAREN; VAR "X"; COMMA; VAR "Y"; RPAREN; RULE;
                ATOM "parent_child"; LPAREN; VAR "Z"; COMMA; VAR "X"; RPAREN; COMMA;
                ATOM "parent_child"; LPAREN; VAR "Z"; COMMA; VAR "Y"; RPAREN; PERIOD
            ];
            "sibling(X,Y):-parent_child(Z,X),parent_child(Z,Y).", [
                ATOM "sibling";      LPAREN; VAR "X"; COMMA; VAR "Y"; RPAREN; RULE;
                ATOM "parent_child"; LPAREN; VAR "Z"; COMMA; VAR "X"; RPAREN; COMMA;
                ATOM "parent_child"; LPAREN; VAR "Z"; COMMA; VAR "Y"; RPAREN; PERIOD
            ];
        ]
    )

let lexer_failure_test_suite =
    "Lexer_failure" >::: (
        List.map (
            fun arg ->
                let title =
                    arg
                in
                title >:: (
                    fun _test_ctxt ->
                        assert_equal
                        None (try_get_all_tokens arg)
                )
        )
        [
            (* Comments *)
            "*/";
            "/* */ */";

            "/*";
            "/* /* */";

            (* Invalid characters *)
            "\r";
            "\b";
        ]
    )

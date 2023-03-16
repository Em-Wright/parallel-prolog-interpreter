open OUnit2
open Common_test
open Lexer_test
open Parser_test
open Evaluator_test
open Stack_evaluator_test
open Util_test
open Trail_util_test
open Trail_evaluator_test
(* open Worker_test *)


let suite = "suite" >::: [
    common_test_suite;
    lexer_test_suite;
    lexer_failure_test_suite;
    parser_test_suite;
    parser_failure_test_suite;
    util_test_suite;
    trail_util_test_suite;
    evaluator_test_suite;
    trail_evaluator_test_suite;
    stack_evaluator_test_suite;
    (* worker_test_suite; *)
]

let () = run_test_tt_main suite

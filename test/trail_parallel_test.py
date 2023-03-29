import subprocess

def run_test(command, expected_output, test_no):
    completed_process = subprocess.run(
        command,
        capture_output=True,
        text=True
    )
    res = completed_process.stdout.strip()
    if res == expected_output.strip():
        print ("test", test_no, "passed")
    else:
        print (res)
        print ("test", test_no, "FAILED")


# TEST 1
args = ["../bin/trail_parallel.exe", '-file', '../prolog_programs/test_nqueensgen.pl', '-num-workers', '6']
ans = """Welcome to the Prolog Interpreter

Opening file ../prolog_programs/test_nqueensgen.pl

?- n_queens(5, X).
===============
X = [5, 3, 1, 4, 2]
===============
===============
X = [5, 2, 4, 1, 3]
===============
===============
X = [4, 2, 5, 3, 1]
===============
===============
X = [4, 1, 3, 5, 2]
===============
===============
X = [3, 5, 2, 4, 1]
===============
===============
X = [3, 1, 4, 2, 5]
===============
===============
X = [2, 5, 3, 1, 4]
===============
===============
X = [2, 4, 1, 3, 5]
===============
===============
X = [1, 4, 2, 5, 3]
===============
===============
X = [1, 3, 5, 2, 4]
===============

File contents loaded.
"""

run_test(args, ans, 1)

# TEST 2
args = ["../bin/trail_parallel.exe", '-file', '../prolog_programs/test_perm.pl', '-num-workers', '6']
ans = """Welcome to the Prolog Interpreter

Opening file ../prolog_programs/test_perm.pl

?- perm([1,2,3], L).
===============
L = [1, 2, 3]
===============
===============
L = [1, 3, 2]
===============
===============
L = [2, 1, 3]
===============
===============
L = [2, 3, 1]
===============
===============
L = [3, 1, 2]
===============
===============
L = [3, 2, 1]
===============

File contents loaded.
"""

run_test(args, ans, 2)

# TEST 3
args = ["../bin/trail_parallel.exe", '-file', '../prolog_programs/test_fib.pl', '-num-workers', '6']
ans = """Welcome to the Prolog Interpreter

Opening file ../prolog_programs/test_fib.pl

?- fib(15, X).
===============
X = 987
===============

File contents loaded.
"""

run_test(args, ans, 3)


# TEST 4 - check cut works
args = ["../bin/trail_parallel.exe", '-file', '../prolog_programs/test_cut.pl', '-num-workers', '6']
ans = """Welcome to the Prolog Interpreter

Opening file ../prolog_programs/test_cut.pl

?- p(Y).
===============
Y = bess
===============
===============
Y = jack
===============

File contents loaded.
"""
run_test(args, ans, 4)

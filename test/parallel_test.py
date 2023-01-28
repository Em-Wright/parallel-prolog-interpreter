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
        print ("test", test_no, "FAILED")


# TEST 1
args = ["../bin/parallel.exe", '-file', '../prolog_programs/nqueensgen.pl', '-num-workers', '6']
ans =  """ Welcome to the Prolog Interpreter

Opening file ../prolog_programs/nqueensgen.pl

?- n_queens(5, X).

====================
X = [5, 3, 1, 4, 2]
====================
====================
X = [5, 2, 4, 1, 3]
====================
====================
X = [4, 2, 5, 3, 1]
====================
====================
X = [4, 1, 3, 5, 2]
====================
====================
X = [3, 5, 2, 4, 1]
====================
====================
X = [3, 1, 4, 2, 5]
====================
====================
X = [2, 5, 3, 1, 4]
====================
====================
X = [2, 4, 1, 3, 5]
====================
====================
X = [1, 4, 2, 5, 3]
====================
====================
X = [1, 3, 5, 2, 4]
====================
true




File contents loaded."""

run_test(args, ans, 1)

import csv


in_string = """./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  6.46s user 8.62s system 6% cpu 3:50.25 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  6.85s user 9.14s system 6% cpu 3:50.74 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  6.61s user 8.94s system 6% cpu 3:52.79 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  6.59s user 8.91s system 6% cpu 3:51.36 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  6.28s user 8.45s system 6% cpu 3:48.19 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  6.33s user 8.51s system 6% cpu 3:49.10 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  6.31s user 8.47s system 6% cpu 3:49.78 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  6.64s user 8.90s system 6% cpu 3:49.60 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  6.77s user 9.06s system 6% cpu 3:50.72 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  6.57s user 8.85s system 6% cpu 3:50.51 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  9.23s user 12.41s system 8% cpu 4:20.24 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  9.61s user 13.03s system 8% cpu 4:22.18 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  9.86s user 13.05s system 8% cpu 4:17.66 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  9.73s user 12.83s system 8% cpu 4:14.38 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  9.65s user 12.74s system 8% cpu 4:17.62 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  9.84s user 13.09s system 8% cpu 4:15.84 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  9.56s user 12.80s system 8% cpu 4:18.14 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  9.67s user 13.09s system 8% cpu 4:20.86 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  9.61s user 12.77s system 8% cpu 4:16.74 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  9.25s user 12.35s system 8% cpu 4:22.93 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  7.57s user 9.87s system 4% cpu 6:08.01 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  7.80s user 10.04s system 4% cpu 6:09.39 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  7.66s user 9.83s system 4% cpu 6:10.51 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  7.56s user 9.96s system 4% cpu 6:08.35 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  7.67s user 9.88s system 4% cpu 6:10.90 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  7.58s user 9.94s system 4% cpu 6:09.43 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  7.61s user 9.74s system 4% cpu 6:06.71 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  7.63s user 9.99s system 4% cpu 6:11.19 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  7.75s user 10.07s system 4% cpu 6:11.98 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  7.52s user 9.79s system 4% cpu 6:07.78 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  13.13s user 18.08s system 4% cpu 12:07.59 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  12.97s user 18.16s system 4% cpu 12:05.60 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  13.05s user 18.12s system 4% cpu 12:06.75 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  12.86s user 17.97s system 4% cpu 12:01.97 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  13.09s user 18.02s system 4% cpu 12:04.98 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  13.06s user 18.00s system 4% cpu 12:02.07 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  12.86s user 18.02s system 4% cpu 12:01.72 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  12.96s user 18.12s system 4% cpu 12:02.55 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  12.95s user 18.19s system 4% cpu 12:05.54 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  13.04s user 18.14s system 4% cpu 12:04.45 total
"""


print("8 workers")
par8 = []
for line in in_string.split("\n")[0:10]:
    s = line.split()
    par8.append(s[13])
    print(s[13])

print("\n\n6 workers")
par6 = []
for line in in_string.split("\n")[10:20]:
    s = line.split()
    par6.append(s[13])
    print(s[13])

print("\n\n4 workers")
par4 = []
for line in in_string.split("\n")[20:30]:
    s = line.split()
    par4.append(s[13])
    print( s[13])

print("\n\n2 workers")
par2 = []
for line in in_string.split("\n")[30:40]:
    s = line.split()
    par2.append(s[13])
    print( s[13])

# print("\n\nsequential")
# seq = []
# for line in in_string.split("\n")[120:150]:
#     s = line.split()
#     seq.append(s[12])
#     print( s[12])

# print("\n\ntrail")
# tr = []
# for line in in_string.split("\n")[150:180]:
#     s = line.split()
#     tr.append(s[12])
#     print( s[12])

with open("8queens.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(par8)
    writer.writerow(par6)
    writer.writerow(par4)
    writer.writerow(par2)
#     writer.writerow(seq)
#     writer.writerow(tr)


in_string2 = """Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.01s system 23% cpu 0.074 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 83% cpu 0.014 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 81% cpu 0.014 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 84% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 83% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 82% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 83% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 83% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 77% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 80% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 68% cpu 0.015 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 83% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 82% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 83% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 82% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 81% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 77% cpu 0.013 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 84% cpu 0.011 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 84% cpu 0.011 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 80% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 83% cpu 0.011 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 84% cpu 0.011 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 80% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 84% cpu 0.011 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 84% cpu 0.011 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 85% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 83% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 85% cpu 0.011 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 84% cpu 0.011 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_fib.pl > timings.txt  0.01s user 0.00s system 83% cpu 0.012 total"""

swipl = []
for line in in_string2.split("\n"):
    s = line.split(' ')
    if s[0] == "Warning:" or s[0]== "Warning:\xa0" or len(s) < 13:
        continue
    swipl.append(s[12])

with open("fibswi.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(swipl)

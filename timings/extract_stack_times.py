import csv

in_string = """ ./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.01s system 35% cpu 0.047 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 92% cpu 0.012 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 92% cpu 0.012 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 92% cpu 0.012 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.013 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.013 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 92% cpu 0.012 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.012 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.013 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 91% cpu 0.012 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 92% cpu 0.012 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.013 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 92% cpu 0.012 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 92% cpu 0.012 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 94% cpu 0.013 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 92% cpu 0.012 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 92% cpu 0.012 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 92% cpu 0.012 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 91% cpu 0.013 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 92% cpu 0.012 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 92% cpu 0.012 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 91% cpu 0.012 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 92% cpu 0.012 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 92% cpu 0.012 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 91% cpu 0.012 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 91% cpu 0.012 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 92% cpu 0.012 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 92% cpu 0.012 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 92% cpu 0.012 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 92% cpu 0.012 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.01s system 35% cpu 0.040 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.009 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.009 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.009 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 88% cpu 0.009 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.009 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.010 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.009 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.010 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.010 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.009 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.009 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.009 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.010 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.009 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.009 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.009 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.010 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.009 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 91% cpu 0.009 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 91% cpu 0.009 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.010 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.009 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.009 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.009 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.009 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 93% cpu 0.010 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.010 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.010 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.010 total"""

times1 = []
for line in in_string.split("\n")[0:30]:
    s = line.split()
    times1.append(s[12])

times2 = []
for line in in_string.split("\n")[30:60]:
    s = line.split()
    times2.append(s[12])

with open("results.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([])
    writer.writerow(times1)
    writer.writerow(times2)

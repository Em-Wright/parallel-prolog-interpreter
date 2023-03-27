import csv

in_string = """ ./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 81% cpu 0.154 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 120% cpu 0.100 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 132% cpu 0.093 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 129% cpu 0.094 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 128% cpu 0.096 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 128% cpu 0.097 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 133% cpu 0.094 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 125% cpu 0.096 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 131% cpu 0.094 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 127% cpu 0.095 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 124% cpu 0.097 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 129% cpu 0.094 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 123% cpu 0.096 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 125% cpu 0.095 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 123% cpu 0.098 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 124% cpu 0.095 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 121% cpu 0.100 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 124% cpu 0.096 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 117% cpu 0.101 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.06s system 116% cpu 0.100 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.06s system 112% cpu 0.100 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 116% cpu 0.103 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.06s system 119% cpu 0.100 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 123% cpu 0.097 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 114% cpu 0.102 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 121% cpu 0.097 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 124% cpu 0.097 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 123% cpu 0.097 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.06s system 116% cpu 0.099 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 127% cpu 0.094 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 98% cpu 0.088 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 101% cpu 0.088 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 100% cpu 0.089 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 97% cpu 0.088 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 97% cpu 0.089 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 97% cpu 0.089 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 99% cpu 0.090 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 97% cpu 0.090 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 103% cpu 0.089 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 102% cpu 0.088 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 99% cpu 0.089 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 96% cpu 0.089 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 101% cpu 0.087 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 96% cpu 0.092 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 103% cpu 0.088 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 100% cpu 0.087 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 100% cpu 0.090 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 102% cpu 0.089 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 101% cpu 0.090 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 95% cpu 0.092 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 99% cpu 0.090 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 101% cpu 0.087 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 104% cpu 0.089 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 99% cpu 0.090 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 96% cpu 0.093 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 102% cpu 0.087 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 102% cpu 0.092 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 97% cpu 0.092 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 99% cpu 0.090 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 98% cpu 0.094 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 65% cpu 0.094 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 64% cpu 0.093 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 66% cpu 0.092 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 67% cpu 0.090 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 64% cpu 0.097 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 67% cpu 0.092 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 66% cpu 0.090 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 66% cpu 0.094 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 65% cpu 0.093 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 64% cpu 0.091 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 64% cpu 0.093 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 65% cpu 0.090 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 64% cpu 0.092 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 68% cpu 0.092 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 66% cpu 0.095 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 66% cpu 0.092 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 63% cpu 0.096 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 66% cpu 0.091 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 65% cpu 0.093 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 66% cpu 0.092 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 66% cpu 0.091 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 65% cpu 0.090 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 66% cpu 0.091 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 66% cpu 0.092 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 66% cpu 0.092 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 65% cpu 0.091 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 61% cpu 0.099 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 67% cpu 0.090 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 64% cpu 0.093 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 65% cpu 0.093 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 29% cpu 0.116 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 29% cpu 0.117 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 29% cpu 0.117 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 29% cpu 0.115 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 31% cpu 0.117 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 30% cpu 0.117 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 28% cpu 0.118 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 29% cpu 0.115 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 29% cpu 0.116 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 29% cpu 0.115 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 31% cpu 0.116 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 30% cpu 0.115 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 30% cpu 0.118 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 29% cpu 0.116 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 29% cpu 0.119 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 30% cpu 0.119 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 29% cpu 0.118 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 29% cpu 0.116 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 29% cpu 0.115 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 30% cpu 0.115 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 28% cpu 0.121 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 31% cpu 0.117 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 31% cpu 0.117 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 29% cpu 0.117 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 28% cpu 0.116 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 28% cpu 0.117 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 29% cpu 0.118 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 30% cpu 0.119 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 30% cpu 0.119 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 29% cpu 0.118 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.01s system 83% cpu 0.188 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.152 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.152 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.151 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.153 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.152 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.152 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.153 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.151 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.153 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.153 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.151 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.152 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.152 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.151 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.152 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.152 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.152 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.152 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.152 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.152 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.151 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.152 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.153 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.153 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.152 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.152 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.152 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.152 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.15s user 0.00s system 99% cpu 0.152 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.08s system 98% cpu 0.129 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 147% cpu 0.082 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.06s system 121% cpu 0.092 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 143% cpu 0.083 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 137% cpu 0.089 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 141% cpu 0.085 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 151% cpu 0.082 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 150% cpu 0.080 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 149% cpu 0.080 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.06s system 131% cpu 0.089 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 144% cpu 0.083 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.06s system 140% cpu 0.081 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 145% cpu 0.082 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 139% cpu 0.085 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 148% cpu 0.080 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.06s system 143% cpu 0.081 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 153% cpu 0.078 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 151% cpu 0.080 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 144% cpu 0.083 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 152% cpu 0.080 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.06s system 139% cpu 0.084 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.06s system 144% cpu 0.081 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.06s system 145% cpu 0.080 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 150% cpu 0.079 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.06s system 128% cpu 0.090 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 147% cpu 0.081 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 136% cpu 0.087 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 135% cpu 0.087 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 140% cpu 0.085 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 155% cpu 0.078 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 124% cpu 0.070 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 117% cpu 0.075 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 119% cpu 0.071 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 117% cpu 0.074 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 118% cpu 0.073 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 119% cpu 0.073 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 121% cpu 0.071 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 121% cpu 0.072 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 112% cpu 0.077 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 124% cpu 0.073 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 116% cpu 0.074 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 116% cpu 0.076 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 116% cpu 0.075 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 118% cpu 0.074 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 116% cpu 0.073 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 122% cpu 0.074 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 121% cpu 0.073 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 105% cpu 0.078 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 118% cpu 0.076 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 116% cpu 0.076 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 111% cpu 0.079 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 119% cpu 0.078 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 119% cpu 0.075 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 120% cpu 0.077 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 119% cpu 0.075 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 124% cpu 0.073 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 119% cpu 0.075 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 122% cpu 0.072 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 116% cpu 0.077 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 119% cpu 0.073 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 73% cpu 0.082 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 77% cpu 0.076 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 79% cpu 0.074 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 80% cpu 0.072 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 77% cpu 0.078 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 82% cpu 0.076 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 81% cpu 0.072 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 80% cpu 0.073 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 81% cpu 0.076 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 81% cpu 0.073 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 78% cpu 0.076 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 78% cpu 0.076 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 81% cpu 0.073 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 74% cpu 0.078 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 82% cpu 0.072 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 78% cpu 0.075 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 75% cpu 0.079 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 83% cpu 0.073 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 82% cpu 0.073 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 81% cpu 0.075 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 81% cpu 0.073 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 84% cpu 0.072 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 83% cpu 0.074 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 83% cpu 0.072 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 80% cpu 0.074 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 81% cpu 0.074 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 79% cpu 0.074 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 81% cpu 0.073 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 84% cpu 0.073 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 81% cpu 0.075 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 39% cpu 0.092 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 38% cpu 0.090 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 38% cpu 0.091 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 38% cpu 0.090 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 38% cpu 0.090 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 38% cpu 0.090 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 39% cpu 0.090 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 36% cpu 0.094 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 38% cpu 0.093 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 40% cpu 0.090 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 37% cpu 0.091 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 38% cpu 0.090 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 38% cpu 0.092 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 38% cpu 0.089 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 38% cpu 0.090 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 39% cpu 0.092 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 39% cpu 0.089 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 38% cpu 0.088 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 38% cpu 0.092 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 39% cpu 0.089 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 38% cpu 0.089 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 38% cpu 0.089 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 38% cpu 0.089 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 39% cpu 0.089 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 38% cpu 0.089 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 37% cpu 0.089 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 39% cpu 0.089 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 39% cpu 0.090 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 35% cpu 0.093 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 37% cpu 0.088 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.01s system 75% cpu 0.140 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.100 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.100 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.102 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.101 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.100 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.102 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.102 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.101 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.102 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.102 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.099 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.101 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.100 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.100 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 99% cpu 0.101 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.101 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.109 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.101 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.100 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.102 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.102 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.101 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.100 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.101 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.102 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.101 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.102 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 98% cpu 0.104 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.10s user 0.00s system 99% cpu 0.101 total"""



print("8 workers")
par8 = []
for line in in_string.split("\n")[0:30]:
    s = line.split()
    if s[4] != "8":
        print (s[4])
    par8.append(s[13])

print("\n\n6 workers")
par6 = []
for line in in_string.split("\n")[30:60]:
    s = line.split()
    if s[4] != "6":
        print (s[4])
    par6.append(s[13])

print("\n\n4 workers")
par4 = []
for line in in_string.split("\n")[60:90]:
    s = line.split()
    if s[4] != "4":
        print( s[4])
    par4.append(s[13])

print("\n\n2 workers")
par2 = []
for line in in_string.split("\n")[90:120]:
    s = line.split()
    if s[4] != "2":
        print(s[4])
    par2.append(s[13])

print("\n\nsequential")
seq = []
for line in in_string.split("\n")[120:150]:
# for line in in_string.split("\n")[0:30]:
    s = line.split()
    seq.append(s[12])
    print( s[12])

print("\n\ntrail 8")
tr8 = []
for line in in_string.split("\n")[150:180]:
    s = line.split()
    tr8.append(s[13])
    print( s[13])
tr6 = []
for line in in_string.split("\n")[180:210]:
    s = line.split()
    tr6.append(s[13])
    print( s[13])
tr4 = []
for line in in_string.split("\n")[210:240]:
    s = line.split()
    tr4.append(s[13])
    print( s[13])
tr2 = []
for line in in_string.split("\n")[240:270]:
    s = line.split()
    tr2.append(s[13])
    print( s[13])
trseq = []
for line in in_string.split("\n")[270:300]:
# for line in in_string.split("\n")[30:60]:
    s = line.split()
    trseq.append(s[12])
    print( s[12])


in_string2 = """Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.01s system 24% cpu 0.072 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 86% cpu 0.016 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 87% cpu 0.015 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 86% cpu 0.016 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 85% cpu 0.016 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 81% cpu 0.016 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 86% cpu 0.016 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 86% cpu 0.015 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 81% cpu 0.017 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 87% cpu 0.015 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 87% cpu 0.015 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 87% cpu 0.016 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 87% cpu 0.015 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 87% cpu 0.015 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 87% cpu 0.015 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 86% cpu 0.015 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 87% cpu 0.015 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 83% cpu 0.016 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 87% cpu 0.015 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 86% cpu 0.015 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 86% cpu 0.016 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 86% cpu 0.015 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 84% cpu 0.016 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 83% cpu 0.017 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 84% cpu 0.016 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 87% cpu 0.015 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 87% cpu 0.016 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 86% cpu 0.016 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 87% cpu 0.015 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 88% cpu 0.016 total
"""

swipl = []
for line in in_string2.split("\n"):
    s = line.split(' ')
    if len(s) > 0 and s[0] == "swipl":
        swipl.append(s[12])

with open("results.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([])
    writer.writerow(par8)
    writer.writerow(par6)
    writer.writerow(par4)
    writer.writerow(par2)
    writer.writerow(seq)
    writer.writerow([])
    writer.writerow(tr8)
    writer.writerow(tr6)
    writer.writerow(tr4)
    writer.writerow(tr2)
    writer.writerow(trseq)
    writer.writerow([])
    writer.writerow(swipl)

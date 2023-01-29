import csv

in_string = """./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.67s system 6% cpu 16.991 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.49s user 0.65s system 6% cpu 17.210 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.48s user 0.62s system 6% cpu 16.928 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.47s user 0.61s system 6% cpu 16.292 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.47s user 0.61s system 6% cpu 16.459 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.46s user 0.59s system 6% cpu 16.177 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.46s user 0.59s system 6% cpu 16.675 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.47s user 0.61s system 6% cpu 16.575 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.46s user 0.59s system 6% cpu 16.286 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.46s user 0.60s system 6% cpu 16.280 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.46s user 0.59s system 6% cpu 16.221 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.46s user 0.59s system 6% cpu 16.200 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.46s user 0.60s system 6% cpu 16.377 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.46s user 0.60s system 6% cpu 16.327 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.47s user 0.60s system 6% cpu 16.323 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.48s user 0.62s system 6% cpu 16.576 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.46s user 0.60s system 6% cpu 16.203 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.47s user 0.61s system 6% cpu 16.421 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.48s user 0.62s system 6% cpu 16.176 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.46s user 0.60s system 6% cpu 16.332 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.45s user 0.57s system 6% cpu 16.224 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.44s user 0.57s system 6% cpu 16.097 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.46s user 0.58s system 6% cpu 16.359 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.47s user 0.59s system 6% cpu 16.528 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.45s user 0.58s system 6% cpu 16.413 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.47s user 0.59s system 6% cpu 16.487 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.45s user 0.57s system 6% cpu 16.283 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.44s user 0.58s system 6% cpu 16.210 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.45s user 0.58s system 6% cpu 16.302 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.45s user 0.57s system 6% cpu 16.596 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.71s user 0.91s system 8% cpu 18.388 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.70s user 0.90s system 9% cpu 17.464 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.71s user 0.93s system 9% cpu 18.103 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.70s user 0.89s system 8% cpu 17.739 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.63s user 0.80s system 8% cpu 17.740 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.70s user 0.89s system 8% cpu 17.839 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.73s user 0.92s system 9% cpu 17.710 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.70s user 0.89s system 8% cpu 18.041 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.73s user 0.96s system 9% cpu 18.200 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.71s user 0.93s system 9% cpu 17.650 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.71s user 0.92s system 9% cpu 17.707 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.72s user 0.93s system 9% cpu 18.321 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.70s user 0.90s system 9% cpu 17.751 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.69s user 0.87s system 8% cpu 17.438 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.72s user 0.95s system 9% cpu 17.952 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.71s user 0.94s system 9% cpu 17.673 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.72s user 0.94s system 9% cpu 17.586 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.72s user 0.93s system 9% cpu 17.949 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.72s user 0.93s system 9% cpu 18.159 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.71s user 0.91s system 9% cpu 17.746 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.73s user 0.96s system 9% cpu 17.784 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.73s user 0.94s system 9% cpu 17.813 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.72s user 0.94s system 9% cpu 17.463 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.73s user 0.94s system 9% cpu 18.107 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.71s user 0.91s system 8% cpu 18.149 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.70s user 0.92s system 9% cpu 17.472 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.73s user 0.95s system 9% cpu 18.280 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.72s user 0.94s system 9% cpu 17.549 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.72s user 0.94s system 9% cpu 18.036 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.71s user 0.93s system 9% cpu 17.747 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.56s user 0.72s system 5% cpu 25.499 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.56s user 0.70s system 4% cpu 25.453 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.57s user 0.74s system 5% cpu 25.351 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.55s user 0.73s system 5% cpu 25.484 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.56s user 0.71s system 4% cpu 25.299 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.56s user 0.72s system 5% cpu 25.400 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.56s user 0.75s system 5% cpu 25.472 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.55s user 0.69s system 4% cpu 25.464 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.56s user 0.69s system 4% cpu 25.341 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.55s user 0.73s system 5% cpu 25.247 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.55s user 0.71s system 4% cpu 25.559 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.56s user 0.71s system 4% cpu 25.468 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.56s user 0.75s system 5% cpu 25.631 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.54s user 0.71s system 4% cpu 25.328 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.55s user 0.69s system 4% cpu 25.482 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.56s user 0.73s system 5% cpu 25.436 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.55s user 0.71s system 5% cpu 25.210 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.55s user 0.70s system 4% cpu 25.334 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.55s user 0.72s system 4% cpu 25.400 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.54s user 0.74s system 5% cpu 25.372 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.55s user 0.69s system 4% cpu 25.508 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.57s user 0.72s system 5% cpu 25.661 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.56s user 0.75s system 5% cpu 25.400 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.55s user 0.72s system 5% cpu 25.303 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.56s user 0.71s system 4% cpu 25.705 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.57s user 0.75s system 5% cpu 25.375 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.55s user 0.71s system 4% cpu 25.278 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.56s user 0.71s system 5% cpu 25.243 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.56s user 0.72s system 5% cpu 25.204 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.56s user 0.75s system 5% cpu 25.473 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.92s user 1.33s system 4% cpu 50.115 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.92s user 1.34s system 4% cpu 50.090 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.92s user 1.32s system 4% cpu 50.052 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.92s user 1.33s system 4% cpu 50.155 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.92s user 1.31s system 4% cpu 50.345 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.90s user 1.31s system 4% cpu 49.984 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.92s user 1.30s system 4% cpu 50.232 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.92s user 1.30s system 4% cpu 50.013 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.91s user 1.30s system 4% cpu 50.059 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.93s user 1.30s system 4% cpu 50.040 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.92s user 1.29s system 4% cpu 50.463 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.90s user 1.31s system 4% cpu 49.925 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.94s user 1.32s system 4% cpu 50.123 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.91s user 1.30s system 4% cpu 50.106 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.91s user 1.30s system 4% cpu 49.929 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.94s user 1.30s system 4% cpu 50.171 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.91s user 1.31s system 4% cpu 50.270 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.92s user 1.31s system 4% cpu 50.049 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.92s user 1.30s system 4% cpu 50.223 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.90s user 1.32s system 4% cpu 50.327 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.93s user 1.30s system 4% cpu 50.015 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.93s user 1.28s system 4% cpu 50.609 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.90s user 1.29s system 4% cpu 50.171 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.93s user 1.30s system 4% cpu 50.267 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.92s user 1.30s system 4% cpu 50.051 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.91s user 1.29s system 4% cpu 50.067 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.92s user 1.28s system 4% cpu 49.690 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.92s user 1.30s system 4% cpu 49.842 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.91s user 1.29s system 4% cpu 50.118 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.93s user 1.31s system 4% cpu 50.343 total """

in_string = """./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.51s user 0.57s system 5% cpu 18.396 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.53s system 5% cpu 18.450 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.51s user 0.53s system 5% cpu 18.345 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.54s system 5% cpu 18.421 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.55s system 5% cpu 18.363 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.54s system 5% cpu 18.442 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.54s system 5% cpu 18.301 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.54s system 5% cpu 18.366 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.51s user 0.54s system 5% cpu 18.448 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.51s user 0.55s system 5% cpu 18.390 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.54s system 5% cpu 18.419 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.51s user 0.54s system 5% cpu 18.413 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.53s system 5% cpu 18.370 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.55s system 5% cpu 18.431 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.53s system 5% cpu 18.329 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.55s system 5% cpu 18.396 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.53s system 5% cpu 18.316 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.54s system 5% cpu 18.368 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.51s user 0.54s system 5% cpu 18.442 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.53s system 5% cpu 18.366 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.51s user 0.53s system 5% cpu 18.372 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.54s system 5% cpu 18.331 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.53s system 5% cpu 18.344 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.53s system 5% cpu 18.346 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.54s system 5% cpu 18.340 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.54s system 5% cpu 18.411 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.52s system 5% cpu 18.395 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.53s system 5% cpu 18.340 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.53s system 5% cpu 18.363 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.50s user 0.53s system 5% cpu 18.337 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.47s user 0.49s system 5% cpu 18.400 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.48s user 0.49s system 5% cpu 18.315 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.47s user 0.50s system 5% cpu 18.373 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.47s user 0.49s system 5% cpu 18.395 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.48s user 0.50s system 5% cpu 18.413 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.47s user 0.49s system 5% cpu 18.325 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.47s user 0.50s system 5% cpu 18.307 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.47s user 0.49s system 5% cpu 18.326 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.47s user 0.49s system 5% cpu 18.345 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.47s user 0.49s system 5% cpu 18.366 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.47s user 0.49s system 5% cpu 18.337 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.47s user 0.49s system 5% cpu 18.367 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.48s user 0.49s system 5% cpu 18.354 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.47s user 0.49s system 5% cpu 18.355 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.47s user 0.49s system 5% cpu 18.296 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.47s user 0.49s system 5% cpu 18.331 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.46s user 0.48s system 5% cpu 18.201 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.47s user 0.48s system 5% cpu 18.305 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.47s user 0.48s system 5% cpu 18.330 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.48s user 0.49s system 5% cpu 18.365 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.47s user 0.48s system 5% cpu 18.346 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.47s user 0.49s system 5% cpu 18.373 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.47s user 0.47s system 5% cpu 18.329 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.47s user 0.49s system 5% cpu 18.348 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.47s user 0.48s system 5% cpu 18.321 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.47s user 0.48s system 5% cpu 18.403 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.46s user 0.48s system 5% cpu 18.300 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.47s user 0.49s system 5% cpu 18.430 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.47s user 0.48s system 5% cpu 18.330 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.48s user 0.49s system 5% cpu 18.399 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.43s user 0.43s system 4% cpu 18.308 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.44s user 0.44s system 4% cpu 18.424 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.43s user 0.44s system 4% cpu 18.325 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.44s user 0.44s system 4% cpu 18.364 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.43s user 0.43s system 4% cpu 18.349 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.44s user 0.45s system 4% cpu 18.385 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.43s user 0.43s system 4% cpu 18.390 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.44s user 0.44s system 4% cpu 18.424 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.43s user 0.44s system 4% cpu 18.378 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.44s user 0.44s system 4% cpu 18.338 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.43s user 0.44s system 4% cpu 18.291 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.44s user 0.44s system 4% cpu 18.380 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.43s user 0.43s system 4% cpu 18.381 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.44s user 0.44s system 4% cpu 18.367 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.43s user 0.44s system 4% cpu 18.316 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.44s user 0.44s system 4% cpu 18.348 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.43s user 0.44s system 4% cpu 18.339 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.44s user 0.44s system 4% cpu 18.394 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.43s user 0.43s system 4% cpu 18.317 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.44s user 0.44s system 4% cpu 18.306 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.43s user 0.43s system 4% cpu 18.282 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.43s user 0.44s system 4% cpu 18.296 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.44s user 0.43s system 4% cpu 18.300 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.44s user 0.44s system 4% cpu 18.324 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.44s user 0.44s system 4% cpu 18.368 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.44s user 0.43s system 4% cpu 18.281 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.44s user 0.44s system 4% cpu 18.325 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.44s user 0.44s system 4% cpu 18.372 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.44s user 0.44s system 4% cpu 18.324 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.44s user 0.44s system 4% cpu 18.299 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.41s user 0.39s system 4% cpu 18.379 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.40s user 0.38s system 4% cpu 18.290 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.41s user 0.39s system 4% cpu 18.381 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.41s user 0.39s system 4% cpu 18.362 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.41s user 0.39s system 4% cpu 18.372 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.40s user 0.39s system 4% cpu 18.354 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.41s user 0.39s system 4% cpu 18.355 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.41s user 0.39s system 4% cpu 18.285 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.41s user 0.40s system 4% cpu 18.415 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.40s user 0.39s system 4% cpu 18.285 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.41s user 0.39s system 4% cpu 18.371 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.40s user 0.38s system 4% cpu 18.368 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.42s user 0.39s system 4% cpu 18.468 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.40s user 0.38s system 4% cpu 18.397 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.41s user 0.39s system 4% cpu 18.376 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.41s user 0.39s system 4% cpu 18.354 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.41s user 0.39s system 4% cpu 18.447 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.41s user 0.39s system 4% cpu 18.391 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.41s user 0.39s system 4% cpu 18.323 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.41s user 0.39s system 4% cpu 18.330 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.41s user 0.39s system 4% cpu 18.355 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.41s user 0.39s system 4% cpu 18.378 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.41s user 0.39s system 4% cpu 18.417 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.41s user 0.39s system 4% cpu 18.386 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.40s user 0.39s system 4% cpu 18.309 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.42s user 0.40s system 4% cpu 18.446 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.41s user 0.39s system 4% cpu 18.309 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.41s user 0.42s system 4% cpu 18.474 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.40s user 0.38s system 4% cpu 18.308 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.41s user 0.39s system 4% cpu 18.329 total """

print("8 workers")
par8 = []
for line in in_string.split("\n")[0:30]:
    s = line.split()
    par8.append(s[13])
    print(s[13])

print("\n\n6 workers")
par6 = []
for line in in_string.split("\n")[30:60]:
    s = line.split()
    par6.append(s[13])
    print(s[13])

print("\n\n4 workers")
par4 = []
for line in in_string.split("\n")[60:90]:
    s = line.split()
    par4.append(s[13])
    print( s[13])

print("\n\n2 workers")
par2 = []
for line in in_string.split("\n")[90:120]:
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

with open("nqueens.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([])
    writer.writerow(["8queens"])
    writer.writerow(par8)
    writer.writerow(par6)
    writer.writerow(par4)
    writer.writerow(par2)
    writer.writerow([])
    # writer.writerow(seq)
    # writer.writerow(tr)

in_string2 = """
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.01s system 27% cpu 0.058 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 84% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 84% cpu 0.011 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 84% cpu 0.011 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 78% cpu 0.013 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 73% cpu 0.013 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 85% cpu 0.011 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 83% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 83% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 83% cpu 0.011 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 83% cpu 0.011 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 81% cpu 0.013 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 84% cpu 0.011 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 84% cpu 0.011 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 81% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 83% cpu 0.011 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 74% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 64% cpu 0.015 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 78% cpu 0.013 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 84% cpu 0.011 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 84% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 83% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 86% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 74% cpu 0.014 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 83% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 80% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 83% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 83% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 83% cpu 0.012 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_contrived.pl:15:
Warning:    Singleton variables: [X]
swipl -q prolog_programs/swi_contrived.pl > timings.txt  0.01s user 0.00s system 83% cpu 0.012 total
"""

swipl = []
for line in in_string2.split("\n"):
    s = line.split(' ')
    if s[0] == "Warning:" or s[0]== "Warning:\xa0" or len(s) < 13:
        continue
    swipl.append(s[12])

# with open("contrived.csv", "a") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(swipl)

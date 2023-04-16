import csv

in_string = """./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 41% cpu 0.321 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.08s system 42% cpu 0.315 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.08s system 42% cpu 0.313 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 41% cpu 0.316 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 42% cpu 0.315 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 40% cpu 0.316 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 40% cpu 0.319 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 42% cpu 0.319 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 42% cpu 0.320 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 42% cpu 0.317 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.08s system 42% cpu 0.317 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.08s system 42% cpu 0.320 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.08s system 42% cpu 0.317 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 41% cpu 0.325 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.08s system 43% cpu 0.316 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.08s system 42% cpu 0.318 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.08s system 42% cpu 0.320 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 41% cpu 0.319 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 41% cpu 0.319 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 41% cpu 0.323 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.08s system 41% cpu 0.331 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.08s system 42% cpu 0.325 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 40% cpu 0.324 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 40% cpu 0.319 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 39% cpu 0.321 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 41% cpu 0.320 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.08s system 43% cpu 0.313 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 42% cpu 0.316 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 40% cpu 0.317 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.08s system 41% cpu 0.321 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 37% cpu 0.310 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 36% cpu 0.315 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 35% cpu 0.321 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 37% cpu 0.314 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.07s system 37% cpu 0.317 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.07s system 38% cpu 0.320 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 37% cpu 0.314 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.07s system 37% cpu 0.315 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.07s system 37% cpu 0.310 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.07s system 38% cpu 0.312 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 36% cpu 0.315 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 35% cpu 0.330 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.07s system 36% cpu 0.330 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.07s system 39% cpu 0.316 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.07s system 37% cpu 0.314 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.07s system 37% cpu 0.317 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.07s system 37% cpu 0.317 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 37% cpu 0.311 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 36% cpu 0.318 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 37% cpu 0.320 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.07s system 37% cpu 0.314 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 37% cpu 0.315 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 37% cpu 0.314 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.07s system 38% cpu 0.316 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 37% cpu 0.316 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.07s system 38% cpu 0.316 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.07s system 38% cpu 0.313 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.07s system 38% cpu 0.310 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 37% cpu 0.311 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.07s system 36% cpu 0.318 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 31% cpu 0.315 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 31% cpu 0.311 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.05s user 0.06s system 32% cpu 0.316 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.06s system 33% cpu 0.310 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.06s system 32% cpu 0.309 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.06s system 32% cpu 0.310 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 31% cpu 0.310 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 32% cpu 0.306 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.06s system 31% cpu 0.310 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 31% cpu 0.304 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.06s system 32% cpu 0.310 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 31% cpu 0.308 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.06s system 32% cpu 0.309 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 28% cpu 0.321 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 32% cpu 0.306 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 31% cpu 0.311 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.05s user 0.06s system 33% cpu 0.310 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.06s system 32% cpu 0.309 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 31% cpu 0.306 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.06s system 32% cpu 0.307 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 31% cpu 0.309 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 31% cpu 0.307 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.06s system 32% cpu 0.307 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 31% cpu 0.308 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.06s system 30% cpu 0.327 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 32% cpu 0.308 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 31% cpu 0.311 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 31% cpu 0.308 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.06s system 32% cpu 0.309 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 31% cpu 0.309 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.05s system 26% cpu 0.308 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.05s system 27% cpu 0.302 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.05s system 27% cpu 0.305 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.04s system 26% cpu 0.307 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.05s system 26% cpu 0.308 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.04s system 26% cpu 0.305 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.05s system 27% cpu 0.307 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.05s system 26% cpu 0.315 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.04s system 26% cpu 0.307 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.05s system 27% cpu 0.305 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.05s system 27% cpu 0.304 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.05s system 27% cpu 0.303 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.05s system 26% cpu 0.302 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.05s system 27% cpu 0.306 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.05s system 27% cpu 0.306 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.05s system 26% cpu 0.305 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.05s system 27% cpu 0.305 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.05s system 27% cpu 0.307 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.05s system 27% cpu 0.309 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.05s system 26% cpu 0.304 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.05s system 26% cpu 0.308 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.05s system 27% cpu 0.306 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.04s system 25% cpu 0.309 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.04s system 26% cpu 0.305 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.05s system 27% cpu 0.311 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.05s system 26% cpu 0.313 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.04s system 26% cpu 0.305 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.04s system 27% cpu 0.302 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.04s system 26% cpu 0.304 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.05s system 28% cpu 0.305 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 22% cpu 0.303 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 23% cpu 0.304 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 22% cpu 0.302 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 22% cpu 0.301 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 22% cpu 0.310 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 23% cpu 0.307 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 23% cpu 0.303 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 22% cpu 0.305 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 22% cpu 0.303 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 22% cpu 0.304 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 22% cpu 0.313 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 22% cpu 0.303 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 23% cpu 0.305 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 22% cpu 0.302 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 23% cpu 0.303 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 23% cpu 0.304 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 22% cpu 0.306 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 23% cpu 0.306 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 23% cpu 0.304 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 23% cpu 0.303 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 22% cpu 0.312 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 23% cpu 0.301 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 22% cpu 0.304 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 22% cpu 0.302 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 21% cpu 0.312 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 21% cpu 0.304 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 22% cpu 0.301 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 22% cpu 0.302 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 23% cpu 0.305 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.04s system 22% cpu 0.302 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.309 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.304 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.306 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.302 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.301 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.307 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.302 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.305 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.304 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.301 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.307 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.306 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.302 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.303 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.303 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.304 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.304 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.301 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.304 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.306 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.303 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.312 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.305 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.304 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 19% cpu 0.301 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.303 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.304 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.304 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.302 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.03s user 0.03s system 18% cpu 0.303 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 14% cpu 0.300 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 14% cpu 0.301 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 14% cpu 0.297 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 14% cpu 0.301 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 14% cpu 0.297 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 14% cpu 0.299 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 14% cpu 0.303 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 14% cpu 0.303 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 14% cpu 0.301 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 13% cpu 0.299 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 14% cpu 0.299 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 14% cpu 0.300 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 14% cpu 0.300 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 14% cpu 0.296 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 14% cpu 0.298 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 14% cpu 0.299 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 14% cpu 0.299 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 14% cpu 0.303 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 14% cpu 0.301 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 15% cpu 0.308 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 15% cpu 0.299 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 15% cpu 0.305 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 14% cpu 0.305 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 15% cpu 0.303 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 14% cpu 0.305 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 15% cpu 0.308 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 15% cpu 0.305 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 14% cpu 0.311 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.03s system 15% cpu 0.304 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 15% cpu 0.304 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 8% cpu 0.527 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 8% cpu 0.525 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 8% cpu 0.524 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 8% cpu 0.520 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 8% cpu 0.515 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 8% cpu 0.520 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 8% cpu 0.516 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 8% cpu 0.517 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.517 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.521 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 8% cpu 0.522 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.515 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.517 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.517 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.515 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 8% cpu 0.512 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.518 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 8% cpu 0.516 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.517 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 8% cpu 0.516 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 8% cpu 0.524 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 8% cpu 0.520 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 8% cpu 0.520 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 8% cpu 0.520 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 8% cpu 0.519 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 8% cpu 0.520 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 8% cpu 0.520 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.518 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 8% cpu 0.513 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 8% cpu 0.515 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.45s user 0.01s system 92% cpu 0.491 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.44s user 0.00s system 99% cpu 0.450 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.44s user 0.00s system 99% cpu 0.449 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.44s user 0.00s system 99% cpu 0.449 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.44s user 0.00s system 99% cpu 0.449 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.44s user 0.00s system 99% cpu 0.447 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.45s user 0.00s system 99% cpu 0.453 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.44s user 0.00s system 99% cpu 0.448 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.44s user 0.00s system 99% cpu 0.447 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.44s user 0.00s system 99% cpu 0.447 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.44s user 0.00s system 99% cpu 0.448 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.45s user 0.00s system 99% cpu 0.457 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.45s user 0.00s system 99% cpu 0.451 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.44s user 0.00s system 99% cpu 0.448 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.44s user 0.00s system 99% cpu 0.448 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.44s user 0.00s system 99% cpu 0.449 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.44s user 0.00s system 99% cpu 0.447 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.44s user 0.00s system 99% cpu 0.448 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.44s user 0.00s system 99% cpu 0.449 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.44s user 0.00s system 99% cpu 0.448 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.44s user 0.01s system 99% cpu 0.451 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.44s user 0.01s system 99% cpu 0.450 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.45s user 0.00s system 99% cpu 0.455 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.44s user 0.01s system 99% cpu 0.450 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.45s user 0.01s system 99% cpu 0.452 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.45s user 0.01s system 99% cpu 0.452 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.44s user 0.01s system 99% cpu 0.451 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.44s user 0.01s system 99% cpu 0.452 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.44s user 0.01s system 99% cpu 0.453 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.44s user 0.00s system 99% cpu 0.449 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.363 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.370 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.370 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.375 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.38s user 0.01s system 99% cpu 0.383 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.365 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.372 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.368 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.370 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.365 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.35s user 0.01s system 99% cpu 0.362 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.363 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.371 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.364 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.363 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.366 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.38s user 0.01s system 99% cpu 0.384 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.367 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.368 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.368 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.366 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.38s user 0.01s system 99% cpu 0.386 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.35s user 0.01s system 99% cpu 0.364 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.367 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.366 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.367 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.367 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.367 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.38s user 0.01s system 99% cpu 0.390 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.36s user 0.01s system 99% cpu 0.364 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.08s system 61% cpu 0.218 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 73% cpu 0.172 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 70% cpu 0.170 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 71% cpu 0.173 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 70% cpu 0.175 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 69% cpu 0.173 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 71% cpu 0.170 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.06s system 68% cpu 0.172 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 69% cpu 0.171 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 70% cpu 0.172 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 69% cpu 0.171 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 73% cpu 0.169 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 70% cpu 0.178 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 68% cpu 0.172 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 70% cpu 0.173 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.06s system 61% cpu 0.181 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 70% cpu 0.172 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 73% cpu 0.172 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.06s system 67% cpu 0.174 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 70% cpu 0.179 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 71% cpu 0.172 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 68% cpu 0.175 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 70% cpu 0.174 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 71% cpu 0.172 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 73% cpu 0.173 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 72% cpu 0.171 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 71% cpu 0.173 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.05s user 0.07s system 70% cpu 0.171 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 69% cpu 0.176 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.06s user 0.07s system 71% cpu 0.174 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 63% cpu 0.168 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 64% cpu 0.169 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 61% cpu 0.169 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 63% cpu 0.167 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 63% cpu 0.169 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 66% cpu 0.168 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 64% cpu 0.167 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 63% cpu 0.169 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 61% cpu 0.169 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 62% cpu 0.170 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 63% cpu 0.165 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 59% cpu 0.169 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 63% cpu 0.170 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 62% cpu 0.169 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 64% cpu 0.168 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 62% cpu 0.167 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 63% cpu 0.170 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 58% cpu 0.182 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 61% cpu 0.169 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 61% cpu 0.171 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 61% cpu 0.169 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 62% cpu 0.173 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 61% cpu 0.170 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.05s system 59% cpu 0.167 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 61% cpu 0.172 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 61% cpu 0.169 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 60% cpu 0.175 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 65% cpu 0.167 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 63% cpu 0.173 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.05s user 0.06s system 61% cpu 0.167 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 56% cpu 0.165 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 55% cpu 0.164 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 53% cpu 0.168 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 53% cpu 0.169 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 56% cpu 0.163 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 50% cpu 0.173 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 55% cpu 0.164 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 54% cpu 0.169 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 54% cpu 0.167 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 56% cpu 0.166 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 53% cpu 0.172 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 49% cpu 0.179 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 55% cpu 0.165 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 53% cpu 0.172 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 53% cpu 0.166 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 53% cpu 0.170 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 53% cpu 0.168 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 55% cpu 0.165 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 53% cpu 0.164 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 51% cpu 0.172 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 54% cpu 0.165 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 55% cpu 0.166 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 56% cpu 0.165 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 53% cpu 0.166 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 57% cpu 0.167 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 55% cpu 0.167 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 52% cpu 0.167 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 54% cpu 0.168 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 55% cpu 0.165 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.04s user 0.05s system 54% cpu 0.165 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.04s system 47% cpu 0.161 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 46% cpu 0.165 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 44% cpu 0.166 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 48% cpu 0.159 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 46% cpu 0.167 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 47% cpu 0.164 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 44% cpu 0.168 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 46% cpu 0.162 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 46% cpu 0.162 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 47% cpu 0.162 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.04s user 0.04s system 48% cpu 0.160 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 45% cpu 0.164 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 45% cpu 0.162 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 46% cpu 0.158 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 46% cpu 0.164 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 46% cpu 0.163 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 47% cpu 0.161 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 45% cpu 0.163 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 46% cpu 0.162 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 48% cpu 0.161 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 46% cpu 0.163 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 46% cpu 0.162 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 47% cpu 0.164 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 47% cpu 0.163 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 47% cpu 0.159 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 44% cpu 0.170 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 44% cpu 0.171 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 44% cpu 0.169 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 46% cpu 0.162 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.03s user 0.04s system 47% cpu 0.160 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 37% cpu 0.165 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 38% cpu 0.161 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 39% cpu 0.161 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 37% cpu 0.168 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 39% cpu 0.159 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 39% cpu 0.159 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 39% cpu 0.158 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 38% cpu 0.160 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 38% cpu 0.160 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 36% cpu 0.168 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 37% cpu 0.160 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 38% cpu 0.158 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 38% cpu 0.158 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 39% cpu 0.160 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 38% cpu 0.163 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 39% cpu 0.160 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 40% cpu 0.160 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 38% cpu 0.158 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 37% cpu 0.163 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 38% cpu 0.159 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 39% cpu 0.160 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 36% cpu 0.165 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 37% cpu 0.161 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 39% cpu 0.159 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 38% cpu 0.159 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 38% cpu 0.159 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 38% cpu 0.158 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 38% cpu 0.159 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 39% cpu 0.163 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.03s user 0.03s system 38% cpu 0.161 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 31% cpu 0.159 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 32% cpu 0.159 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 31% cpu 0.158 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 31% cpu 0.161 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 30% cpu 0.163 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 32% cpu 0.160 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 31% cpu 0.159 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 30% cpu 0.158 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 30% cpu 0.166 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 31% cpu 0.159 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 31% cpu 0.160 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 31% cpu 0.157 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 31% cpu 0.157 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 29% cpu 0.169 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 30% cpu 0.159 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 31% cpu 0.158 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.02s system 30% cpu 0.156 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 31% cpu 0.158 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 31% cpu 0.158 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.02s system 30% cpu 0.159 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 31% cpu 0.159 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 30% cpu 0.159 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 31% cpu 0.157 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 31% cpu 0.161 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 30% cpu 0.163 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 31% cpu 0.158 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 30% cpu 0.166 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 30% cpu 0.165 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 31% cpu 0.159 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.02s user 0.03s system 30% cpu 0.161 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 23% cpu 0.157 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 23% cpu 0.153 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 24% cpu 0.153 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 23% cpu 0.156 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 23% cpu 0.155 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 23% cpu 0.154 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 23% cpu 0.156 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 24% cpu 0.158 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 23% cpu 0.156 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 24% cpu 0.155 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 25% cpu 0.155 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 25% cpu 0.157 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 23% cpu 0.161 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 23% cpu 0.155 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 25% cpu 0.155 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 22% cpu 0.165 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 23% cpu 0.155 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 24% cpu 0.157 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 23% cpu 0.155 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 23% cpu 0.155 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 24% cpu 0.154 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 23% cpu 0.155 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 23% cpu 0.155 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 23% cpu 0.155 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 24% cpu 0.156 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 23% cpu 0.157 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 23% cpu 0.155 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 25% cpu 0.154 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 22% cpu 0.170 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.02s user 0.02s system 24% cpu 0.156 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 12% cpu 0.251 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.01s user 0.02s system 12% cpu 0.250 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.01s user 0.02s system 11% cpu 0.251 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.01s user 0.01s system 11% cpu 0.247 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.01s system 11% cpu 0.249 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.01s system 12% cpu 0.249 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.01s system 12% cpu 0.248 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.01s system 11% cpu 0.258 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.01s system 12% cpu 0.250 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.01s system 11% cpu 0.248 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.01s system 12% cpu 0.247 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.01s user 0.01s system 11% cpu 0.262 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 12% cpu 0.251 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.01s user 0.02s system 12% cpu 0.248 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.01s system 12% cpu 0.247 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.01s user 0.01s system 11% cpu 0.260 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.01s system 11% cpu 0.244 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.01s system 11% cpu 0.246 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.01s system 12% cpu 0.248 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.01s system 11% cpu 0.245 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.01s system 11% cpu 0.247 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.01s system 11% cpu 0.247 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.01s system 11% cpu 0.248 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.01s system 11% cpu 0.247 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.01s system 12% cpu 0.248 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.01s system 12% cpu 0.247 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.01s system 11% cpu 0.245 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.01s system 11% cpu 0.247 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.01s system 12% cpu 0.247 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.01s system 11% cpu 0.246 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.36s user 0.69s system 96% cpu 1.088 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.36s user 0.70s system 99% cpu 1.068 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.35s user 0.65s system 99% cpu 1.007 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.35s user 0.65s system 99% cpu 1.003 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.36s user 0.64s system 99% cpu 1.007 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.36s user 0.64s system 99% cpu 1.006 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.36s user 0.65s system 99% cpu 1.012 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.36s user 0.66s system 99% cpu 1.020 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.36s user 0.64s system 99% cpu 1.003 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.35s user 0.64s system 99% cpu 0.998 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.36s user 0.65s system 99% cpu 1.008 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.36s user 0.65s system 99% cpu 1.013 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.35s user 0.65s system 99% cpu 1.003 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.35s user 0.64s system 99% cpu 1.001 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.35s user 0.66s system 99% cpu 1.017 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.35s user 0.64s system 99% cpu 0.999 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.36s user 0.65s system 99% cpu 1.011 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.35s user 0.64s system 99% cpu 0.999 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.36s user 0.64s system 99% cpu 1.000 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.35s user 0.67s system 99% cpu 1.027 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.35s user 0.68s system 99% cpu 1.033 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.36s user 0.68s system 99% cpu 1.041 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.35s user 0.68s system 99% cpu 1.035 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.35s user 0.68s system 99% cpu 1.034 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.35s user 0.66s system 99% cpu 1.015 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.35s user 0.64s system 99% cpu 0.997 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.36s user 0.66s system 99% cpu 1.017 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.35s user 0.65s system 99% cpu 1.011 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.35s user 0.66s system 99% cpu 1.018 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.37s user 0.65s system 99% cpu 1.022 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  29.41s user 0.13s system 34% cpu 1:25.69 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  30.50s user 0.18s system 0% cpu 54:08.04 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  29.30s user 0.08s system 3% cpu 16:10.36 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  30.06s user 0.15s system 15% cpu 3:20.02 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  29.60s user 0.13s system 4% cpu 10:04.31 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  30.15s user 0.23s system 27% cpu 1:48.68 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  29.68s user 0.10s system 12% cpu 3:50.69 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  29.53s user 0.16s system 17% cpu 2:53.53 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  29.45s user 0.15s system 4% cpu 11:10.65 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  30.12s user 0.23s system 2% cpu 21:47.65 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  29.34s user 0.09s system 2% cpu 18:15.70 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  29.75s user 0.15s system 6% cpu 8:08.03 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  29.70s user 0.16s system 2% cpu 19:56.76 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  31.02s user 0.20s system 3% cpu 13:12.55 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  29.72s user 0.07s system 2% cpu 23:03.19 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  31.38s user 0.11s system 1% cpu 27:08.97 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  31.72s user 0.16s system 1% cpu 26:54.44 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  30.73s user 0.12s system 1% cpu 36:46.54 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  29.55s user 0.11s system 1% cpu 27:13.77 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  29.87s user 0.05s system 1% cpu 27:07.97 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  30.03s user 0.08s system 0% cpu 54:00.32 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  30.28s user 0.16s system 1% cpu 43:33.50 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  29.61s user 0.09s system 1% cpu 37:58.88 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  29.30s user 0.11s system 1% cpu 40:37.50 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  29.87s user 0.10s system 0% cpu 54:02.29 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  30.43s user 0.18s system 0% cpu 54:07.06 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  29.31s user 0.08s system 1% cpu 40:33.27 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  29.18s user 0.11s system 1% cpu 27:09.04 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  29.49s user 0.10s system 1% cpu 44:11.47 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  30.21s user 0.21s system 1% cpu 38:07.21 total"""


print("8 workers")
par8 = []
for line in in_string.split("\n")[0:30]:
    s = line.split()
    if s[4] != "8":
        print (s[4])
    par8.append(s[13])

print("\n\n7 workers")
par7 = []
for line in in_string.split("\n")[30:60]:
    s = line.split()
    if s[4] != "7":
        print (s[4])
    par7.append(s[13])

print("\n\n6 workers")
par6 = []
for line in in_string.split("\n")[60:90]:
    s = line.split()
    if s[4] != "6":
        print( s[4])
    par6.append(s[13])

print("\n\n5 workers")
par5 = []
for line in in_string.split("\n")[90:120]:
    s = line.split()
    if s[4] != "5":
        print(s[4])
    par5.append(s[13])

print("4 workers")
par4 = []
for line in in_string.split("\n")[120:150]:
    s = line.split()
    if s[4] != "4":
        print (s[4])
    par4.append(s[13])

print("\n\n3 workers")
par3 = []
for line in in_string.split("\n")[150:180]:
    s = line.split()
    if s[4] != "3":
        print (s[4])
    par3.append(s[13])

print("\n\n2 workers")
par2 = []
for line in in_string.split("\n")[180:210]:
    s = line.split()
    if s[4] != "2":
        print( s[4])
    par2.append(s[13])

print("\n\n1 workers")
par1 = []
for line in in_string.split("\n")[210:240]:
    s = line.split()
    if s[4] != "1":
        print(s[4])
    par1.append(s[13])

print("\n\nstack seq")
stackseq = []
for line in in_string.split("\n")[240:270]:
    s = line.split()
    stackseq.append(s[12])

print("\n\nsequential")
seq = []
for line in in_string.split("\n")[270:300]:
    s = line.split()
    seq.append(s[12])
    print( s[12])

tr8 = []
for line in in_string.split("\n")[300:330]:
    s = line.split()
    tr8.append(s[13])
    print( s[13])
tr7 = []
for line in in_string.split("\n")[330:360]:
    s = line.split()
    tr7.append(s[13])
    print( s[13])
tr6 = []
for line in in_string.split("\n")[360:390]:
    s = line.split()
    tr6.append(s[13])
    print( s[13])
tr5 = []
for line in in_string.split("\n")[390:420]:
    s = line.split()
    tr5.append(s[13])
    print( s[13])
tr4 = []
for line in in_string.split("\n")[420:450]:
    s = line.split()
    tr4.append(s[13])
    print( s[13])
tr3 = []
for line in in_string.split("\n")[450:480]:
    s = line.split()
    tr3.append(s[13])
    print( s[13])
tr2 = []
for line in in_string.split("\n")[480:510]:
    s = line.split()
    tr2.append(s[13])
    print( s[13])
tr1 = []
for line in in_string.split("\n")[510:540]:
    s = line.split()
    tr1.append(s[13])
    print( s[13])
trstack = []
for line in in_string.split("\n")[540:570]:
    s = line.split()
    trstack.append(s[12])
    print( s[12])
trseq = []
for line in in_string.split("\n")[570:600]:
    s = line.split()
    trseq.append(s[12])
    print( s[12])

#########################################################

# print("8 workers")
# par8 = []
# for line in in_string.split("\n")[0:10]:
#     s = line.split()
#     if s[4] != "8":
#         print (s[4])
#     par8.append(s[13])

# print("\n\n7 workers")
# par7 = []
# for line in in_string.split("\n")[10:20]:
#     s = line.split()
#     if s[4] != "7":
#         print (s[4])
#     par7.append(s[13])

# print("\n\n6 workers")
# par6 = []
# for line in in_string.split("\n")[20:30]:
#     s = line.split()
#     if s[4] != "6":
#         print( s[4])
#     par6.append(s[13])

# print("\n\n5 workers")
# par5 = []
# for line in in_string.split("\n")[30:40]:
#     s = line.split()
#     if s[4] != "5":
#         print(s[4])
#     par5.append(s[13])

# print("4 workers")
# par4 = []
# for line in in_string.split("\n")[40:50]:
#     s = line.split()
#     if s[4] != "4":
#         print (s[4])
#     par4.append(s[13])

# print("\n\n3 workers")
# par3 = []
# for line in in_string.split("\n")[50:60]:
#     s = line.split()
#     if s[4] != "3":
#         print (s[4])
#     par3.append(s[13])

# print("\n\n2 workers")
# par2 = []
# for line in in_string.split("\n")[60:70]:
#     s = line.split()
#     if s[4] != "2":
#         print( s[4])
#     par2.append(s[13])

# print("\n\n1 workers")
# par1 = []
# for line in in_string.split("\n")[70:80]:
#     s = line.split()
#     if s[4] != "1":
#         print(s[4])
#     par1.append(s[13])

# print("\n\nstack seq")
# stackseq = []
# for line in in_string.split("\n")[80:90]:
#     s = line.split()
#     stackseq.append(s[12])

# print("\n\nsequential")
# seq = []
# for line in in_string.split("\n")[90:100]:
#     s = line.split()
#     seq.append(s[12])
#     print( s[12])

# tr8 = []
# for line in in_string.split("\n")[100:110]:
#     s = line.split()
#     tr8.append(s[13])
#     print( s[13])
# tr7 = []
# for line in in_string.split("\n")[110:120]:
#     s = line.split()
#     tr7.append(s[13])
#     print( s[13])
# tr6 = []
# for line in in_string.split("\n")[120:130]:
#     s = line.split()
#     tr6.append(s[13])
#     print( s[13])
# tr5 = []
# for line in in_string.split("\n")[130:140]:
#     s = line.split()
#     tr5.append(s[13])
#     print( s[13])
# tr4 = []
# for line in in_string.split("\n")[140:150]:
#     s = line.split()
#     tr4.append(s[13])
#     print( s[13])
# tr3 = []
# for line in in_string.split("\n")[150:160]:
#     s = line.split()
#     tr3.append(s[13])
#     print( s[13])
# tr2 = []
# for line in in_string.split("\n")[160:170]:
#     s = line.split()
#     tr2.append(s[13])
#     print( s[13])
# tr1 = []
# for line in in_string.split("\n")[170:180]:
#     s = line.split()
#     tr1.append(s[13])
#     print( s[13])
# trstack = []
# for line in in_string.split("\n")[180:190]:
#     s = line.split()
#     trstack.append(s[12])
#     print( s[12])
# trseq = []
# for line in in_string.split("\n")[190:200]:
#     s = line.split()
#     trseq.append(s[12])
#     print( s[12])




in_string2 = ""

swipl = []
for line in in_string2.split("\n"):
    s = line.split(' ')
    if len(s) > 0 and s[0] == "swipl":
        swipl.append(s[12])

with open("results.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([])
    writer.writerow(par8)
    writer.writerow(par7)
    writer.writerow(par6)
    writer.writerow(par5)
    writer.writerow(par4)
    writer.writerow(par3)
    writer.writerow(par2)
    writer.writerow(par1)
    writer.writerow(stackseq)
    writer.writerow(seq)
    writer.writerow(tr8)
    writer.writerow(tr7)
    writer.writerow(tr6)
    writer.writerow(tr5)
    writer.writerow(tr4)
    writer.writerow(tr3)
    writer.writerow(tr2)
    writer.writerow(tr1)
    writer.writerow(trstack)
    writer.writerow(trseq)
    writer.writerow(swipl)

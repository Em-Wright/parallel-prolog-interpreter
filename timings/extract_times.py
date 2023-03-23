import csv

in_string = """ ./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.64s user 0.59s system 8% cpu 13.649 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.62s user 0.53s system 8% cpu 13.331 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.61s user 0.53s system 8% cpu 13.297 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.63s user 0.57s system 8% cpu 13.406 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.64s user 0.60s system 9% cpu 13.444 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.64s user 0.57s system 8% cpu 13.434 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.65s user 0.61s system 9% cpu 13.474 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.65s user 0.60s system 9% cpu 13.648 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.64s user 0.60s system 9% cpu 13.518 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.62s user 0.55s system 8% cpu 13.349 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.61s user 0.53s system 8% cpu 13.263 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.63s user 0.57s system 8% cpu 13.417 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.63s user 0.58s system 8% cpu 13.483 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.64s user 0.61s system 9% cpu 13.605 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.63s user 0.56s system 8% cpu 13.424 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.62s user 0.54s system 8% cpu 13.266 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.62s user 0.53s system 8% cpu 13.272 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.62s user 0.54s system 8% cpu 13.373 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.62s user 0.55s system 8% cpu 13.358 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.63s user 0.55s system 8% cpu 13.359 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.63s user 0.58s system 9% cpu 13.478 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.63s user 0.55s system 8% cpu 13.361 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.62s user 0.55s system 8% cpu 13.315 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.63s user 0.55s system 8% cpu 13.340 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.61s user 0.55s system 8% cpu 13.296 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.61s user 0.54s system 8% cpu 13.292 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.63s user 0.56s system 8% cpu 13.387 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.63s user 0.57s system 8% cpu 13.399 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.63s user 0.57s system 8% cpu 13.491 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.62s user 0.55s system 8% cpu 13.313 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.58s user 0.49s system 8% cpu 13.293 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.59s user 0.49s system 8% cpu 13.309 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.59s user 0.50s system 8% cpu 13.347 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.60s user 0.51s system 8% cpu 13.376 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.59s user 0.51s system 8% cpu 13.371 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.56s user 0.49s system 7% cpu 13.325 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.58s user 0.49s system 8% cpu 13.339 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.58s user 0.49s system 8% cpu 13.251 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.58s user 0.48s system 7% cpu 13.232 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.58s user 0.49s system 8% cpu 13.265 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.60s user 0.51s system 8% cpu 13.423 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.58s user 0.48s system 7% cpu 13.240 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.58s user 0.48s system 7% cpu 13.226 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.58s user 0.47s system 7% cpu 13.212 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.60s user 0.52s system 8% cpu 13.313 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.58s user 0.49s system 8% cpu 13.299 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.59s user 0.50s system 8% cpu 13.327 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.59s user 0.51s system 8% cpu 13.351 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.57s user 0.47s system 7% cpu 13.246 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.58s user 0.49s system 8% cpu 13.228 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.58s user 0.49s system 8% cpu 13.274 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.58s user 0.50s system 8% cpu 13.283 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.57s user 0.49s system 7% cpu 13.324 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.60s user 0.53s system 8% cpu 13.395 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.58s user 0.49s system 8% cpu 13.356 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.58s user 0.48s system 8% cpu 13.273 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.58s user 0.47s system 7% cpu 13.199 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.59s user 0.50s system 8% cpu 13.293 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.58s user 0.49s system 8% cpu 13.265 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.58s user 0.50s system 8% cpu 13.276 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.56s user 0.47s system 7% cpu 13.379 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.53s user 0.44s system 7% cpu 13.280 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.54s user 0.43s system 7% cpu 13.227 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.55s user 0.44s system 7% cpu 13.265 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.55s user 0.45s system 7% cpu 13.319 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.55s user 0.44s system 7% cpu 13.273 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.56s user 0.46s system 7% cpu 13.333 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.57s user 0.47s system 7% cpu 13.433 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.54s user 0.44s system 7% cpu 13.289 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.55s user 0.43s system 7% cpu 13.236 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.55s user 0.44s system 7% cpu 13.258 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.55s user 0.45s system 7% cpu 13.352 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.55s user 0.45s system 7% cpu 13.255 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.56s user 0.47s system 7% cpu 13.413 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.55s user 0.45s system 7% cpu 13.367 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.26s user 0.26s system 0% cpu 54.967 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.58s user 0.51s system 8% cpu 13.592 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.55s user 0.45s system 7% cpu 13.435 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.55s user 0.44s system 7% cpu 13.277 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.55s user 0.44s system 7% cpu 13.247 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.56s user 0.45s system 7% cpu 13.355 total
./bin/parallel.exe -num-workers 4 -file "${PROG}" > timings.txt  0.55s user 0.44s system 7% cpu 13.242 total
./bin/parallel.exe -num-workers 4 -file "${PROG}" > timings.txt  0.55s user 0.45s system 7% cpu 13.321 total
./bin/parallel.exe -num-workers 4 -file "${PROG}" > timings.txt  0.55s user 0.43s system 7% cpu 13.250 total
./bin/parallel.exe -num-workers 4 -file "${PROG}" > timings.txt  0.55s user 0.45s system 7% cpu 13.301 total
./bin/parallel.exe -num-workers 4 -file "${PROG}" > timings.txt  0.56s user 0.46s system 7% cpu 13.417 total
./bin/parallel.exe -num-workers 4 -file "${PROG}" > timings.txt  0.54s user 0.43s system 7% cpu 13.273 total
./bin/parallel.exe -num-workers 4 -file "${PROG}" > timings.txt  0.55s user 0.44s system 7% cpu 13.209 total
./bin/parallel.exe -num-workers 4 -file "${PROG}" > timings.txt  0.56s user 0.45s system 7% cpu 13.331 total
./bin/parallel.exe -num-workers 4 -file "${PROG}" > timings.txt  0.56s user 0.46s system 7% cpu 13.413 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.51s user 0.40s system 6% cpu 13.294 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.52s user 0.40s system 6% cpu 13.249 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.53s user 0.43s system 7% cpu 13.456 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.53s user 0.41s system 7% cpu 13.354 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.52s user 0.39s system 6% cpu 13.251 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.52s user 0.40s system 6% cpu 13.308 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.52s user 0.41s system 6% cpu 13.312 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.50s user 0.39s system 6% cpu 13.265 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.53s user 0.41s system 7% cpu 13.326 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.53s user 0.42s system 7% cpu 13.419 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.51s user 0.38s system 6% cpu 13.205 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.51s user 0.38s system 6% cpu 13.232 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.52s user 0.40s system 6% cpu 13.283 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.53s user 0.41s system 7% cpu 13.333 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.51s user 0.39s system 6% cpu 13.229 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.53s user 0.42s system 7% cpu 13.360 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.52s user 0.40s system 6% cpu 13.328 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.52s user 0.40s system 6% cpu 13.268 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.52s user 0.40s system 6% cpu 13.307 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.53s user 0.41s system 7% cpu 13.358 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.52s user 0.40s system 6% cpu 13.275 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.53s user 0.42s system 7% cpu 13.354 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.54s user 0.43s system 7% cpu 13.412 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.52s user 0.40s system 6% cpu 13.277 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.52s user 0.40s system 6% cpu 13.286 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.52s user 0.40s system 6% cpu 13.261 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.52s user 0.40s system 6% cpu 13.297 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.51s user 0.40s system 6% cpu 13.219 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.54s user 0.42s system 7% cpu 13.377 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.52s user 0.41s system 6% cpu 13.344 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.66s user 0.06s system 98% cpu 3.759 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.59s user 0.06s system 99% cpu 3.648 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.52s user 0.04s system 99% cpu 3.559 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.52s user 0.04s system 99% cpu 3.556 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.50s user 0.04s system 99% cpu 3.539 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.53s user 0.04s system 99% cpu 3.569 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.50s user 0.04s system 99% cpu 3.544 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.50s user 0.05s system 99% cpu 3.545 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.49s user 0.05s system 99% cpu 3.546 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.50s user 0.07s system 99% cpu 3.572 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.49s user 0.04s system 99% cpu 3.534 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.53s user 0.05s system 99% cpu 3.579 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.50s user 0.05s system 99% cpu 3.554 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.51s user 0.05s system 99% cpu 3.560 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.59s user 0.04s system 99% cpu 3.631 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.51s user 0.07s system 99% cpu 3.584 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.52s user 0.05s system 99% cpu 3.577 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.52s user 0.06s system 99% cpu 3.579 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.51s user 0.06s system 99% cpu 3.572 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.66s user 0.08s system 99% cpu 3.750 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.53s user 0.06s system 99% cpu 3.591 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.49s user 0.07s system 99% cpu 3.562 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.51s user 0.06s system 99% cpu 3.567 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.49s user 0.04s system 99% cpu 3.534 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.50s user 0.04s system 99% cpu 3.536 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.49s user 0.04s system 99% cpu 3.534 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.50s user 0.04s system 99% cpu 3.543 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.48s user 0.04s system 99% cpu 3.526 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.51s user 0.04s system 99% cpu 3.557 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  3.52s user 0.04s system 99% cpu 3.560 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.52s user 0.42s system 10% cpu 8.619 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.56s user 0.47s system 11% cpu 8.855 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.53s user 0.42s system 11% cpu 8.612 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.52s user 0.41s system 10% cpu 8.514 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.52s user 0.42s system 11% cpu 8.479 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.55s user 0.49s system 11% cpu 8.700 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.54s user 0.49s system 11% cpu 8.695 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.55s user 0.45s system 11% cpu 8.743 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.52s user 0.41s system 10% cpu 8.532 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.52s user 0.43s system 11% cpu 8.517 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.53s user 0.46s system 11% cpu 8.595 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.52s user 0.41s system 10% cpu 8.568 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.52s user 0.44s system 11% cpu 8.595 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.52s user 0.41s system 10% cpu 8.482 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.52s user 0.45s system 11% cpu 8.532 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.53s user 0.44s system 11% cpu 8.627 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.54s user 0.47s system 11% cpu 8.693 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.53s user 0.42s system 11% cpu 8.602 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.51s user 0.44s system 11% cpu 8.497 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.55s user 0.48s system 11% cpu 8.673 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.54s user 0.45s system 11% cpu 8.677 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.51s user 0.41s system 10% cpu 8.496 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.54s user 0.47s system 11% cpu 8.694 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.54s user 0.44s system 11% cpu 8.645 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.52s user 0.42s system 10% cpu 8.574 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.52s user 0.44s system 11% cpu 8.515 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.52s user 0.44s system 11% cpu 8.569 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.53s user 0.43s system 11% cpu 8.653 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.53s user 0.44s system 11% cpu 8.691 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.52s user 0.43s system 11% cpu 8.655 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.51s user 0.38s system 10% cpu 8.624 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.50s user 0.41s system 10% cpu 8.540 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.50s user 0.40s system 10% cpu 8.569 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.51s user 0.40s system 10% cpu 8.635 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.50s user 0.38s system 10% cpu 8.532 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.49s user 0.40s system 10% cpu 8.509 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.51s user 0.41s system 10% cpu 8.579 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.51s user 0.41s system 10% cpu 8.581 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.51s user 0.42s system 10% cpu 8.606 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.50s user 0.40s system 10% cpu 8.641 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.50s user 0.37s system 10% cpu 8.514 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.50s user 0.42s system 10% cpu 8.525 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.49s user 0.37s system 10% cpu 8.495 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.50s user 0.38s system 10% cpu 8.568 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.50s user 0.40s system 10% cpu 8.568 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.50s user 0.38s system 10% cpu 8.504 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.52s user 0.41s system 10% cpu 8.725 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.52s user 0.42s system 10% cpu 8.690 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.51s user 0.41s system 10% cpu 8.699 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.51s user 0.40s system 10% cpu 8.712 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.50s user 0.40s system 10% cpu 8.563 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.51s user 0.41s system 10% cpu 8.645 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.52s user 0.40s system 10% cpu 8.633 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.50s user 0.38s system 10% cpu 8.536 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.51s user 0.40s system 10% cpu 8.618 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.50s user 0.40s system 10% cpu 8.520 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.50s user 0.39s system 10% cpu 8.574 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.50s user 0.42s system 10% cpu 8.557 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.51s user 0.41s system 10% cpu 8.610 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.51s user 0.42s system 10% cpu 8.605 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.48s user 0.36s system 9% cpu 8.527 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.47s user 0.35s system 9% cpu 8.463 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.47s user 0.35s system 9% cpu 8.506 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.47s user 0.34s system 9% cpu 8.494 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.47s user 0.35s system 9% cpu 8.515 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.47s user 0.36s system 9% cpu 8.558 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.48s user 0.36s system 9% cpu 8.550 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.47s user 0.36s system 9% cpu 8.592 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.48s user 0.35s system 9% cpu 8.642 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.48s user 0.37s system 9% cpu 8.606 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.48s user 0.36s system 9% cpu 8.676 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.47s user 0.36s system 9% cpu 8.561 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.47s user 0.35s system 9% cpu 8.519 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.47s user 0.35s system 9% cpu 8.506 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.47s user 0.36s system 9% cpu 8.509 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.48s user 0.38s system 9% cpu 8.625 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.48s user 0.36s system 9% cpu 8.566 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.47s user 0.35s system 9% cpu 8.549 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.48s user 0.36s system 9% cpu 8.557 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.49s user 0.37s system 9% cpu 8.627 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.49s user 0.38s system 9% cpu 8.689 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.47s user 0.36s system 9% cpu 8.567 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.47s user 0.35s system 9% cpu 8.521 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.47s user 0.35s system 9% cpu 8.540 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.47s user 0.35s system 9% cpu 8.485 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.47s user 0.35s system 9% cpu 8.569 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.48s user 0.36s system 9% cpu 8.561 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.48s user 0.37s system 9% cpu 8.584 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.48s user 0.36s system 9% cpu 8.575 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.50s user 0.39s system 10% cpu 8.667 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.49s user 0.36s system 9% cpu 8.760 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.47s user 0.33s system 9% cpu 8.686 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.46s user 0.32s system 8% cpu 8.668 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.44s user 0.30s system 8% cpu 8.483 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.45s user 0.31s system 8% cpu 8.504 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.45s user 0.31s system 8% cpu 8.477 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.46s user 0.32s system 9% cpu 8.535 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.45s user 0.31s system 8% cpu 8.576 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.45s user 0.31s system 8% cpu 8.534 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.46s user 0.32s system 9% cpu 8.555 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.46s user 0.33s system 9% cpu 8.576 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.45s user 0.32s system 8% cpu 8.556 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.44s user 0.29s system 8% cpu 8.460 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.45s user 0.31s system 8% cpu 8.496 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.45s user 0.31s system 8% cpu 8.555 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.46s user 0.32s system 9% cpu 8.584 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.48s user 0.34s system 9% cpu 8.706 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.45s user 0.31s system 8% cpu 8.543 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.45s user 0.31s system 8% cpu 8.557 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.45s user 0.31s system 8% cpu 8.538 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.46s user 0.32s system 9% cpu 8.575 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.46s user 0.32s system 9% cpu 8.615 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.46s user 0.32s system 9% cpu 8.599 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.45s user 0.31s system 8% cpu 8.526 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.45s user 0.31s system 8% cpu 8.640 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.44s user 0.31s system 8% cpu 8.519 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.45s user 0.31s system 8% cpu 8.574 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.45s user 0.32s system 8% cpu 8.522 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.46s user 0.32s system 9% cpu 8.587 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.48s user 0.35s system 9% cpu 8.694 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.01s system 6% cpu 0.214 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 85% cpu 0.007 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 86% cpu 0.007 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 85% cpu 0.007 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 87% cpu 0.006 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 85% cpu 0.006 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 86% cpu 0.006 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 84% cpu 0.007 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 85% cpu 0.007 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 86% cpu 0.006 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 86% cpu 0.006 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 87% cpu 0.006 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 87% cpu 0.007 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 86% cpu 0.006 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 85% cpu 0.006 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 86% cpu 0.007 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 85% cpu 0.006 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 86% cpu 0.006 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 85% cpu 0.006 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 85% cpu 0.007 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 86% cpu 0.006 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 86% cpu 0.006 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 87% cpu 0.006 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 86% cpu 0.006 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 85% cpu 0.007 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 85% cpu 0.007 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 86% cpu 0.006 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 86% cpu 0.006 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 85% cpu 0.006 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.00s user 0.00s system 86% cpu 0.006 total
"""




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

print("\n\nsequential")
seq = []
for line in in_string.split("\n")[120:150]:
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
    s = line.split()
    trseq.append(s[12])
    print( s[12])

in_string2 = """
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 78% cpu 0.121 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.095 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.094 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.095 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.094 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.094 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.097 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 97% cpu 0.095 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.096 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 97% cpu 0.095 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.094 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 97% cpu 0.094 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.095 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.094 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.095 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.093 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.093 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.094 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.094 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.094 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 92% cpu 0.098 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.095 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.094 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.094 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.094 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.094 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.094 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.094 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.096 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.07s user 0.02s system 96% cpu 0.095 total"""

swipl = []
for line in in_string2.split("\n"):
    s = line.split(' ')
    if len(s) > 0 and s[0] == "swipl":
        swipl.append(s[12])

with open("fib25.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([])
    writer.writerow(["fib25"])
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

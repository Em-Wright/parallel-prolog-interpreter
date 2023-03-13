import csv


in_string = """./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.14s system 14% cpu 1.654 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.13s system 14% cpu 1.616 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.13s system 13% cpu 1.666 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.592 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.595 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.09s user 0.12s system 13% cpu 1.593 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.13s system 13% cpu 1.698 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.645 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.09s user 0.12s system 12% cpu 1.608 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.09s user 0.13s system 13% cpu 1.686 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.09s user 0.11s system 12% cpu 1.686 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.09s user 0.11s system 12% cpu 1.604 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.609 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.606 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.13s system 13% cpu 1.658 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.09s user 0.12s system 13% cpu 1.626 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.09s user 0.12s system 13% cpu 1.596 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.632 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.09s user 0.12s system 12% cpu 1.621 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 11% cpu 1.873 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.09s user 0.11s system 12% cpu 1.653 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.624 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.600 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.594 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.603 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.600 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.642 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.13s system 14% cpu 1.601 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.09s user 0.12s system 12% cpu 1.664 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.600 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.10s user 0.13s system 13% cpu 1.776 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.13s system 13% cpu 1.870 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.10s user 0.13s system 11% cpu 1.978 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.10s user 0.12s system 12% cpu 1.819 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.14s system 14% cpu 1.771 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.15s system 14% cpu 1.845 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.15s system 13% cpu 1.977 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.15s system 14% cpu 1.814 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.15s system 14% cpu 1.795 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.15s system 14% cpu 1.798 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.15s system 14% cpu 1.788 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.15s system 14% cpu 1.800 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.15s system 14% cpu 1.800 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.15s system 13% cpu 1.902 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.15s system 13% cpu 1.909 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.16s system 14% cpu 1.958 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.15s system 14% cpu 1.850 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.14s system 14% cpu 1.828 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.14s system 14% cpu 1.811 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.15s system 15% cpu 1.824 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.15s system 14% cpu 1.790 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.17s system 14% cpu 1.988 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.16s system 13% cpu 2.021 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.14s system 13% cpu 1.915 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.14s system 14% cpu 1.791 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.16s system 15% cpu 1.847 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.14s system 14% cpu 1.791 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.14s system 13% cpu 1.871 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.16s system 13% cpu 1.995 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.15s system 13% cpu 1.898 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.10s system 7% cpu 2.617 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.10s system 7% cpu 2.626 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.11s system 7% cpu 2.623 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.13s system 8% cpu 2.631 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.12s system 7% cpu 2.638 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.11s system 7% cpu 2.617 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.10s system 7% cpu 2.607 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.10s system 7% cpu 2.608 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.10s system 7% cpu 2.601 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.10s system 7% cpu 2.614 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.11s system 7% cpu 2.631 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.10s user 0.14s system 9% cpu 2.702 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.10s user 0.14s system 9% cpu 2.707 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.12s system 8% cpu 2.651 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.08s user 0.10s system 6% cpu 2.609 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.11s system 7% cpu 2.620 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.11s system 7% cpu 2.622 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.10s system 7% cpu 2.602 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.10s system 7% cpu 2.605 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.10s system 7% cpu 2.609 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.10s user 0.12s system 8% cpu 2.629 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.10s system 7% cpu 2.608 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.11s system 7% cpu 2.617 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.11s system 7% cpu 2.703 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.10s user 0.13s system 8% cpu 2.668 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.13s system 8% cpu 2.646 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.10s user 0.11s system 7% cpu 2.618 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.11s system 7% cpu 2.614 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.10s user 0.12s system 8% cpu 2.625 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.11s system 7% cpu 2.623 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.11s user 0.15s system 4% cpu 5.127 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.09s user 0.15s system 4% cpu 5.106 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.10s user 0.15s system 4% cpu 5.127 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.09s user 0.15s system 4% cpu 5.113 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.11s user 0.15s system 5% cpu 5.137 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.11s user 0.15s system 5% cpu 5.156 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.11s user 0.16s system 5% cpu 5.147 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.12s user 0.15s system 5% cpu 5.181 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.11s user 0.15s system 5% cpu 5.164 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.12s user 0.16s system 5% cpu 5.157 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.09s user 0.15s system 4% cpu 5.112 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.12s user 0.16s system 5% cpu 5.153 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.12s user 0.15s system 5% cpu 5.140 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.13s user 0.16s system 5% cpu 5.170 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.13s user 0.16s system 5% cpu 5.183 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.13s user 0.16s system 5% cpu 5.182 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.12s user 0.16s system 5% cpu 5.223 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.11s user 0.15s system 4% cpu 5.139 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.09s user 0.15s system 4% cpu 5.122 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.09s user 0.15s system 4% cpu 5.126 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.10s user 0.15s system 4% cpu 5.132 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.10s user 0.15s system 4% cpu 5.134 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.09s user 0.15s system 4% cpu 5.130 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.13s user 0.17s system 5% cpu 5.198 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.10s user 0.15s system 4% cpu 5.136 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.12s user 0.16s system 5% cpu 5.157 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.09s user 0.15s system 4% cpu 5.120 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.12s user 0.16s system 5% cpu 5.159 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.11s user 0.16s system 5% cpu 5.156 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.13s user 0.16s system 5% cpu 5.157 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.45s user 0.14s system 99% cpu 10.626 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.49s user 0.06s system 99% cpu 10.559 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.53s user 0.05s system 99% cpu 10.579 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.51s user 0.05s system 99% cpu 10.559 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.51s user 0.10s system 99% cpu 10.614 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.50s user 0.07s system 99% cpu 10.575 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.45s user 0.06s system 99% cpu 10.510 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.47s user 0.12s system 99% cpu 10.600 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.50s user 0.10s system 99% cpu 10.605 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.47s user 0.03s system 99% cpu 10.498 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.54s user 0.05s system 99% cpu 10.602 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.52s user 0.05s system 99% cpu 10.581 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.46s user 0.06s system 99% cpu 10.526 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.48s user 0.05s system 99% cpu 10.526 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.46s user 0.09s system 99% cpu 10.550 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.43s user 0.13s system 99% cpu 10.566 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.47s user 0.05s system 99% cpu 10.529 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.45s user 0.04s system 99% cpu 10.490 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.45s user 0.03s system 99% cpu 10.480 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.46s user 0.07s system 99% cpu 10.539 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.44s user 0.04s system 99% cpu 10.535 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.48s user 0.06s system 99% cpu 10.550 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.53s user 0.12s system 99% cpu 10.650 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.51s user 0.07s system 99% cpu 10.591 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.43s user 0.03s system 99% cpu 10.465 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.48s user 0.04s system 99% cpu 10.531 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.49s user 0.05s system 99% cpu 10.545 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.47s user 0.08s system 99% cpu 10.556 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.53s user 0.06s system 99% cpu 10.606 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.49s user 0.09s system 99% cpu 10.588 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.14s user 0.21s system 9% cpu 3.648 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.15s user 0.20s system 9% cpu 3.559 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.14s user 0.19s system 9% cpu 3.582 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.15s user 0.20s system 9% cpu 3.674 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.16s user 0.21s system 9% cpu 3.778 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.14s user 0.19s system 9% cpu 3.615 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.14s user 0.19s system 9% cpu 3.541 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.14s user 0.19s system 9% cpu 3.571 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.14s user 0.19s system 8% cpu 3.730 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.15s user 0.20s system 9% cpu 3.599 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.15s user 0.20s system 8% cpu 4.134 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.15s user 0.20s system 9% cpu 3.765 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.16s user 0.21s system 8% cpu 4.052 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.14s user 0.19s system 9% cpu 3.447 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.14s user 0.19s system 9% cpu 3.491 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.15s user 0.20s system 9% cpu 3.751 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.15s user 0.21s system 8% cpu 4.072 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.13s user 0.18s system 9% cpu 3.449 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.14s user 0.19s system 9% cpu 3.539 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.14s user 0.19s system 9% cpu 3.534 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.15s user 0.20s system 9% cpu 3.779 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.15s user 0.19s system 9% cpu 3.560 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.14s user 0.19s system 8% cpu 3.711 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.14s user 0.19s system 9% cpu 3.669 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.14s user 0.18s system 9% cpu 3.444 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.15s user 0.19s system 9% cpu 3.623 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.14s user 0.19s system 9% cpu 3.590 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.14s user 0.19s system 9% cpu 3.409 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.14s user 0.18s system 9% cpu 3.545 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.14s user 0.19s system 9% cpu 3.413 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.19s user 0.25s system 10% cpu 4.145 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.20s user 0.28s system 11% cpu 4.078 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.18s user 0.25s system 10% cpu 4.028 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.18s user 0.24s system 10% cpu 4.022 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.17s user 0.24s system 10% cpu 4.047 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.17s user 0.24s system 10% cpu 4.086 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.17s user 0.23s system 10% cpu 4.044 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.18s user 0.24s system 9% cpu 4.176 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.17s user 0.24s system 9% cpu 4.114 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.18s user 0.26s system 10% cpu 4.122 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.18s user 0.24s system 10% cpu 4.123 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.18s user 0.24s system 9% cpu 4.410 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.18s user 0.25s system 9% cpu 4.382 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.18s user 0.26s system 10% cpu 4.106 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.17s user 0.25s system 10% cpu 4.059 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.19s user 0.27s system 11% cpu 4.109 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.19s user 0.28s system 11% cpu 4.069 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.18s user 0.25s system 10% cpu 4.061 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.18s user 0.27s system 10% cpu 4.178 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.19s user 0.27s system 11% cpu 4.140 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.18s user 0.26s system 10% cpu 4.106 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.19s user 0.26s system 11% cpu 4.031 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.20s user 0.26s system 11% cpu 3.876 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.21s user 0.28s system 12% cpu 3.929 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.21s user 0.29s system 12% cpu 3.984 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.20s user 0.28s system 12% cpu 3.919 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.18s user 0.25s system 10% cpu 4.023 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.18s user 0.26s system 11% cpu 4.035 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.20s user 0.27s system 11% cpu 3.988 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.21s user 0.29s system 12% cpu 3.855 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.17s user 0.22s system 7% cpu 5.586 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.17s user 0.22s system 6% cpu 5.571 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.17s user 0.22s system 6% cpu 5.975 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.16s user 0.21s system 6% cpu 5.592 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.16s user 0.23s system 6% cpu 5.797 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.15s user 0.20s system 6% cpu 5.558 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.16s user 0.20s system 6% cpu 5.551 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.15s user 0.20s system 6% cpu 5.555 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.16s user 0.21s system 6% cpu 5.575 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.17s user 0.22s system 6% cpu 5.600 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.16s user 0.22s system 6% cpu 5.604 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.16s user 0.21s system 6% cpu 5.559 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.15s user 0.21s system 6% cpu 5.568 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.16s user 0.21s system 6% cpu 5.585 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.18s user 0.26s system 7% cpu 5.639 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.17s user 0.22s system 6% cpu 5.607 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.17s user 0.22s system 6% cpu 5.564 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.17s user 0.22s system 7% cpu 5.601 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.17s user 0.22s system 7% cpu 5.612 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.15s user 0.20s system 6% cpu 5.556 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.16s user 0.20s system 6% cpu 5.565 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.15s user 0.19s system 6% cpu 5.540 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.15s user 0.19s system 6% cpu 5.555 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.15s user 0.19s system 6% cpu 5.554 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.17s user 0.22s system 6% cpu 5.588 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.15s user 0.20s system 6% cpu 5.545 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.16s user 0.21s system 6% cpu 5.576 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.15s user 0.20s system 6% cpu 5.532 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.17s user 0.22s system 6% cpu 5.780 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.16s user 0.22s system 6% cpu 5.569 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.26s user 0.29s system 4% cpu 11.029 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.25s user 0.28s system 4% cpu 11.073 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.23s user 0.27s system 4% cpu 10.950 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.23s user 0.27s system 4% cpu 10.932 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.24s user 0.28s system 4% cpu 10.989 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.24s user 0.27s system 4% cpu 10.940 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.25s user 0.28s system 4% cpu 10.993 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.26s user 0.29s system 4% cpu 11.006 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.25s user 0.28s system 4% cpu 10.985 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.23s user 0.27s system 4% cpu 10.923 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.23s user 0.27s system 4% cpu 10.936 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.24s user 0.28s system 4% cpu 10.987 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.24s user 0.29s system 4% cpu 11.003 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.24s user 0.29s system 4% cpu 10.964 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.26s user 0.30s system 5% cpu 11.036 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.26s user 0.29s system 4% cpu 11.023 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.24s user 0.27s system 4% cpu 10.950 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.24s user 0.28s system 4% cpu 10.972 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.24s user 0.28s system 4% cpu 11.000 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.25s user 0.30s system 4% cpu 11.060 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.24s user 0.28s system 4% cpu 10.981 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.25s user 0.29s system 4% cpu 10.993 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.26s user 0.30s system 5% cpu 11.036 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.24s user 0.28s system 4% cpu 10.986 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.24s user 0.28s system 4% cpu 10.955 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.24s user 0.28s system 4% cpu 10.976 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.25s user 0.30s system 4% cpu 11.003 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.24s user 0.28s system 4% cpu 10.950 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.26s user 0.30s system 5% cpu 11.049 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.26s user 0.30s system 5% cpu 11.080 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.13s user 0.05s system 99% cpu 6.217 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.10s user 0.02s system 99% cpu 6.125 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.02s user 0.02s system 99% cpu 6.042 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.00s user 0.02s system 99% cpu 6.025 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.00s user 0.02s system 99% cpu 6.023 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.11s user 0.02s system 99% cpu 6.134 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.02s user 0.06s system 99% cpu 6.083 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.01s user 0.04s system 99% cpu 6.060 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.37s user 0.03s system 99% cpu 6.405 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.02s user 0.01s system 99% cpu 6.034 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  5.99s user 0.04s system 99% cpu 6.029 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  5.98s user 0.07s system 99% cpu 6.055 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.08s user 0.07s system 99% cpu 6.150 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.04s user 0.03s system 98% cpu 6.156 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.08s user 0.01s system 99% cpu 6.095 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  5.99s user 0.02s system 99% cpu 6.013 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  5.99s user 0.02s system 99% cpu 6.008 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  5.99s user 0.03s system 99% cpu 6.020 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.07s user 0.02s system 99% cpu 6.101 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.08s user 0.03s system 99% cpu 6.127 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.06s user 0.02s system 99% cpu 6.082 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.03s user 0.04s system 99% cpu 6.074 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.05s user 0.03s system 99% cpu 6.088 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.15s user 0.05s system 99% cpu 6.202 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.13s user 0.06s system 99% cpu 6.197 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.01s user 0.08s system 99% cpu 6.094 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.11s user 0.07s system 99% cpu 6.184 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.00s user 0.02s system 99% cpu 6.030 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.01s user 0.03s system 99% cpu 6.035 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.03s user 0.02s system 99% cpu 6.058 total
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
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.01s system 53% cpu 0.246 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.129 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 97% cpu 0.129 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.127 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 97% cpu 0.128 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.128 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.128 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 97% cpu 0.128 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.128 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.128 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.127 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.127 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.127 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.128 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.01s system 98% cpu 0.128 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.128 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.127 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.127 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.127 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.127 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.127 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.127 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.128 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.129 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.127 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.127 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.127 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.127 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.00s system 98% cpu 0.129 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:14:
Warning:    Singleton variables: [Y,X]
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_nqueensgen.pl:17:
Warning:    Singleton variables: [L]
swipl -q "${SWIPROG}" > timings.txt  0.12s user 0.01s system 98% cpu 0.128 total
"""

swipl = []
for line in in_string2.split("\n"):
    s = line.split(' ')
    if len(s) > 0 and s[0] == "swipl":
        swipl.append(s[12])

with open("nqueens.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([])
    writer.writerow(["8queens"])
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

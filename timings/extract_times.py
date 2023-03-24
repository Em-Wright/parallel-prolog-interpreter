import csv

in_string = """ ./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.13s system 13% cpu 1.620 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 14% cpu 1.566 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 14% cpu 1.573 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.09s user 0.11s system 12% cpu 1.576 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.676 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.611 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.11s system 13% cpu 1.539 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.555 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.580 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.600 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 14% cpu 1.569 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.605 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.11s system 13% cpu 1.560 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.624 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.09s user 0.11s system 12% cpu 1.564 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 14% cpu 1.553 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 14% cpu 1.533 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.09s user 0.11s system 13% cpu 1.553 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.561 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 14% cpu 1.568 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.599 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 14% cpu 1.553 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 14% cpu 1.602 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.13s system 14% cpu 1.577 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.542 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.13s system 14% cpu 1.610 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 13% cpu 1.585 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 14% cpu 1.553 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.12s system 14% cpu 1.559 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.10s user 0.11s system 13% cpu 1.605 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.14s system 14% cpu 1.746 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.13s system 13% cpu 1.734 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.13s system 14% cpu 1.720 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.13s system 14% cpu 1.757 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.13s system 14% cpu 1.733 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.13s system 14% cpu 1.740 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.13s system 13% cpu 1.720 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.13s system 13% cpu 1.751 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.14s system 14% cpu 1.781 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.14s system 15% cpu 1.759 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.14s system 14% cpu 1.774 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.14s system 14% cpu 1.761 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.13s system 13% cpu 1.757 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.13s system 14% cpu 1.719 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.13s system 13% cpu 1.756 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.13s system 14% cpu 1.731 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.13s system 13% cpu 1.749 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.13s system 14% cpu 1.743 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.13s system 14% cpu 1.724 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.13s system 14% cpu 1.709 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.13s system 14% cpu 1.718 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.13s system 13% cpu 1.730 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.13s system 14% cpu 1.723 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.15s system 15% cpu 1.767 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.14s system 14% cpu 1.753 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.15s system 15% cpu 1.778 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.12s user 0.15s system 14% cpu 1.805 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.13s system 12% cpu 1.873 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.13s system 13% cpu 1.799 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.11s user 0.13s system 13% cpu 1.757 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.08s user 0.10s system 7% cpu 2.568 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.10s user 0.13s system 8% cpu 2.552 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.12s system 8% cpu 2.573 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.12s system 8% cpu 2.547 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.08s user 0.10s system 7% cpu 2.515 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.12s system 8% cpu 2.576 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.10s user 0.13s system 9% cpu 2.539 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.12s system 8% cpu 2.562 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.11s system 8% cpu 2.520 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.11s system 8% cpu 2.531 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.10s system 7% cpu 2.528 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.10s user 0.12s system 8% cpu 2.528 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.11s system 8% cpu 2.568 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.10s system 7% cpu 2.533 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.08s user 0.10s system 7% cpu 2.568 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.08s user 0.10s system 7% cpu 2.510 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.11s system 7% cpu 2.578 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.08s user 0.11s system 7% cpu 2.516 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.10s system 7% cpu 2.510 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.10s system 7% cpu 2.559 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.11s system 7% cpu 2.539 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.10s system 7% cpu 2.576 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.11s system 7% cpu 2.575 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.11s system 7% cpu 2.520 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.10s user 0.12s system 8% cpu 2.609 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.11s system 7% cpu 2.531 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.10s system 7% cpu 2.541 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.11s system 7% cpu 2.554 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.11s system 8% cpu 2.518 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.09s user 0.10s system 7% cpu 2.518 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.10s user 0.14s system 5% cpu 4.903 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.11s user 0.15s system 5% cpu 4.888 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.09s user 0.14s system 4% cpu 4.871 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.09s user 0.14s system 4% cpu 4.873 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.11s user 0.15s system 5% cpu 4.895 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.09s user 0.15s system 4% cpu 4.873 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.11s user 0.15s system 5% cpu 4.904 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.12s user 0.15s system 5% cpu 4.927 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.13s user 0.15s system 5% cpu 4.942 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.12s user 0.16s system 5% cpu 4.912 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.12s user 0.15s system 5% cpu 4.927 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.10s user 0.14s system 5% cpu 4.902 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.09s user 0.14s system 4% cpu 4.874 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.09s user 0.15s system 4% cpu 4.896 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.10s user 0.14s system 4% cpu 4.908 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.09s user 0.14s system 4% cpu 4.862 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.09s user 0.14s system 4% cpu 4.863 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.09s user 0.14s system 4% cpu 4.877 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.09s user 0.14s system 4% cpu 4.872 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.09s user 0.14s system 4% cpu 4.891 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.12s user 0.16s system 5% cpu 4.910 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.09s user 0.15s system 4% cpu 4.893 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.12s user 0.15s system 5% cpu 4.949 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.10s user 0.15s system 5% cpu 4.906 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.08s user 0.14s system 4% cpu 4.874 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.10s user 0.15s system 5% cpu 4.881 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.10s user 0.15s system 4% cpu 4.876 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.10s user 0.15s system 4% cpu 4.881 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.11s user 0.15s system 5% cpu 4.889 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.11s user 0.15s system 5% cpu 4.879 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.44s user 0.12s system 99% cpu 10.602 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.45s user 0.02s system 99% cpu 10.479 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.53s user 0.02s system 99% cpu 10.558 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.58s user 0.02s system 99% cpu 10.605 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.57s user 0.06s system 99% cpu 10.641 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.48s user 0.04s system 99% cpu 10.523 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.57s user 0.05s system 99% cpu 10.628 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.43s user 0.04s system 99% cpu 10.482 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.44s user 0.05s system 99% cpu 10.490 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.52s user 0.12s system 99% cpu 10.649 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.47s user 0.08s system 99% cpu 10.549 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.44s user 0.02s system 99% cpu 10.461 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.49s user 0.03s system 99% cpu 10.523 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.59s user 0.05s system 99% cpu 10.646 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.46s user 0.10s system 99% cpu 10.560 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.44s user 0.05s system 99% cpu 10.496 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.44s user 0.04s system 99% cpu 10.476 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.47s user 0.09s system 99% cpu 10.566 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.46s user 0.09s system 99% cpu 10.553 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.45s user 0.10s system 99% cpu 10.564 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.49s user 0.02s system 99% cpu 10.512 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.54s user 0.05s system 99% cpu 10.588 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.55s user 0.05s system 99% cpu 10.607 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.46s user 0.08s system 99% cpu 10.539 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.49s user 0.06s system 99% cpu 10.555 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.52s user 0.03s system 99% cpu 10.552 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.43s user 0.05s system 99% cpu 10.481 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.48s user 0.08s system 99% cpu 10.562 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.48s user 0.12s system 99% cpu 10.610 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  10.48s user 0.03s system 99% cpu 10.511 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.09s user 0.12s system 24% cpu 0.827 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 22% cpu 0.776 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 22% cpu 0.787 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 21% cpu 0.776 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 23% cpu 0.785 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 22% cpu 0.831 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.09s user 0.10s system 24% cpu 0.785 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 23% cpu 0.794 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 20% cpu 0.853 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 20% cpu 0.805 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 21% cpu 0.830 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 20% cpu 0.812 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 22% cpu 0.785 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 22% cpu 0.789 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 21% cpu 0.829 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 21% cpu 0.804 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 21% cpu 0.829 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 21% cpu 0.854 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 18% cpu 0.959 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 18% cpu 0.888 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.08s system 19% cpu 0.836 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 22% cpu 0.774 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.08s system 21% cpu 0.775 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 20% cpu 0.786 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 20% cpu 0.824 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 21% cpu 0.777 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 21% cpu 0.819 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 21% cpu 0.819 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.08s system 20% cpu 0.809 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 19% cpu 0.908 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 15% cpu 0.900 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 19% cpu 0.864 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 19% cpu 0.856 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 18% cpu 0.865 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 17% cpu 0.936 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.08s system 17% cpu 0.922 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 19% cpu 0.856 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 19% cpu 0.855 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 19% cpu 0.866 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.09s system 18% cpu 0.885 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.08s system 17% cpu 0.902 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 19% cpu 0.864 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.09s system 18% cpu 0.878 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.09s system 18% cpu 0.887 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 18% cpu 0.945 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 19% cpu 0.877 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 19% cpu 0.889 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 18% cpu 0.869 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 18% cpu 0.875 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 19% cpu 0.859 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 19% cpu 0.873 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.08s system 17% cpu 0.888 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 19% cpu 0.853 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 19% cpu 0.887 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 19% cpu 0.865 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 18% cpu 0.857 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 18% cpu 0.881 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 19% cpu 0.864 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 18% cpu 0.872 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 19% cpu 0.855 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 9% cpu 1.214 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 9% cpu 1.226 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.07s system 10% cpu 1.222 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.07s system 9% cpu 1.229 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 9% cpu 1.220 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 9% cpu 1.224 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 9% cpu 1.214 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 9% cpu 1.234 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.07s system 10% cpu 1.233 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.07s system 9% cpu 1.245 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 9% cpu 1.221 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.07s system 10% cpu 1.226 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.07s system 10% cpu 1.234 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.08s system 11% cpu 1.243 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.08s system 11% cpu 1.235 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.08s system 11% cpu 1.237 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.08s system 10% cpu 1.231 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.07s system 9% cpu 1.242 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.07s system 9% cpu 1.223 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.07s system 9% cpu 1.240 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.07s system 10% cpu 1.244 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.08s system 10% cpu 1.264 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.07s system 10% cpu 1.238 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.07s system 10% cpu 1.257 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.08s system 10% cpu 1.249 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.08s system 11% cpu 1.234 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.08s system 11% cpu 1.241 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 9% cpu 1.215 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 9% cpu 1.210 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 9% cpu 1.233 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.08s system 5% cpu 2.337 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.08s system 5% cpu 2.343 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.08s system 5% cpu 2.329 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.06s user 0.08s system 6% cpu 2.349 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.07s user 0.08s system 6% cpu 2.362 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.06s user 0.08s system 5% cpu 2.326 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.08s system 5% cpu 2.327 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.06s user 0.08s system 6% cpu 2.373 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.07s user 0.08s system 6% cpu 2.357 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.06s user 0.08s system 5% cpu 2.356 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.08s system 5% cpu 2.359 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.07s user 0.09s system 6% cpu 2.368 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.08s user 0.09s system 6% cpu 2.390 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.06s user 0.08s system 6% cpu 2.347 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.07s user 0.08s system 6% cpu 2.356 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.07s user 0.08s system 6% cpu 2.379 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.07s user 0.08s system 6% cpu 2.391 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.06s user 0.08s system 5% cpu 2.338 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.06s user 0.08s system 5% cpu 2.339 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.06s user 0.07s system 5% cpu 2.351 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.08s system 5% cpu 2.350 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.08s system 5% cpu 2.334 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.06s user 0.07s system 5% cpu 2.353 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.06s user 0.08s system 5% cpu 2.333 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.08s system 5% cpu 2.344 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.08s system 5% cpu 2.338 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.06s user 0.08s system 5% cpu 2.348 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.06s user 0.08s system 5% cpu 2.348 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.06s user 0.08s system 5% cpu 2.364 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.06s user 0.08s system 5% cpu 2.348 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.56s user 0.03s system 99% cpu 6.638 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.51s user 0.05s system 99% cpu 6.557 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.55s user 0.08s system 99% cpu 6.629 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.51s user 0.03s system 99% cpu 6.543 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.56s user 0.03s system 99% cpu 6.592 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.50s user 0.02s system 99% cpu 6.528 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.58s user 0.04s system 99% cpu 6.631 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.52s user 0.05s system 99% cpu 6.579 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.50s user 0.04s system 99% cpu 6.543 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.52s user 0.08s system 99% cpu 6.603 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.53s user 0.06s system 99% cpu 6.598 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.59s user 0.02s system 99% cpu 6.616 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.50s user 0.02s system 99% cpu 6.529 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.49s user 0.02s system 99% cpu 6.518 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.52s user 0.01s system 99% cpu 6.531 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.54s user 0.01s system 99% cpu 6.548 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.51s user 0.02s system 99% cpu 6.522 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.47s user 0.06s system 99% cpu 6.532 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.53s user 0.01s system 99% cpu 6.540 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.51s user 0.04s system 99% cpu 6.550 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.49s user 0.01s system 99% cpu 6.500 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.44s user 0.04s system 99% cpu 6.489 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.50s user 0.03s system 99% cpu 6.537 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.56s user 0.05s system 99% cpu 6.617 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.48s user 0.07s system 99% cpu 6.553 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.48s user 0.08s system 99% cpu 6.564 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.47s user 0.02s system 99% cpu 6.489 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.51s user 0.01s system 99% cpu 6.522 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.51s user 0.01s system 99% cpu 6.524 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  6.53s user 0.02s system 99% cpu 6.550 total
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

in_string2 = """Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.01s system 43% cpu 0.099 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 94% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 94% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 94% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 94% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 95% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 94% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 94% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 94% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 94% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 94% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 95% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 94% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 94% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 94% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 95% cpu 0.036 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 94% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 94% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 95% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 94% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 94% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 94% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 94% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 94% cpu 0.038 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 94% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 94% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 94% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 94% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 95% cpu 0.037 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_sudoku_perm.pl:9:
Warning:    Singleton variables: [Rows]
swipl -q "${SWIPROG}" > timings.txt  0.03s user 0.00s system 95% cpu 0.037 total
"""

swipl = []
for line in in_string2.split("\n"):
    s = line.split(' ')
    if len(s) > 0 and s[0] == "swipl":
        swipl.append(s[12])

with open("sudokuperm.csv", "w") as csvfile:
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

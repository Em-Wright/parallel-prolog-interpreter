import csv

in_string = """./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.31s user 0.15s system 29% cpu 1.575 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.31s user 0.12s system 28% cpu 1.514 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.31s user 0.12s system 28% cpu 1.502 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.31s user 0.12s system 28% cpu 1.501 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.31s user 0.12s system 28% cpu 1.511 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.31s user 0.12s system 28% cpu 1.505 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.32s user 0.12s system 29% cpu 1.516 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.31s user 0.12s system 28% cpu 1.513 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.30s user 0.11s system 27% cpu 1.508 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.31s user 0.12s system 28% cpu 1.517 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.31s user 0.13s system 28% cpu 1.512 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.31s user 0.11s system 28% cpu 1.505 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.32s user 0.12s system 29% cpu 1.524 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.31s user 0.12s system 28% cpu 1.512 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.31s user 0.12s system 28% cpu 1.509 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.31s user 0.12s system 28% cpu 1.518 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.32s user 0.13s system 26% cpu 1.668 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.31s user 0.12s system 28% cpu 1.513 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.31s user 0.12s system 28% cpu 1.507 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.32s user 0.12s system 29% cpu 1.524 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.32s user 0.13s system 29% cpu 1.540 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.31s user 0.12s system 29% cpu 1.506 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.31s user 0.12s system 28% cpu 1.508 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.32s user 0.12s system 28% cpu 1.514 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.32s user 0.12s system 28% cpu 1.526 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.31s user 0.12s system 28% cpu 1.507 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.31s user 0.12s system 28% cpu 1.509 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.31s user 0.12s system 28% cpu 1.515 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.31s user 0.12s system 28% cpu 1.522 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.31s user 0.13s system 29% cpu 1.509 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.30s user 0.11s system 27% cpu 1.500 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.30s user 0.11s system 27% cpu 1.494 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.30s user 0.11s system 27% cpu 1.503 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.30s user 0.10s system 26% cpu 1.500 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.29s user 0.11s system 26% cpu 1.484 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.30s user 0.11s system 27% cpu 1.498 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.30s user 0.11s system 27% cpu 1.490 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.30s user 0.11s system 27% cpu 1.493 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.30s user 0.11s system 27% cpu 1.504 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.31s user 0.12s system 27% cpu 1.525 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.31s user 0.11s system 27% cpu 1.504 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.31s user 0.11s system 26% cpu 1.537 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.31s user 0.11s system 27% cpu 1.517 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.31s user 0.12s system 27% cpu 1.536 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.31s user 0.12s system 28% cpu 1.517 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.32s user 0.12s system 28% cpu 1.528 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.31s user 0.12s system 28% cpu 1.529 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.32s user 0.12s system 28% cpu 1.542 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.31s user 0.12s system 27% cpu 1.527 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.30s user 0.11s system 27% cpu 1.503 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.30s user 0.11s system 27% cpu 1.506 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.30s user 0.12s system 27% cpu 1.501 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.31s user 0.12s system 28% cpu 1.526 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.31s user 0.11s system 28% cpu 1.495 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.30s user 0.11s system 27% cpu 1.490 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.31s user 0.11s system 27% cpu 1.509 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.31s user 0.12s system 27% cpu 1.526 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.31s user 0.12s system 28% cpu 1.509 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.30s user 0.11s system 27% cpu 1.494 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.31s user 0.11s system 28% cpu 1.512 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.10s system 26% cpu 1.487 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.09s system 25% cpu 1.498 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.10s system 25% cpu 1.494 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.09s system 25% cpu 1.492 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.10s system 25% cpu 1.496 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.10s system 25% cpu 1.488 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.09s system 25% cpu 1.483 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.28s user 0.09s system 25% cpu 1.482 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.10s system 25% cpu 1.487 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.10s system 26% cpu 1.496 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.09s system 25% cpu 1.485 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.10s system 25% cpu 1.496 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.09s system 25% cpu 1.488 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.09s system 25% cpu 1.497 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.09s system 25% cpu 1.491 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.09s system 25% cpu 1.493 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.30s user 0.09s system 26% cpu 1.495 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.09s system 25% cpu 1.489 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.09s system 25% cpu 1.492 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.09s system 25% cpu 1.479 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.10s system 26% cpu 1.495 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.10s system 26% cpu 1.501 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.10s system 25% cpu 1.490 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.28s user 0.10s system 25% cpu 1.488 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.30s user 0.10s system 26% cpu 1.499 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.10s system 26% cpu 1.500 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.10s system 26% cpu 1.505 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.10s system 25% cpu 1.500 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.29s user 0.09s system 25% cpu 1.487 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.30s user 0.10s system 26% cpu 1.500 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.29s user 0.09s system 25% cpu 1.493 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.29s user 0.10s system 25% cpu 1.516 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.29s user 0.09s system 25% cpu 1.510 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.28s user 0.09s system 24% cpu 1.498 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.29s user 0.09s system 25% cpu 1.516 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.30s user 0.09s system 26% cpu 1.507 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.29s user 0.09s system 25% cpu 1.488 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.29s user 0.09s system 25% cpu 1.504 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.29s user 0.10s system 25% cpu 1.502 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.29s user 0.10s system 25% cpu 1.508 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.30s user 0.10s system 26% cpu 1.525 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.29s user 0.10s system 25% cpu 1.510 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.29s user 0.10s system 25% cpu 1.528 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.29s user 0.09s system 25% cpu 1.495 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.37s user 0.09s system 29% cpu 1.583 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.29s user 0.09s system 25% cpu 1.498 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.29s user 0.09s system 25% cpu 1.508 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.29s user 0.10s system 25% cpu 1.534 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.30s user 0.10s system 25% cpu 1.528 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.30s user 0.10s system 26% cpu 1.508 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.29s user 0.10s system 25% cpu 1.503 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.29s user 0.09s system 24% cpu 1.513 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.30s user 0.09s system 25% cpu 1.521 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.29s user 0.10s system 25% cpu 1.520 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.29s user 0.10s system 25% cpu 1.521 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.30s user 0.10s system 26% cpu 1.520 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.30s user 0.10s system 25% cpu 1.521 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.30s user 0.10s system 25% cpu 1.515 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.29s user 0.09s system 25% cpu 1.505 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.28s user 0.09s system 24% cpu 1.494 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.36s user 0.08s system 27% cpu 1.616 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.35s user 0.08s system 27% cpu 1.553 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.36s user 0.08s system 28% cpu 1.572 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.30s user 0.09s system 25% cpu 1.523 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.29s user 0.08s system 24% cpu 1.499 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.36s user 0.08s system 28% cpu 1.568 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.36s user 0.08s system 27% cpu 1.569 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.30s user 0.09s system 25% cpu 1.526 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.34s user 0.08s system 27% cpu 1.558 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.35s user 0.08s system 27% cpu 1.553 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.35s user 0.09s system 27% cpu 1.621 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.34s user 0.08s system 26% cpu 1.549 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.36s user 0.08s system 27% cpu 1.560 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.33s user 0.08s system 26% cpu 1.542 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.34s user 0.08s system 26% cpu 1.549 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.34s user 0.08s system 26% cpu 1.547 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.33s user 0.07s system 26% cpu 1.545 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.35s user 0.08s system 26% cpu 1.560 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.33s user 0.08s system 26% cpu 1.537 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.34s user 0.07s system 26% cpu 1.544 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.33s user 0.08s system 26% cpu 1.540 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.34s user 0.08s system 26% cpu 1.556 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.34s user 0.08s system 26% cpu 1.545 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.34s user 0.08s system 26% cpu 1.546 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.35s user 0.08s system 27% cpu 1.551 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.34s user 0.07s system 26% cpu 1.544 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.28s user 0.08s system 24% cpu 1.492 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.34s user 0.08s system 26% cpu 1.546 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.33s user 0.08s system 26% cpu 1.544 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.35s user 0.08s system 27% cpu 1.556 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.29s user 0.07s system 23% cpu 1.497 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.32s user 0.07s system 25% cpu 1.530 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.33s user 0.07s system 25% cpu 1.546 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.28s user 0.07s system 23% cpu 1.500 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.32s user 0.07s system 25% cpu 1.535 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.32s user 0.07s system 25% cpu 1.536 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.32s user 0.07s system 25% cpu 1.535 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.32s user 0.07s system 25% cpu 1.537 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.29s user 0.07s system 24% cpu 1.499 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.33s user 0.08s system 26% cpu 1.543 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.33s user 0.07s system 25% cpu 1.547 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.30s user 0.08s system 24% cpu 1.514 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.33s user 0.07s system 26% cpu 1.551 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.32s user 0.07s system 25% cpu 1.535 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.29s user 0.07s system 23% cpu 1.499 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.32s user 0.07s system 25% cpu 1.540 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.33s user 0.07s system 25% cpu 1.544 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.28s user 0.07s system 23% cpu 1.497 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.33s user 0.07s system 26% cpu 1.545 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.34s user 0.07s system 26% cpu 1.556 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.32s user 0.07s system 25% cpu 1.535 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.32s user 0.07s system 25% cpu 1.541 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.33s user 0.07s system 25% cpu 1.538 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.32s user 0.07s system 25% cpu 1.532 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.32s user 0.07s system 25% cpu 1.533 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.32s user 0.07s system 25% cpu 1.530 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.28s user 0.07s system 23% cpu 1.497 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.32s user 0.07s system 25% cpu 1.540 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.33s user 0.08s system 26% cpu 1.546 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.29s user 0.07s system 24% cpu 1.504 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.27s user 0.06s system 22% cpu 1.488 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.27s user 0.06s system 22% cpu 1.492 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.32s user 0.06s system 24% cpu 1.546 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.27s user 0.06s system 22% cpu 1.491 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.28s user 0.07s system 23% cpu 1.502 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.29s user 0.07s system 23% cpu 1.509 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.29s user 0.07s system 23% cpu 1.509 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.28s user 0.06s system 22% cpu 1.490 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.27s user 0.06s system 22% cpu 1.485 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.34s user 0.07s system 26% cpu 1.563 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.28s user 0.07s system 23% cpu 1.503 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.34s user 0.07s system 26% cpu 1.561 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.28s user 0.07s system 23% cpu 1.503 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.28s user 0.06s system 23% cpu 1.489 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.28s user 0.06s system 23% cpu 1.500 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.28s user 0.07s system 23% cpu 1.485 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.29s user 0.07s system 23% cpu 1.523 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.28s user 0.06s system 23% cpu 1.487 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.28s user 0.07s system 23% cpu 1.492 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.28s user 0.07s system 23% cpu 1.495 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.28s user 0.06s system 22% cpu 1.503 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.28s user 0.06s system 22% cpu 1.501 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.27s user 0.06s system 22% cpu 1.496 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.28s user 0.06s system 22% cpu 1.488 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.27s user 0.06s system 22% cpu 1.496 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.32s user 0.06s system 24% cpu 1.536 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.27s user 0.06s system 22% cpu 1.488 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.28s user 0.06s system 22% cpu 1.497 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.27s user 0.06s system 22% cpu 1.491 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.28s user 0.06s system 22% cpu 1.494 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.07s system 11% cpu 2.568 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.07s system 11% cpu 2.570 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.07s system 11% cpu 2.554 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.07s system 11% cpu 2.570 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.06s system 11% cpu 2.561 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.07s system 11% cpu 2.569 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.07s system 11% cpu 2.579 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.07s system 11% cpu 2.570 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.07s system 11% cpu 2.569 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.07s system 11% cpu 2.577 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.07s system 11% cpu 2.592 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.27s user 0.07s system 12% cpu 2.696 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.07s system 11% cpu 2.585 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.08s system 11% cpu 2.632 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.24s user 0.09s system 12% cpu 2.646 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.27s user 0.10s system 13% cpu 2.671 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.08s system 11% cpu 2.605 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.07s system 11% cpu 2.602 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.08s system 11% cpu 2.595 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.07s system 11% cpu 2.589 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.24s user 0.09s system 12% cpu 2.649 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.27s user 0.09s system 13% cpu 2.657 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.07s system 11% cpu 2.584 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.07s system 11% cpu 2.570 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.08s system 11% cpu 2.586 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.07s system 11% cpu 2.578 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.07s system 11% cpu 2.567 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.07s system 11% cpu 2.593 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.08s system 11% cpu 2.599 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.23s user 0.07s system 11% cpu 2.593 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.03s system 98% cpu 1.851 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.81s user 0.03s system 99% cpu 1.840 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.01s system 99% cpu 1.793 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.02s system 99% cpu 1.807 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.00s system 99% cpu 1.789 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.01s system 99% cpu 1.791 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.01s system 99% cpu 1.785 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.00s system 99% cpu 1.785 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.01s system 99% cpu 1.790 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.01s system 99% cpu 1.794 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.01s system 99% cpu 1.787 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.01s system 99% cpu 1.791 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.01s system 99% cpu 1.787 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.00s system 99% cpu 1.786 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.01s system 99% cpu 1.787 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.01s system 99% cpu 1.784 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.01s system 99% cpu 1.789 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.00s system 99% cpu 1.785 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.00s system 99% cpu 1.785 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.01s system 99% cpu 1.792 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.01s system 99% cpu 1.791 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.01s system 99% cpu 1.790 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.01s system 99% cpu 1.788 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.00s system 99% cpu 1.788 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.00s system 99% cpu 1.791 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.00s system 99% cpu 1.784 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.02s system 99% cpu 1.800 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.02s system 99% cpu 1.806 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.02s system 99% cpu 1.805 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  1.78s user 0.01s system 99% cpu 1.792 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.260 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.261 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.257 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.26s user 0.01s system 99% cpu 0.263 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 96% cpu 0.267 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.256 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.256 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.255 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.256 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.254 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.255 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.254 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.254 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.261 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.255 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.261 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.259 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.256 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.261 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.256 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.26s user 0.01s system 99% cpu 0.262 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.261 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.257 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.257 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.256 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.262 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.257 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.257 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.258 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.256 total
"""


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

# tr8 = []
# for line in in_string.split("\n")[300:330]:
#     s = line.split()
#     tr8.append(s[13])
#     print( s[13])
# tr7 = []
# for line in in_string.split("\n")[330:360]:
#     s = line.split()
#     tr7.append(s[13])
#     print( s[13])
# tr6 = []
# for line in in_string.split("\n")[360:390]:
#     s = line.split()
#     tr6.append(s[13])
#     print( s[13])
# tr5 = []
# for line in in_string.split("\n")[390:420]:
#     s = line.split()
#     tr5.append(s[13])
#     print( s[13])
# tr4 = []
# for line in in_string.split("\n")[420:450]:
#     s = line.split()
#     tr4.append(s[13])
#     print( s[13])
# tr3 = []
# for line in in_string.split("\n")[450:480]:
#     s = line.split()
#     tr3.append(s[13])
#     print( s[13])
# tr2 = []
# for line in in_string.split("\n")[480:510]:
#     s = line.split()
#     tr2.append(s[13])
#     print( s[13])
# tr1 = []
# for line in in_string.split("\n")[510:540]:
#     s = line.split()
#     tr1.append(s[13])
#     print( s[13])
# trstack = []
# for line in in_string.split("\n")[540:570]:
#     s = line.split()
#     trstack.append(s[12])
#     print( s[12])
# trseq = []
# for line in in_string.split("\n")[570:600]:
#     s = line.split()
#     trseq.append(s[12])
#     print( s[12])

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
    # writer.writerow(tr8)
    # writer.writerow(tr7)
    # writer.writerow(tr6)
    # writer.writerow(tr5)
    # writer.writerow(tr4)
    # writer.writerow(tr3)
    # writer.writerow(tr2)
    # writer.writerow(tr1)
    # writer.writerow(trstack)
    # writer.writerow(trseq)
    # writer.writerow(swipl)

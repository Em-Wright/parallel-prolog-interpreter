import csv

in_string = """./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  1.73s user 0.21s system 74% cpu 2.599 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  1.72s user 0.19s system 74% cpu 2.580 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  1.70s user 0.19s system 73% cpu 2.556 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  1.71s user 0.20s system 74% cpu 2.570 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  1.71s user 0.20s system 74% cpu 2.580 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  1.70s user 0.20s system 74% cpu 2.570 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  1.70s user 0.20s system 74% cpu 2.560 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  1.75s user 0.21s system 74% cpu 2.629 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  1.72s user 0.22s system 74% cpu 2.617 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  1.73s user 0.21s system 74% cpu 2.601 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  1.70s user 0.21s system 73% cpu 2.580 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  1.69s user 0.20s system 73% cpu 2.572 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  1.69s user 0.19s system 73% cpu 2.570 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  1.69s user 0.19s system 73% cpu 2.548 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  1.69s user 0.20s system 73% cpu 2.570 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  1.68s user 0.20s system 73% cpu 2.561 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  1.70s user 0.21s system 73% cpu 2.585 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  1.69s user 0.19s system 73% cpu 2.549 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  1.72s user 0.20s system 71% cpu 2.690 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  1.68s user 0.20s system 73% cpu 2.552 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  1.69s user 0.21s system 72% cpu 2.611 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  1.67s user 0.19s system 72% cpu 2.557 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  1.70s user 0.18s system 72% cpu 2.576 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  1.67s user 0.17s system 72% cpu 2.532 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  1.66s user 0.17s system 72% cpu 2.519 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  1.68s user 0.20s system 73% cpu 2.567 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  1.69s user 0.21s system 73% cpu 2.588 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  1.68s user 0.19s system 72% cpu 2.567 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  1.67s user 0.18s system 72% cpu 2.534 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  1.65s user 0.18s system 72% cpu 2.516 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  1.69s user 0.19s system 72% cpu 2.590 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  1.68s user 0.19s system 72% cpu 2.572 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  1.65s user 0.17s system 72% cpu 2.527 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  1.68s user 0.19s system 72% cpu 2.581 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  1.68s user 0.21s system 72% cpu 2.596 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  1.67s user 0.17s system 72% cpu 2.557 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  1.68s user 0.19s system 72% cpu 2.580 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  1.67s user 0.19s system 72% cpu 2.578 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  1.67s user 0.20s system 72% cpu 2.576 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  1.69s user 0.19s system 72% cpu 2.608 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  1.66s user 0.18s system 71% cpu 2.568 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  1.69s user 0.17s system 71% cpu 2.584 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  1.68s user 0.16s system 72% cpu 2.559 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  1.69s user 0.17s system 72% cpu 2.583 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  1.67s user 0.16s system 71% cpu 2.546 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  1.66s user 0.17s system 71% cpu 2.548 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  1.72s user 0.16s system 72% cpu 2.596 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  1.68s user 0.18s system 72% cpu 2.584 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  1.70s user 0.19s system 72% cpu 2.625 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  1.66s user 0.18s system 72% cpu 2.562 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  1.72s user 0.16s system 71% cpu 2.643 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  1.74s user 0.14s system 72% cpu 2.606 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  1.74s user 0.15s system 72% cpu 2.627 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  1.78s user 0.17s system 72% cpu 2.675 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  1.77s user 0.17s system 72% cpu 2.675 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  1.78s user 0.19s system 72% cpu 2.708 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  1.77s user 0.19s system 72% cpu 2.708 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  1.77s user 0.18s system 72% cpu 2.697 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  1.75s user 0.17s system 72% cpu 2.652 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  1.75s user 0.16s system 72% cpu 2.647 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  1.70s user 0.16s system 71% cpu 2.594 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  1.70s user 0.15s system 71% cpu 2.593 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  1.69s user 0.15s system 71% cpu 2.573 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  1.71s user 0.14s system 71% cpu 2.587 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  1.67s user 0.16s system 71% cpu 2.570 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  1.73s user 0.15s system 71% cpu 2.612 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  1.72s user 0.18s system 71% cpu 2.644 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  1.64s user 0.14s system 70% cpu 2.524 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  1.70s user 0.15s system 71% cpu 2.581 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  1.73s user 0.17s system 71% cpu 2.642 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  1.70s user 0.16s system 71% cpu 2.612 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  1.70s user 0.15s system 70% cpu 2.598 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  1.69s user 0.16s system 71% cpu 2.600 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  1.69s user 0.17s system 70% cpu 2.610 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  1.72s user 0.15s system 71% cpu 2.637 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  1.68s user 0.16s system 70% cpu 2.597 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  1.69s user 0.14s system 70% cpu 2.595 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  1.69s user 0.14s system 70% cpu 2.582 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  1.68s user 0.14s system 70% cpu 2.569 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  1.69s user 0.15s system 70% cpu 2.591 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.00s user 0.01s system 24% cpu 0.051 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.00s user 0.00s system 86% cpu 0.007 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.00s user 0.00s system 87% cpu 0.007 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.00s user 0.00s system 87% cpu 0.007 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.00s user 0.00s system 87% cpu 0.007 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.00s user 0.00s system 87% cpu 0.007 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.00s user 0.00s system 87% cpu 0.007 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.00s user 0.00s system 88% cpu 0.008 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.00s user 0.00s system 87% cpu 0.007 total
./bin/sequential.exe stack -file "${PROG}" > timings.txt  0.00s user 0.00s system 88% cpu 0.007 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.27s user 0.01s system 99% cpu 0.274 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.26s user 0.01s system 99% cpu 0.267 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.26s user 0.01s system 99% cpu 0.272 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.27s user 0.01s system 99% cpu 0.278 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.26s user 0.01s system 99% cpu 0.271 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.26s user 0.01s system 99% cpu 0.268 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.255 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.26s user 0.01s system 99% cpu 0.270 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.26s user 0.01s system 99% cpu 0.273 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  0.25s user 0.01s system 99% cpu 0.253 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  1.73s user 0.22s system 77% cpu 2.533 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  1.72s user 0.21s system 78% cpu 2.463 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  1.73s user 0.20s system 78% cpu 2.467 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  1.71s user 0.19s system 78% cpu 2.431 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  1.72s user 0.22s system 78% cpu 2.471 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  1.76s user 0.21s system 78% cpu 2.503 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  1.77s user 0.23s system 79% cpu 2.519 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  1.75s user 0.21s system 78% cpu 2.490 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  1.74s user 0.22s system 78% cpu 2.492 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  1.76s user 0.21s system 78% cpu 2.508 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  1.71s user 0.20s system 77% cpu 2.460 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  1.71s user 0.20s system 77% cpu 2.452 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  1.71s user 0.20s system 78% cpu 2.440 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  1.70s user 0.20s system 77% cpu 2.442 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  1.74s user 0.22s system 77% cpu 2.509 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  1.74s user 0.21s system 78% cpu 2.495 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  1.76s user 0.21s system 78% cpu 2.511 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  1.72s user 0.19s system 77% cpu 2.465 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  1.70s user 0.20s system 77% cpu 2.442 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  1.70s user 0.21s system 77% cpu 2.462 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  1.74s user 0.20s system 77% cpu 2.501 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  1.72s user 0.20s system 77% cpu 2.469 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  1.73s user 0.20s system 77% cpu 2.481 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  1.71s user 0.19s system 77% cpu 2.457 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  1.72s user 0.19s system 77% cpu 2.463 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  1.70s user 0.20s system 77% cpu 2.457 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  1.71s user 0.21s system 77% cpu 2.483 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  1.74s user 0.19s system 77% cpu 2.489 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  1.73s user 0.19s system 77% cpu 2.468 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  1.72s user 0.20s system 77% cpu 2.480 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  1.72s user 0.18s system 75% cpu 2.532 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  1.74s user 0.19s system 77% cpu 2.503 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  1.68s user 0.19s system 76% cpu 2.435 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  1.71s user 0.20s system 77% cpu 2.472 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  1.73s user 0.22s system 77% cpu 2.527 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  1.70s user 0.19s system 76% cpu 2.450 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  1.71s user 0.20s system 77% cpu 2.479 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  1.71s user 0.18s system 76% cpu 2.476 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  1.69s user 0.19s system 76% cpu 2.447 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  1.67s user 0.17s system 75% cpu 2.429 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  1.71s user 0.16s system 76% cpu 2.455 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  1.70s user 0.16s system 75% cpu 2.453 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  1.74s user 0.18s system 76% cpu 2.506 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  1.72s user 0.17s system 76% cpu 2.469 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  1.73s user 0.17s system 76% cpu 2.483 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  1.73s user 0.18s system 76% cpu 2.498 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  1.72s user 0.17s system 74% cpu 2.536 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  1.72s user 0.18s system 76% cpu 2.480 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  1.74s user 0.17s system 76% cpu 2.497 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  1.70s user 0.17s system 76% cpu 2.449 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  1.78s user 0.16s system 76% cpu 2.533 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  1.78s user 0.16s system 76% cpu 2.527 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  1.75s user 0.16s system 76% cpu 2.509 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  1.79s user 0.17s system 76% cpu 2.556 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  1.76s user 0.16s system 76% cpu 2.521 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  1.77s user 0.16s system 76% cpu 2.531 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  1.80s user 0.18s system 76% cpu 2.583 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  1.75s user 0.17s system 76% cpu 2.517 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  1.76s user 0.17s system 76% cpu 2.526 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  1.79s user 0.17s system 76% cpu 2.572 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  1.71s user 0.15s system 75% cpu 2.461 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  1.71s user 0.17s system 75% cpu 2.479 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  1.74s user 0.16s system 75% cpu 2.515 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  1.72s user 0.15s system 75% cpu 2.465 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  1.74s user 0.15s system 75% cpu 2.488 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  1.74s user 0.15s system 75% cpu 2.498 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  1.68s user 0.16s system 75% cpu 2.449 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  1.73s user 0.16s system 75% cpu 2.498 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  1.69s user 0.15s system 75% cpu 2.450 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  1.72s user 0.15s system 75% cpu 2.476 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  1.70s user 0.15s system 74% cpu 2.474 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  1.70s user 0.15s system 75% cpu 2.468 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  1.71s user 0.16s system 74% cpu 2.496 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  1.72s user 0.14s system 74% cpu 2.490 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  1.70s user 0.15s system 74% cpu 2.479 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  1.72s user 0.17s system 75% cpu 2.505 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  1.72s user 0.14s system 74% cpu 2.481 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  1.71s user 0.15s system 74% cpu 2.478 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  1.72s user 0.15s system 74% cpu 2.492 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  1.74s user 0.16s system 75% cpu 2.535 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.01s user 0.01s system 7% cpu 0.211 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.00s user 0.00s system 85% cpu 0.007 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.00s user 0.00s system 86% cpu 0.006 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.00s user 0.00s system 87% cpu 0.007 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.00s user 0.00s system 87% cpu 0.007 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.00s user 0.00s system 86% cpu 0.007 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.00s user 0.00s system 85% cpu 0.007 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.00s user 0.00s system 86% cpu 0.007 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.00s user 0.00s system 90% cpu 0.006 total
./bin/trail_sequential.exe trail-stack -file "${PROG}" > timings.txt  0.00s user 0.00s system 85% cpu 0.007 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.04s user 0.00s system 96% cpu 0.041 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.04s user 0.00s system 96% cpu 0.042 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.04s user 0.00s system 96% cpu 0.041 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.04s user 0.00s system 96% cpu 0.042 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.04s user 0.00s system 96% cpu 0.047 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.04s user 0.00s system 96% cpu 0.043 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.04s user 0.00s system 97% cpu 0.041 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.04s user 0.00s system 96% cpu 0.042 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.04s user 0.00s system 96% cpu 0.044 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.04s user 0.00s system 96% cpu 0.042 total """

# print("8 workers")
# par8 = []
# for line in in_string.split("\n")[0:30]:
#     s = line.split()
#     if s[4] != "8":
#         print (s[4])
#     par8.append(s[13])

# print("\n\n7 workers")
# par7 = []
# for line in in_string.split("\n")[30:60]:
#     s = line.split()
#     if s[4] != "7":
#         print (s[4])
#     par7.append(s[13])

# print("\n\n6 workers")
# par6 = []
# for line in in_string.split("\n")[60:90]:
#     s = line.split()
#     if s[4] != "6":
#         print( s[4])
#     par6.append(s[13])

# print("\n\n5 workers")
# par5 = []
# for line in in_string.split("\n")[90:120]:
#     s = line.split()
#     if s[4] != "5":
#         print(s[4])
#     par5.append(s[13])

# print("4 workers")
# par4 = []
# for line in in_string.split("\n")[120:150]:
#     s = line.split()
#     if s[4] != "4":
#         print (s[4])
#     par4.append(s[13])

# print("\n\n3 workers")
# par3 = []
# for line in in_string.split("\n")[150:180]:
#     s = line.split()
#     if s[4] != "3":
#         print (s[4])
#     par3.append(s[13])

# print("\n\n2 workers")
# par2 = []
# for line in in_string.split("\n")[180:210]:
#     s = line.split()
#     if s[4] != "2":
#         print( s[4])
#     par2.append(s[13])

# print("\n\n1 workers")
# par1 = []
# for line in in_string.split("\n")[210:240]:
#     s = line.split()
#     if s[4] != "1":
#         print(s[4])
#     par1.append(s[13])

# print("\n\nstack seq")
# stackseq = []
# for line in in_string.split("\n")[240:270]:
#     s = line.split()
#     stackseq.append(s[12])

# print("\n\nsequential")
# seq = []
# for line in in_string.split("\n")[270:300]:
#     s = line.split()
#     seq.append(s[12])
#     print( s[12])

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

print("8 workers")
par8 = []
for line in in_string.split("\n")[0:10]:
    s = line.split()
    if s[4] != "8":
        print (s[4])
    par8.append(s[13])

print("\n\n7 workers")
par7 = []
for line in in_string.split("\n")[10:20]:
    s = line.split()
    if s[4] != "7":
        print (s[4])
    par7.append(s[13])

print("\n\n6 workers")
par6 = []
for line in in_string.split("\n")[20:30]:
    s = line.split()
    if s[4] != "6":
        print( s[4])
    par6.append(s[13])

print("\n\n5 workers")
par5 = []
for line in in_string.split("\n")[30:40]:
    s = line.split()
    if s[4] != "5":
        print(s[4])
    par5.append(s[13])

print("4 workers")
par4 = []
for line in in_string.split("\n")[40:50]:
    s = line.split()
    if s[4] != "4":
        print (s[4])
    par4.append(s[13])

print("\n\n3 workers")
par3 = []
for line in in_string.split("\n")[50:60]:
    s = line.split()
    if s[4] != "3":
        print (s[4])
    par3.append(s[13])

print("\n\n2 workers")
par2 = []
for line in in_string.split("\n")[60:70]:
    s = line.split()
    if s[4] != "2":
        print( s[4])
    par2.append(s[13])

print("\n\n1 workers")
par1 = []
for line in in_string.split("\n")[70:80]:
    s = line.split()
    if s[4] != "1":
        print(s[4])
    par1.append(s[13])

print("\n\nstack seq")
stackseq = []
for line in in_string.split("\n")[80:90]:
    s = line.split()
    stackseq.append(s[12])

print("\n\nsequential")
seq = []
for line in in_string.split("\n")[90:100]:
    s = line.split()
    seq.append(s[12])
    print( s[12])

tr8 = []
for line in in_string.split("\n")[100:110]:
    s = line.split()
    tr8.append(s[13])
    print( s[13])
tr7 = []
for line in in_string.split("\n")[110:120]:
    s = line.split()
    tr7.append(s[13])
    print( s[13])
tr6 = []
for line in in_string.split("\n")[120:130]:
    s = line.split()
    tr6.append(s[13])
    print( s[13])
tr5 = []
for line in in_string.split("\n")[130:140]:
    s = line.split()
    tr5.append(s[13])
    print( s[13])
tr4 = []
for line in in_string.split("\n")[140:150]:
    s = line.split()
    tr4.append(s[13])
    print( s[13])
tr3 = []
for line in in_string.split("\n")[150:160]:
    s = line.split()
    tr3.append(s[13])
    print( s[13])
tr2 = []
for line in in_string.split("\n")[160:170]:
    s = line.split()
    tr2.append(s[13])
    print( s[13])
tr1 = []
for line in in_string.split("\n")[170:180]:
    s = line.split()
    tr1.append(s[13])
    print( s[13])
trstack = []
for line in in_string.split("\n")[180:190]:
    s = line.split()
    trstack.append(s[12])
    print( s[12])
trseq = []
for line in in_string.split("\n")[190:200]:
    s = line.split()
    trseq.append(s[12])
    print( s[12])




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

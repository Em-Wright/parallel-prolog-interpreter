import csv

in_string = """./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 18% cpu 0.989 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 18% cpu 0.989 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 17% cpu 0.995 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 18% cpu 0.993 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 18% cpu 0.986 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 18% cpu 0.992 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 17% cpu 1.004 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 18% cpu 1.000 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 18% cpu 1.001 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 17% cpu 0.998 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 17% cpu 1.000 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 18% cpu 0.998 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 17% cpu 1.000 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 17% cpu 0.997 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.09s user 0.10s system 18% cpu 1.005 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 17% cpu 0.988 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.09s user 0.10s system 18% cpu 1.015 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 17% cpu 0.991 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 18% cpu 1.016 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 17% cpu 0.996 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.09s user 0.10s system 18% cpu 1.013 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.09s user 0.10s system 18% cpu 1.009 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 17% cpu 1.004 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.09s user 0.10s system 18% cpu 1.002 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 17% cpu 1.001 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 18% cpu 1.004 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.09s user 0.11s system 18% cpu 1.015 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.09s user 0.11s system 19% cpu 1.025 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.09s user 0.11s system 18% cpu 1.020 total
./bin/parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 17% cpu 1.019 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.09s system 16% cpu 1.008 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.09s system 16% cpu 1.002 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.09s system 16% cpu 0.985 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.09s system 16% cpu 0.985 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.08s system 16% cpu 0.986 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.09s system 16% cpu 1.005 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.10s system 17% cpu 1.021 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.10s system 17% cpu 1.006 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.09s system 16% cpu 1.014 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.09s system 17% cpu 1.003 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.09s system 16% cpu 0.997 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.09s system 16% cpu 0.992 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.09s system 16% cpu 0.992 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.09s system 16% cpu 0.987 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.09s system 16% cpu 0.997 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.08s system 16% cpu 0.988 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.08s system 16% cpu 0.991 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 15% cpu 0.996 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.09s system 16% cpu 0.998 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.09s system 16% cpu 0.999 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.09s system 16% cpu 1.005 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.09s system 16% cpu 1.006 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.09s system 16% cpu 0.993 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.09s system 16% cpu 0.998 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.09s system 16% cpu 0.999 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.09s system 16% cpu 0.992 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.08s user 0.09s system 16% cpu 0.994 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 15% cpu 0.989 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 15% cpu 0.995 total
./bin/parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 15% cpu 0.996 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 14% cpu 1.005 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.07s system 14% cpu 0.997 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.07s system 14% cpu 0.981 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 14% cpu 0.987 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 15% cpu 0.994 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 15% cpu 1.005 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.09s system 15% cpu 1.006 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 15% cpu 0.991 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 15% cpu 0.990 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 14% cpu 0.995 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 14% cpu 1.001 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 14% cpu 1.002 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 14% cpu 0.993 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.08s user 0.09s system 16% cpu 1.010 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 15% cpu 1.012 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 15% cpu 1.009 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 15% cpu 1.002 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 15% cpu 1.000 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 15% cpu 0.988 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 14% cpu 0.982 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 14% cpu 0.986 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 15% cpu 0.989 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 15% cpu 0.988 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 15% cpu 0.996 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 15% cpu 0.996 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 15% cpu 1.014 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 15% cpu 0.987 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 15% cpu 0.986 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 15% cpu 1.005 total
./bin/parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 15% cpu 1.006 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.07s user 0.07s system 13% cpu 0.993 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.07s user 0.07s system 13% cpu 1.021 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.07s user 0.07s system 13% cpu 0.987 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.07s system 13% cpu 0.981 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.07s user 0.07s system 13% cpu 0.993 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.07s user 0.07s system 13% cpu 0.998 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.07s system 13% cpu 1.006 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.07s user 0.07s system 13% cpu 0.983 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.07s user 0.07s system 13% cpu 0.989 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.07s user 0.07s system 13% cpu 0.993 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.07s user 0.07s system 14% cpu 0.994 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.07s system 13% cpu 0.985 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.07s system 13% cpu 0.993 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.07s user 0.07s system 13% cpu 0.996 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.07s system 13% cpu 0.991 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.07s system 13% cpu 0.989 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.07s system 13% cpu 0.989 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.07s system 13% cpu 0.992 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.07s system 13% cpu 0.983 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 13% cpu 0.980 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.07s system 13% cpu 0.982 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.07s system 13% cpu 0.977 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.07s user 0.07s system 13% cpu 0.983 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.07s system 13% cpu 0.987 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.07s system 13% cpu 0.982 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 13% cpu 0.985 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.07s user 0.07s system 13% cpu 0.995 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.07s system 13% cpu 0.980 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.07s user 0.07s system 13% cpu 0.997 total
./bin/parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.07s user 0.07s system 13% cpu 0.999 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 12% cpu 0.996 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 12% cpu 0.989 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.07s system 12% cpu 0.997 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 12% cpu 0.993 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 12% cpu 0.996 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 12% cpu 0.991 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 12% cpu 0.988 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 12% cpu 1.006 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 12% cpu 1.001 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 12% cpu 0.994 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 12% cpu 1.001 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 12% cpu 1.002 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 12% cpu 0.996 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.07s system 12% cpu 0.985 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 12% cpu 0.984 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 12% cpu 0.995 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 12% cpu 0.993 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 12% cpu 1.004 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.07s system 12% cpu 1.011 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 12% cpu 1.001 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 12% cpu 0.997 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 12% cpu 1.004 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 12% cpu 0.999 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 11% cpu 0.980 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 11% cpu 0.984 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 11% cpu 0.974 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 12% cpu 0.983 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 12% cpu 0.989 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 11% cpu 0.978 total
./bin/parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 12% cpu 0.992 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 10% cpu 0.981 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.06s user 0.06s system 11% cpu 0.995 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.06s user 0.06s system 11% cpu 1.011 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 10% cpu 1.001 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 10% cpu 0.991 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 10% cpu 0.976 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 10% cpu 0.979 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 10% cpu 0.977 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 10% cpu 0.993 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 10% cpu 0.982 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 10% cpu 0.993 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.06s system 11% cpu 0.995 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 10% cpu 0.979 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 10% cpu 0.988 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 10% cpu 1.000 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 10% cpu 0.992 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.06s system 11% cpu 0.998 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.06s system 10% cpu 0.999 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.06s system 11% cpu 0.996 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.06s system 10% cpu 1.008 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 10% cpu 0.986 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 10% cpu 0.987 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 10% cpu 0.986 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 10% cpu 0.986 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 10% cpu 0.988 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 10% cpu 0.996 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.06s system 11% cpu 0.999 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.06s user 0.06s system 11% cpu 1.010 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.06s system 10% cpu 1.007 total
./bin/parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.06s system 11% cpu 0.997 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.05s system 9% cpu 0.993 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.05s system 9% cpu 0.992 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.04s system 9% cpu 0.988 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.05s system 9% cpu 0.993 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.05s system 9% cpu 1.003 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.05s system 9% cpu 0.999 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.05s system 9% cpu 1.002 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.05s system 9% cpu 1.013 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.05s system 9% cpu 1.006 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.05s system 9% cpu 0.996 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.05s system 9% cpu 0.998 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.05s system 9% cpu 1.002 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.05s system 9% cpu 0.987 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.05s system 10% cpu 1.011 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.05s system 9% cpu 0.993 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.05s system 9% cpu 0.989 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.05s system 9% cpu 0.997 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.05s system 9% cpu 0.987 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.04s system 9% cpu 0.988 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.05s system 9% cpu 1.002 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.05s system 9% cpu 0.992 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.05s system 9% cpu 0.996 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.04s system 9% cpu 0.988 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.04s system 9% cpu 0.979 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.04s system 9% cpu 0.981 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.04s system 9% cpu 0.973 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.04s system 8% cpu 0.975 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.04s system 9% cpu 0.984 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.05s system 9% cpu 0.982 total
./bin/parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.05s user 0.05s system 9% cpu 0.998 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.995 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.981 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.985 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.981 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.971 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.984 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.980 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.986 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.989 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.987 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.997 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.991 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.986 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.997 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.991 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.987 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.974 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.977 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.978 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.978 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.973 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.980 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.985 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.978 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.972 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.997 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.993 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.994 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.997 total
./bin/parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 6% cpu 0.999 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.79s user 0.04s system 97% cpu 1.872 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.76s user 0.04s system 99% cpu 1.803 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.79s user 0.03s system 99% cpu 1.820 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.77s user 0.02s system 99% cpu 1.800 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.77s user 0.02s system 99% cpu 1.791 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.76s user 0.02s system 99% cpu 1.782 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.79s user 0.02s system 99% cpu 1.816 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.74s user 0.03s system 99% cpu 1.772 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.78s user 0.03s system 99% cpu 1.816 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.76s user 0.02s system 99% cpu 1.781 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.75s user 0.02s system 99% cpu 1.772 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.75s user 0.02s system 99% cpu 1.773 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.76s user 0.02s system 99% cpu 1.788 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.76s user 0.02s system 99% cpu 1.781 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.77s user 0.02s system 99% cpu 1.792 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.77s user 0.03s system 99% cpu 1.810 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.83s user 0.03s system 99% cpu 1.868 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.76s user 0.02s system 99% cpu 1.790 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.76s user 0.02s system 99% cpu 1.791 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.77s user 0.02s system 99% cpu 1.801 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.79s user 0.03s system 99% cpu 1.824 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.77s user 0.03s system 99% cpu 1.800 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.77s user 0.03s system 99% cpu 1.800 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.76s user 0.02s system 99% cpu 1.780 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.79s user 0.02s system 99% cpu 1.818 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.81s user 0.03s system 99% cpu 1.846 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.75s user 0.04s system 99% cpu 1.790 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.75s user 0.03s system 99% cpu 1.783 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.75s user 0.02s system 99% cpu 1.774 total
./bin/sequential.exe sequential -file "${PROG}" > timings.txt  1.81s user 0.04s system 99% cpu 1.849 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.11s system 25% cpu 0.733 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 25% cpu 0.690 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 25% cpu 0.676 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 24% cpu 0.670 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 24% cpu 0.680 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 25% cpu 0.673 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 24% cpu 0.684 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.07s user 0.09s system 24% cpu 0.665 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 25% cpu 0.682 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 24% cpu 0.680 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 24% cpu 0.680 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 24% cpu 0.675 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 24% cpu 0.680 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 24% cpu 0.678 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 25% cpu 0.670 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.07s user 0.09s system 24% cpu 0.677 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 24% cpu 0.679 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.07s user 0.09s system 24% cpu 0.671 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 24% cpu 0.675 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 24% cpu 0.672 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 25% cpu 0.669 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 24% cpu 0.672 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 24% cpu 0.665 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 24% cpu 0.682 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 25% cpu 0.664 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 25% cpu 0.675 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 26% cpu 0.669 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 25% cpu 0.687 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.09s system 24% cpu 0.685 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 8 > timings.txt  0.08s user 0.10s system 25% cpu 0.678 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 22% cpu 0.681 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 23% cpu 0.664 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 23% cpu 0.663 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 21% cpu 0.668 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 21% cpu 0.663 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 21% cpu 0.674 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.07s system 20% cpu 0.669 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 23% cpu 0.671 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 22% cpu 0.677 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 21% cpu 0.665 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 22% cpu 0.698 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 22% cpu 0.678 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 21% cpu 0.687 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 22% cpu 0.665 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 22% cpu 0.666 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 22% cpu 0.667 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 22% cpu 0.675 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.09s system 23% cpu 0.668 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.09s system 23% cpu 0.687 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 22% cpu 0.677 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.09s system 23% cpu 0.671 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 22% cpu 0.669 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 22% cpu 0.661 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.09s system 23% cpu 0.662 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 22% cpu 0.675 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 22% cpu 0.661 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 22% cpu 0.664 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 22% cpu 0.669 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 22% cpu 0.663 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 7 > timings.txt  0.07s user 0.08s system 22% cpu 0.667 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.07s system 20% cpu 0.671 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.07s system 19% cpu 0.659 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.07s system 20% cpu 0.662 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.07s system 20% cpu 0.670 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.07s system 20% cpu 0.662 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.07s system 20% cpu 0.662 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.07s system 20% cpu 0.657 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.07s system 20% cpu 0.663 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.07s system 20% cpu 0.658 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.07s system 19% cpu 0.657 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.07s system 20% cpu 0.680 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.07s system 20% cpu 0.668 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 21% cpu 0.684 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.07s system 20% cpu 0.671 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 21% cpu 0.669 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.07s system 20% cpu 0.696 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 21% cpu 0.679 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.08s system 21% cpu 0.674 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.07s system 20% cpu 0.668 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.07s system 20% cpu 0.658 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.08s system 21% cpu 0.672 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.08s system 21% cpu 0.679 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.07s system 20% cpu 0.670 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.07s system 20% cpu 0.663 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.07s system 19% cpu 0.688 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.07s system 20% cpu 0.664 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.07s system 20% cpu 0.661 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.07s user 0.07s system 20% cpu 0.689 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.07s system 19% cpu 0.674 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 6 > timings.txt  0.06s user 0.07s system 20% cpu 0.676 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 17% cpu 0.666 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 18% cpu 0.678 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 18% cpu 0.661 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.07s system 18% cpu 0.676 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 18% cpu 0.668 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.07s system 18% cpu 0.675 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.07s system 18% cpu 0.673 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 18% cpu 0.663 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 18% cpu 0.664 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 18% cpu 0.663 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 18% cpu 0.661 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 18% cpu 0.660 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 17% cpu 0.660 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.07s system 18% cpu 0.663 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 18% cpu 0.671 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.07s system 18% cpu 0.666 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.07s system 19% cpu 0.669 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 17% cpu 0.670 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 18% cpu 0.672 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 17% cpu 0.672 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 17% cpu 0.662 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 17% cpu 0.660 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 17% cpu 0.667 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 17% cpu 0.670 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 18% cpu 0.658 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 17% cpu 0.712 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 17% cpu 0.694 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 16% cpu 0.720 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 18% cpu 0.677 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 5 > timings.txt  0.06s user 0.06s system 17% cpu 0.668 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.05s system 15% cpu 0.660 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.05s system 15% cpu 0.660 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.05s system 15% cpu 0.659 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.05s system 15% cpu 0.661 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.05s system 16% cpu 0.664 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.05s system 15% cpu 0.688 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.05s system 15% cpu 0.654 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.05s system 16% cpu 0.652 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.06s system 16% cpu 0.663 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.06s system 16% cpu 0.678 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.06s system 15% cpu 0.674 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.06s system 16% cpu 0.669 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.05s system 16% cpu 0.665 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 16% cpu 0.678 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.06s system 16% cpu 0.668 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.05s system 16% cpu 0.667 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.05s system 15% cpu 0.657 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.06s system 16% cpu 0.657 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.05s system 15% cpu 0.659 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.05s system 15% cpu 0.653 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.05s system 16% cpu 0.658 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.06s system 16% cpu 0.680 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.06s system 16% cpu 0.677 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.06s system 16% cpu 0.681 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.06s system 16% cpu 0.668 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.06s system 16% cpu 0.683 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.06s user 0.06s system 16% cpu 0.679 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.06s system 16% cpu 0.683 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.05s system 16% cpu 0.666 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 4 > timings.txt  0.05s user 0.05s system 15% cpu 0.661 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.04s user 0.05s system 13% cpu 0.660 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 14% cpu 0.666 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 13% cpu 0.673 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 14% cpu 0.668 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 13% cpu 0.665 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 14% cpu 0.676 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 14% cpu 0.671 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 13% cpu 0.651 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.04s user 0.05s system 13% cpu 0.658 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 13% cpu 0.659 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 14% cpu 0.657 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 14% cpu 0.667 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.04s user 0.05s system 13% cpu 0.656 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.04s user 0.04s system 13% cpu 0.664 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 13% cpu 0.658 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 14% cpu 0.662 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 13% cpu 0.663 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 14% cpu 0.657 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 14% cpu 0.666 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 14% cpu 0.669 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.04s user 0.04s system 13% cpu 0.658 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.04s user 0.05s system 13% cpu 0.658 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 13% cpu 0.658 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.04s user 0.04s system 13% cpu 0.656 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.04s user 0.04s system 13% cpu 0.651 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.04s user 0.04s system 13% cpu 0.655 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 13% cpu 0.664 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.04s system 13% cpu 0.654 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.04s user 0.04s system 13% cpu 0.657 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 3 > timings.txt  0.05s user 0.05s system 13% cpu 0.656 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 12% cpu 0.647 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 12% cpu 0.656 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 12% cpu 0.658 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 12% cpu 0.653 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 11% cpu 0.650 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 11% cpu 0.664 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 11% cpu 0.648 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 11% cpu 0.675 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 12% cpu 0.660 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 12% cpu 0.687 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 11% cpu 0.673 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 12% cpu 0.655 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 11% cpu 0.684 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 12% cpu 0.647 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 11% cpu 0.673 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 12% cpu 0.663 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 12% cpu 0.656 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 12% cpu 0.660 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 12% cpu 0.661 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 12% cpu 0.647 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 12% cpu 0.655 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 11% cpu 0.654 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 11% cpu 0.662 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 11% cpu 0.661 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 11% cpu 0.649 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 12% cpu 0.651 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 12% cpu 0.658 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 12% cpu 0.655 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 11% cpu 0.653 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 2 > timings.txt  0.04s user 0.04s system 12% cpu 0.654 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.656 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.647 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.645 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.651 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.03s system 7% cpu 0.652 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.658 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.641 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.652 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.643 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.638 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.649 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.647 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.640 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.649 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.02s system 7% cpu 0.647 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 8% cpu 0.657 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.03s system 7% cpu 0.652 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.649 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 7% cpu 0.658 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.03s system 7% cpu 0.653 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.645 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.03s user 0.02s system 7% cpu 0.674 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.640 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.649 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.651 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.643 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.641 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.03s system 7% cpu 0.645 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.652 total
./bin/trail_parallel.exe -file "${PROG}" -num-workers 1 > timings.txt  0.02s user 0.02s system 7% cpu 0.650 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 42% cpu 0.427 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.175 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 98% cpu 0.181 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.177 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.177 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.176 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.175 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.175 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.176 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.174 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.178 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 98% cpu 0.175 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.178 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 98% cpu 0.177 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.174 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.176 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.175 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.181 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.175 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 98% cpu 0.179 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.175 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.176 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.182 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.176 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.176 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 98% cpu 0.178 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.177 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.177 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.176 total
./bin/trail_sequential.exe trail -file "${PROG}" > timings.txt  0.17s user 0.01s system 99% cpu 0.177 total"""


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

print("\n\nsequential")
seq = []
for line in in_string.split("\n")[240:270]:
# for line in in_string.split("\n")[0:30]:
    s = line.split()
    seq.append(s[12])
    print( s[12])

tr8 = []
for line in in_string.split("\n")[270:300]:
    s = line.split()
    tr8.append(s[13])
    print( s[13])
tr7 = []
for line in in_string.split("\n")[300:330]:
    s = line.split()
    tr7.append(s[13])
    print( s[13])
tr6 = []
for line in in_string.split("\n")[330:360]:
    s = line.split()
    tr6.append(s[13])
    print( s[13])
tr5 = []
for line in in_string.split("\n")[360:390]:
    s = line.split()
    tr5.append(s[13])
    print( s[13])
tr4 = []
for line in in_string.split("\n")[390:420]:
    s = line.split()
    tr4.append(s[13])
    print( s[13])
tr3 = []
for line in in_string.split("\n")[420:450]:
    s = line.split()
    tr3.append(s[13])
    print( s[13])
tr2 = []
for line in in_string.split("\n")[450:480]:
    s = line.split()
    tr2.append(s[13])
    print( s[13])
tr1 = []
for line in in_string.split("\n")[480:510]:
    s = line.split()
    tr1.append(s[13])
    print( s[13])
trseq = []
for line in in_string.split("\n")[510:540]:
# for line in in_string.split("\n")[30:60]:
    s = line.split()
    trseq.append(s[12])
    print( s[12])

in_string2 = """Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.01s system 29% cpu 0.087 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.020 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 88% cpu 0.021 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.021 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.021 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.01s system 86% cpu 0.023 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.020 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.020 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.020 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.020 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.020 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.020 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.020 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.020 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.020 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.020 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.020 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.021 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.020 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.020 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 86% cpu 0.021 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.020 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.021 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.021 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.020 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.020 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 78% cpu 0.023 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.020 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 89% cpu 0.020 total
Warning: /Users/em/Library/CloudStorage/OneDrive-Personal/Documents/Uni/II/Dissertation/parallel-prolog-interpreter/prolog_programs/swi_fib.pl:6:
Warning:    Singleton variables: [X]
swipl -q "${SWIPROG}" > timings.txt  0.01s user 0.00s system 90% cpu 0.020 total"""

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
    writer.writerow(seq)
    writer.writerow(tr8)
    writer.writerow(tr7)
    writer.writerow(tr6)
    writer.writerow(tr5)
    writer.writerow(tr4)
    writer.writerow(tr3)
    writer.writerow(tr2)
    writer.writerow(tr1)
    writer.writerow(trseq)
    writer.writerow(swipl)

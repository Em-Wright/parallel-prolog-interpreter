add(0, M, M).
add(N, M, L) :- N > 0, N2 is N - 1, add(N2, M, L2), L is L2 + 1.
add2(0, M, M).
add2(N, M, L) :- N > 0, N2 is N - 1, add2(N2, M, L2), L is L2 + 1.
add3(0, M, M).
add3(N, M, L) :- N > 0, N2 is N - 1, add3(N2, M, L2), L is L2 + 1.
add4(0, M, M).
add4(N, M, L) :- N > 0, N2 is N - 1, add4(N2, M, L2), L is L2 + 1.
contrived(A, B, C) :- add(A,B,C).
contrived(A, B, C) :- add2(A, B, C).
contrived(A, B, C) :- add3(A, B, C).
contrived(A, B, C) :- add4(A, B, C).
?- contrived(300,400, X).

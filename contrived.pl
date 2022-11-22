add(0, M, M).
add(N, M, L) :- N > 0, N2 is N - 1, add(N2, M, L2), L is L2 + 1.
add2(0, M, M).
add2(N, M, L) :- N > 0, N2 is N - 1, add2(N2, M, L2), L is L2 + 1.
contrived(A, B, C) :- add(A,B,C).
contrived(A, B, C) :- add2(A, B, C).
?- contrived(300,500, X).

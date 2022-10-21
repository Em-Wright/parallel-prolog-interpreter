len([], 0).
len([H|T], N) :- len(T, M), N is M + 1.
ins(Lower, Upper, []).
ins(Lower, Upper, [H | T]) :- H > Lower, H < Upper, ins(Lower, Upper, T).
abs(0, 0).
abs(N, N) :- N > 0.
abs(N, M) :- N < 0, M is N * -1.
n_queens(N, Qs) :- len(Qs, N), M is N + 1, ins(0, M, Qs), safe_queens(Qs).
safe_queens([]).
safe_queens([Q|Qs]) :- safe_queens(Qs, Q, 1), safe_queens(Qs).
safe_queens([], Y, X).
safe_queens([Q|Qs], Q0, D0) :- Q0 != Q, Diff is Q0 - Q, abs(Diff, AbsDiff), AbsDiff != D0, D1 is D0 + 1, safe_queens(Qs, Q0, D1).

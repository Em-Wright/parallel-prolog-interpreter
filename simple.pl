is_zero(0).
?- is_zero(X).
addone(N, M) :- M is N + 1.
?- addone(3, M).
cat(lucy).
cat(tom).
dog(jack).
animal(X) :- cat(X).
animal(X) :- dog(X).
?- animal(X).
?- nonsense(Y).
?- nonsense(nonsense).
?- true.

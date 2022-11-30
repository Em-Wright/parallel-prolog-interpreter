is_zero(0).
?- is_zero(X).
cat(lucy).
cat(tom).
dog(jack).
animal(X) :- cat(X).
animal(X) :- dog(X).
?- animal(X).
?- nonsense(Y).
?- nonsense(nonsense).
?- true.

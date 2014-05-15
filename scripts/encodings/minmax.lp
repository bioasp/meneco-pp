distance(V) :- xreaction(R,N), distance(R,V).
younger(V1) :- distance(V1), distance(V2), V2>V1.
maxdistance(V) :- distance(V), not younger(V).

#minimize [ not false= 0, maxdistance(V)=V].

#const maxdist = -1.
:- maxdistance(V), V > maxdist, maxdist >= 0.

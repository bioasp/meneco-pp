#minimize [ not false= 0, xreaction(R,N)  : ireaction(R,N) ].

#const maxcard = -1.
:- maxcard+1 [xreaction(R,N)  : ireaction(R,N)], maxcard >= 0.

#minimize [ not false= 0, xreaction(R,N)  : distance(R,D)=D ].

#const maxsum = -1.
:- maxsum + 1 [ xreaction(R,N) : distance(R,D)=D ], maxsum >= 0.

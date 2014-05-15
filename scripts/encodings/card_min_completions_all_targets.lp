
% what is producible by the original network
dscope(M) :- seed(M).

dscope(M) :- product(M,R,N), reaction(R,N), draft(N),
           dscope(M2) : reactant(M2,R,N).

dscope(M) :- reactant(M,R,N), reaction(R,N), draft(N), reversible(R),
           dscope(M2) : product(M2,R,N).

% what is producible with all reactions
pscope(M) :- seed(M).

pscope(M) :- product(M,R,N), reaction(R,N),
           pscope(M2) : reactant(M2,R,N).

pscope(M) :- reactant(M,R,N), reaction(R,N), reversible(R),
           pscope(M2) : product(M2,R,N).

% repair
% choose interesting reactions to extend the network.
% dont extend with already existing reactions.
{ xreaction(R,N) : ireaction(R,N) }.

% what is producible with the extensions
xscope(M) :- seed(M).

xscope(M) :- product(M,R,N), reaction(R,N), draft(N),
           xscope(M2) : reactant(M2,R,N).

xscope(M) :- reactant(M,R,N), reaction(R,N), draft(N), reversible(R),
           xscope(M2) : product(M2,R,N).

xscope(M) :- product(M,R,N), xreaction(R,N),
           xscope(M2) : reactant(M2,R,N).

xscope(M) :- reactant(M,R,N), xreaction(R,N), reversible(R),
           xscope(M2) : product(M2,R,N).               
               

% operable reactions
opreaction(R,N) :- xscope(M) : reactant(M,R,N), reaction(R,N).
opreaction(R,N) :- xscope(M) : product(M,R,N), reaction(R,N),reversible(R).

% no xreaction if not all reactants in xscope
:- xreaction(R,N), not opreaction(R,N).

% prohibit xreactions that produce nothing used by an operable reaction
used(M) :- opreaction(R,N), reactant(M,R,N), xreaction(R,N).
used(M) :- opreaction(R,N), reactant(M,R,N), reaction(R,N), draft(N).
used(M) :- opreaction(R,N), reversible(R), product(M,R,N), xreaction(R,N).
used(M) :- opreaction(R,N), reversible(R), product(M,R,N), reaction(R,N), draft(N).
used(M) :- target(M).

:- xreaction(R,N), not reversible(R), not used(M) : product(M,R,N).


%reach all potentially reachable targets
:- target(M), pscope(M), not xscope(M).

#hide.
#show xreaction/2.

% translate from old meneco style to more simple version
reactant(M,R) :- reactant(M,R,N).
product(M,R) :- product(M,R,N).
reaction(R) :- reaction(R,"draft").
ireaction(R) :- reaction(R,"repairnet"), not reaction(R,"draft").

% repair
% choose interesting reactions to extend the network.
% dont extend with already existing reactions.
%{ xreaction(R) : ireaction(R,N) }.
{ xreaction(R) : ireaction(R) }.

% a reaction is applied if all reactants are available
areaction(R) :- available(M) : reactant(M,R), reaction(R).
areaction(R) :- available(M) : product(M,R), reaction(R), reversible(R).

% an xreaction is applied if all reactants are available
areaction(R) :- available(M) : reactant(M,R), xreaction(R).
areaction(R) :- available(M) : product(M,R), xreaction(R), reversible(R).



% a metabolite is available if it is given as a seed or if it is the product of an applied reaction
available(X) :- seed(X).
available(X) :- product(X,R), areaction(R).
available(X) :- reactant(X,R), areaction(R), reversible(R).


reach(X) :- seed(X).
reach(X) :- product(X,R), reactant(Y,R), reach(Y).
reach(X) :- reactant(X,R), product(Y,R), reach(Y), reversible(R).

% a metabolite might be available or not
{ available(X) } :- reach(X). 

% atleast one reaction must be producing X
% if all are inactive it is not a solution 
is_produced(X) :- areaction(R), product(X,R).
is_produced(X) :- reactant(X,R), areaction(R), reversible(R).
:- not is_produced(X), available(X), not seed(X).

% there must be a path of active reactions from the seeds to the available metabolite
founded(X) :- seed(X).
founded(X) :- product(X,R), reactant(Y,R), areaction(R), founded(Y).
founded(X) :- reactant(X,R), product(Y,R), areaction(R), founded(Y), reversible(R).
:- available(X), not founded(X).


% every target must be available
:- target(X), not available(X).

#minimize [ not false= 0, xreaction(R)  : ireaction(R) ].

#hide.
#show xreaction(R).



# How to create an instance for meneco++

> cd scripts/pre_instances
> python sbml2asp.py sbml/Ec_iJR904__sub__1032.sbml > Ec_iJR904__sub__1032.lp
> cat Ec_iJR904__sub__1032.lp draft.lp metaCycFix.lp seeds.lp targets.lp distance_ecoli_metacyc.lp > ../lpinstances/instance1.lp

# How to run benchmark
> bash run_bench.sh instances opt1 1 10 

TODO fix script for new clasp version

# How to create an instance for meneco++

> cd scripts/pre_instances
> python sbml2asp.py ../../benchmarkFiles/Ec_iAF1260/networks/170.sbml benchmarkFiles/Ec_iAF1260/170.sbml > Ec_iAF1260__sub__170.lp
> cat Ec_iAF1260__sub__170.lp draft.lp metaCycFix.lp seeds_Ec_iAF1260.lp targets_Ec_iAF1260_1.lp distance_ecoli_metacyc.lp > ../instances/instance1.lp

# How to run a benchmark

> cd scripts
> python run_bench.py 1 



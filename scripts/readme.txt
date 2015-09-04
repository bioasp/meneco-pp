
# How to create an instance for meneco++

> cd scripts/pre_instances
> python sbml2asp.py ../../benchmarkFiles/Ec_iJR904/withMetacycIds/networks/1032.sbml  > Ec_iJR904_sub_1032.lp
> python sbml2asp.py ../../benchmarkFiles/Ec_iJR904/withMetacycIds/networks/80.sbml  > Ec_iJR904_sub_80.lp
> cat Ec_iJR904_sub_1032.lp draft.lp metaCycFix.lp seeds.lp targets1.lp > ../instances/instance1.lp
> cat Ec_iJR904_sub_80.lp draft.lp metaCycFix.lp seeds.lp targets1.lp > ../instances/instance2.lp


# How to run a benchmark

> cd scripts
> python run_bench.py 1 



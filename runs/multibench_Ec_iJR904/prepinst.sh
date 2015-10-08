#!/usr/bin/env bash

BASE=../../benchmarkFiles/Ec_iJR904/withMetacycIds
NETWORKS_DIR=$BASE/networks
TARGETS_DIR=$BASE/targets
PRE=../../scripts/pre_instances

shopt -s nullglob

# parse seeds just once
python $PRE/sbml2asp.py $BASE/seeds/seeds.sbml | sed 's/species(/seed(/'> seeds.lp

# iterate over all models, all targets
for net in $NETWORKS_DIR/*
do
	for target in $TARGETS_DIR/*
	do
		netname=$(basename "$net")
		netname="${netname%.*}"

		targetname=$(basename "$target")
		targetname="${targetname%.*}"
		instance="instance_${netname}_${targetname}"
		echo Preparing $instance instance

		i=instances/$instance
		mkdir -p $i
		python $PRE/sbml2asp.py $net > $i/model.lp
		python $PRE/sbml2asp.py $target | sed 's/species(/target(/' > $i/targets.lp

		cat $i/model.lp $i/targets.lp $PRE/draft.lp $PRE/metaCycFix.lp seeds.lp > $i/${instance}.lp

	done
done



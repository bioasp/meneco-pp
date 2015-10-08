
# Prepare all instances (all networks x all target sets)
./prepinst.sh

# run meneco++ over each instance
# (require parallel, use -j for max number of concurrent jobs)
find instances -name "instance*.lp" | parallel -j4 "python run_bench.py 1 {} > {}.out"

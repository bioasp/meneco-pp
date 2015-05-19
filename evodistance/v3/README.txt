
# get distances for E. coli (taxid: 562) to all reactions in metacyc
python evod3.py 562 reactionsMetacyc_sansEcoli.txt  metacycnamemap.txt

# get number of reactions per distance, for E. coli versus metacyc
python evod3.py 562 reaction_organism_MetaCyc.txt metacycnamemap.txt  | grep -v WARNING | cut -d ' ' -f 2  | sort | uniq -c > distances_reaction_ecoli.txt

# get number of reactions per distance, for E. coli versus metacyc, excluding from metacyc specific E. coli reactions
grep -v "Escherichia coli" reaction_organism_MetaCyc.txt > reactionsMetacyc_sansEcoli.txt

python evod3.py 562 reactionsMetacyc_sansEcoli.txt  metacycnamemap.txt  | grep -v WARNING | cut -d ' ' -f 2  | sort | uniq -c > distances_reaction_ecoli_v2.txt

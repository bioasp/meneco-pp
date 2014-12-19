
# Evodistance

## Old protocol

To compute the evolutionary distance between *E. coli* and the rest of the organisms in MetaCyc, we used existing data from Roundup (http://roundup.hms.harvard.edu/) and MetaCyc itself.

Roundup stores orthology of genes between thousands of organisms. It uses the Reciprocal Smallest Distance algorithm (RSD), so it stores an estimated evolutionary distance between genes.

Our idea was to use the measurements from Roundup, to establish the evolutionary distance between the 16S genes of the organisms in Metacyc. In general terms, we took the *E. coli* 16S, obtained the evo distance to 16S of other organisms (via Roundup), matched those organism's names with Metacyc names, and used the 16S distance as an proxy for real evolutionary distance. The precise steps were: 


1. Obtain Roundup 3 precomputed orthologies from:  http://roundup.hms.harvard.edu/download/. I used `roundup-3-orthologs_0.5_1e-10.txt.gz`.

1. Extract list of organisms from Roundup website (see `listaOrganismos.txt`, attached)

1. Get Metacyc dump of reactions+organisms (see `reaction_organism_MetaCyc.txt`, attached)

1. Translate roundup names to metacyc names, as best as we can:

	`python matchNames.py listaOrganismos.txt reaction_organism_MetaCyc.txt > tranlations.txt`

	It's always healthy to check the translation.txt file. The `matchNames` script will produce false positives.

1. Get the distances from e-coli to other organisms, using 16S:

	```
zgrep "^PA\|P06992" roundup-3-orthologs_0.5_1e-10.txt.gz > ecolik12-others

	grep -B 1 "^OR" ecolik12-others  > PAOR

	python dist2org.py PAOR listaOrganismos.html | sort -n  > distance_ecoli_others.txt
	```

1. Generate an ASP compatible file with distance facts:

	`python metacycDistances.py distance_ecoli_others.txt tranlations.txt  > ecoli-mcyc-dist.lp`
	
This protocol was not completely successful, given: the difficulties to map organism names between roundup and metacyc, metacyc organisms not accounted for in roundup, and a very limited mapping between reactions and organism in metacyc (about 11 reactions per organism, in average).

In order to cover all of metacyc organisms, we need to compute the distances instead of using pre-computed data bases (like Roundup).


## New protocol

Evolutionary distances will be obtained using the distance provided by the RSD algorithm, comparing the 16S genes from all of metacyc's organisms. The steps are:

1. Obtain and install RSD from: https://github.com/todddeluca/reciprocal_smallest_distance

2. Obtain 16S sequences from the Ribosomal Database Project (RDP). The sequences can be obtained from: http://rdp.cme.msu.edu/misc/resources.jsp. I'm using the Unaligned fastas for Bacteria (16S).

3. Get names and IDS from RDP:

	```
zgrep "^>" release11_2_Bacteria_unaligned.fa.gz > release11_2.signature

	TAB=$'\t'; sed -e 's/^>\(S[^ ]*\) \([^;]*\);.*$/\1'"${TAB}"'\2/' -e 's/ *Lineage=Root.*$//' release11_2.signature > release11_2.names
	```


4. Translate Metacyc organism names to rdp names:

	```
python matchNames.py release11_2.names reaction_organism_MetaCyc.txt > translation_rdp.txt
```

	This generated translations for the 1 136 different metacyc names, except for 127 "NOT FOUND".

5. Obtain the 16S sequence for all of Metacyc's organisms:

	```
	sed -e 's/>\([^;]*\);.*$/\1/' -e 's/ *Lineage=.*$//' release11_2.signature |tr -d '\t' | sed 's/ *$//' > r11_2.idname
	python rdp2meta.py r11_2.idname translation_rdp.txt  > rid2metaname.txt
	cut -f 1   rid2metaname.txt | grep -v S000000000 > ridmeta2blast.ids
	fastacmd -d 16S -p F -i ridmeta2blast.ids  -o ridmeta.fasta
	```


6. BLAST between the 16S target organism (e.q.: *E. coli*) and the rest of the metacyc's 16S, in order to obtain a measure of distance:

	```
	formatdb -t ridmeta -i ridmeta.fasta -p F -o T -n ridmeta
	blastn -db ridmeta -query ridmeta.fasta -out selfblast.blast
	grep "^lcl|S004046286" selfblast.blast | cut -f 2,12  > ecoli2others.txt
	```

The `ecoli2others.txt` contains a measure of the evolutionary distance between *E. coli* and most of metacyc, based on the BLAST score of the 16S genes of the metacyc organisms.

Even if we correctly assign evolutionary distances between organisms, we are still limited by the low number of reactions assigned to organisms at the Metacyc DB.
Without a proper mapping between reactions and organisms, we cannot use the evolutionary distance as a way to prioritize reactions to be used as metabolic patches.



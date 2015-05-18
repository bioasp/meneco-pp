
import sys, os

parents = dict()
id2species = dict()


def parentLines(id):
	"""Get a list of taxonomic parents from certain node"""

	parentLine = [id]

	while id != "1":
		id = parents[id]
		parentLine.append(id)

	return parentLine

def distance(a,b):
	"""Compute the distance between organisms a and b.
		This is computed as the number of jumps up in the
		taxonomy tree, needed so both organisms are part
		of the same subtree. The further a and b are
		phylogeneticalle appart, the further up in the tree
		you have to go to find a common node.
		There is always a common node: the root of the tree.
		If both nodes are the same, distance returns 0.
	"""
	pla = parentLines(a)
	plb = parentLines(b)

	d = 0

	for id in pla:
		if id in plb:
			break
		else:
			d = d+1

	return d



def speciesDistance(a,b):
	"""Make sure that we are obtaining distances between species,
	and not from nodes under the species level. Uses data from NCBI
	categories"""

	assert a in parents, "a(%s) not in parents" % a
	assert b in parents, "b(%s) not in parents" % b

	a = id2species.get(a,a)
	b = id2species.get(b,b)

	return distance(a,b)


def parseNodes(nodesFile):
	"""Parses NCBI nodes (nodes.dmp). Remembers taxids and ids of parents"""

	parents = dict()
	for line in open(nodesFile):
		elems = line.split('|')
		id, parent = elems[0].strip(), elems[1].strip()
		parents[id] = parent

	return parents


def parseCategories(categoriesFile):
	"""Parses NCBI data (categories.dmp) that maps TAXIDs under the species line,
	to their corresponding species TAXID"""

	id2species = dict()
	for line in open(categoriesFile):
		elems = line[:-1].split()
		id2species[elems[2]]=elems[1]
	return id2species

def parseNames(namesFile):
	"""Parses TAXID and names from NCBI's names.dmp"""

	name2id = dict()
	other_kind = ["authority", "type material", "blast name"]

	for line in open(namesFile):
		elems = line.split('|')
		elems = line[:-1].split('\t')
		taxid = elems[0]
		name = elems[2].lower()
		kind = elems[6]

		if kind not in other_kind:
			name2id[name]=taxid

	return name2id

def parseMetacycNames(metanamesFile):
	"""Parse a list of Metacyc names. Skip those that do not
	look like names"""

	metaNames = set()
	for line in open(metanamesFile):
		name = line[:-1].lower()
		parts = name.split(" ")
		if len(parts)>1:
			metaNames.add(name)
	return metaNames


def parseManualMapNames(manualMapFile):
	"""Read a list of manual mapps of organisms to NCBI's taxid.
	Do not trust this mapping!
	"""
	name2manualid = dict()
	for line in open(manualMapFile):
		elems = line[:-1].split('\t')
		name2manualid[elems[0]]=elems[1]

	return name2manualid


def parseMerged(mergedFile):

	old2newtaxid = dict()

	for line in open(mergedFile):
		elems = line[:-1].split('\t')
		old, new = elems[0],elems[2]
		old2newtaxid[old] = new

	return old2newtaxid


def test():
	"""Test some known distances. Should use unittest."""
	print speciesDistance("33", "34") # 1

	print distance("1284404", "1280938") #  3
	print speciesDistance("1284404", "1280938") #  2

	print speciesDistance("562", "4932") # ecoli vs sace, 13
	print speciesDistance("4952", "4932") # yali vs sace, 3


# MAIN

nodesFile = "ncbi/nodes.dmp"
categoriesFile = "ncbi/categories.dmp"
namesFile = "ncbi/names.dmp"
mergedFile = "ncbi/merged.dmp"



parents = parseNodes(nodesFile)
id2species = parseCategories(categoriesFile)
name2id = parseNames(namesFile)
old2newtaxid = parseMerged(mergedFile)

# sys.exit(0)

# ecoli = 562
reftaxid = sys.argv[1]

metacycReactionsFile = sys.argv[2]

manualMapFile = sys.argv[3]
name2manualid = parseManualMapNames(manualMapFile)
name2id.update(name2manualid)


# iterate over metacyc's reactions

reaction2distance = dict()

for line in open(metacycReactionsFile):
	rid, taxid, orgname = line[:-1].split('\t')
	# print "[%s][%s][%s]" % (rid, taxid, orgname)
	orgname = orgname.lower()

	d = 1000
	if taxid.startswith("TAX-"):
		taxid = taxid[4:]
		taxid = old2newtaxid.get(taxid, taxid)
		d = speciesDistance(reftaxid, taxid)
	else:
		if orgname in name2id:
			taxid = name2id[orgname]
			d = speciesDistance(reftaxid, taxid)
		else:
			print "WARNING: org: [%s] not in database" % (orgname)
			continue

	# distace should be valid
	assert d != 1000

	# print "Distance for reaction [%s] is [%d]" % (rid, d)
	reaction2distance[rid] = min(d, reaction2distance.get(rid, 1000))

# output min distance per reaction
for rid, d in reaction2distance.iteritems():
	print rid, d

#### Remember, remember:

# for name in metaNames:

# 	if name not in name2id:
# 		if name not in name2manualid:
# 			targetid = "["+name+"]"
# 			dist = -1
# 			# print name
# 		else:
# 			targetid = name2manualid[name]
# 			dist = speciesDistance(reftaxid, targetid)
# 	else:
# 		targetid = name2id[name]
# 		dist = speciesDistance(reftaxid, targetid)

# 	print "%d %s" % (dist, name)




import sys, os


# id2node = dict()

# class node(object):
# 	def __init__(self, id, parent=None):
# 		self.id = id
# 		self.parent = parent

parents = dict()
id2species = dict()

def distance(a,b):
	assert a != None
	assert b != None

	if a==b:
		# print "00000000000"
		return 0
	else:
		# print a,b
		return 1+distance(parents[a], parents[b])

def parentLines(id):

	parentLine = [id]

	while id != "1":
		id = parents[id]
		parentLine.append(id)

	return parentLine

def distance2(a,b):
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
	a = id2species[a]
	b = id2species[b]

	return distance2(a,b)


def parseNodes(nodesFile):
	parents = dict()
	for line in open(nodesFile):
		elems = line.split('|')
		id, parent = elems[0].strip(), elems[1].strip()
		parents[id] = parent

	return parents


def parseCategories(categoriesFile):
	id2species = dict()
	for line in open(categoriesFile):
		elems = line[:-1].split()
		id2species[elems[2]]=elems[1]
	return id2species

def parseNames(namesFile):
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
	metaNames = set()
	for line in open(metanamesFile):
		name = line[:-1].lower()
		parts = name.split(" ")
		if len(parts)>1:
			metaNames.add(name)
	return metaNames


def parseManualMapNames(manualMapFile):
	name2manualid = dict()
	for line in open(manualMapFile):
		elems = line[:-1].split('\t')
		name2manualid[elems[0]]=elems[1]

	return name2manualid

def test():
	print speciesDistance("33", "34") # 1

	print distance("1284404", "1280938") #  3
	print speciesDistance("1284404", "1280938") #  2

	print speciesDistance("562", "4932") # ecoli vs sace, 13
	print speciesDistance("4952", "4932") # yali vs sace, 3



# main

nodesFile = sys.argv[1]
parents = parseNodes(nodesFile)

categoriesFile = sys.argv[2]
id2species = parseCategories(categoriesFile)

namesFile = sys.argv[3]
name2id = parseNames(namesFile)

metanamesFile = sys.argv[4]
metaNames = parseMetacycNames(metanamesFile)

manualMapFile = sys.argv[5]
name2manualid = parseManualMapNames(manualMapFile)

ecoli = "380394"

for name in metaNames:

	if name not in name2id:
		if name not in name2manualid:
			targetid = "["+name+"]"
			dist = -1
			print name
		else:
			targetid = name2manualid[name]
			dist = speciesDistance(ecoli, targetid)
	else:
		targetid = name2id[name]
		dist = speciesDistance(ecoli, targetid)

	# print "%d %s" % (dist, name)



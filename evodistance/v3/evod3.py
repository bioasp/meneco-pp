
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
		return 0
	else:
		return 1+distance(parents[a], parents[b])

def speciesDistance(a,b):
	a = id2species[a]
	b = id2species[b]

	return distance(a,b)


def parseNodes(nodesFile):
	parents
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

print name2id


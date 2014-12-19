# -*- coding: utf-8 -*-
# Nicolas Loira
# nloira@gmail.com

from __future__ import print_function


import sys,io
import difflib
from collections import defaultdict


def log(*objs):
	print("LOG: ", *objs, file=sys.stderr)


roundupNames=sys.argv[1]
metacycNames=sys.argv[2]

# load roundup id-names, but take only the first two words of names, storing a list of ids for each one

name2id=defaultdict(set)
allNames=set()

log("Parsing roundup names")
for line in open(roundupNames):
	elems=line[:-1].split('\t')
	# name=elems[1]+" "+elems[2]
	name=elems[1]
	oid=elems[0]
	allNames.add(name)
	name2id[name].add(oid)

# now parse metacyc file and try to match names with known roundup names
translation=dict()

log("Parsing metacyc names")

linecount=0
for line in open(metacycNames):
	linecount += 1
	if linecount == 20:
		sys.exit(1)

	elems=line[:-1].split('\t')
	mcname=elems[2]
	if mcname not in translation:
		best=difflib.get_close_matches(mcname, allNames)
		if len(best)>0: translation[mcname]=best[0]
		else: translation[mcname]="NOT FOUND"
		print(mcname+"\t"+translation[mcname])
		log("Translating %s as %s" % (mcname,translation[mcname]))
	else:
		log("%s not in translation" % (mcname))

	
	

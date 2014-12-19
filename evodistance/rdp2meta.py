# Nicolas Loira
# nloira@gmail.com

import sys,os

rid2nameFile = sys.argv[1]
translationFile = sys.argv[2]

# fisrt go for r11 names->ids
name2id=dict()
for line in open(rid2nameFile):
	try:
		id,name = line.split(' ',1)
		name = name[:-1]
		name2id[name]=id

	except:
		# no space, just skip it
		continue

# now go for metacyc names

for line in open(translationFile):
	metaname, rname = line.split('\t')
	rname = rname[:-1]

	id=name2id.get(rname, "S000000000")
	print "%s\t%s" % (id, metaname)


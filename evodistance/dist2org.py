# Nicolas Loira
# nloira@gmail.com 

import sys,os

lastPA=None

baseOrg="83333"
baseGene="P06992"

roundupFile=sys.argv[1]
listOfOrganisms=sys.argv[2]

orgName=dict()

for line in open(listOfOrganisms):
	oid,name = line.split("\t",1)
	orgName[oid]=name[:-1]


for line in open(roundupFile):
	signal=line[0:2]
	if signal=="--":
		continue
	elif signal=="PA":
		elems=line.split()
		if elems[1]==baseOrg: lastPA=elems[2]
		else: lastPA=elems[1]
	elif signal=="OR":
		assert lastPA!=None, "No PA defined"
		elems=line.split()
		if elems[1]==baseGene: gene=elems[2]
		else: gene=elems[1]

		print "%s %s" % (elems[3], orgName.get(lastPA,lastPA+"?"))
	else:
		assert False, "Wrong signal"


	


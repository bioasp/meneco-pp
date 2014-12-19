# Nicolas Loira
# nloira@gmail.com

import sys,os


def discretize(dist):
	dd=0
	if dist<0.0: dd=5
	elif dist<0.7: dd=1
	elif dist<1.5: dd=2
	elif dist<3.0: dd=3
	else: dd=4

	assert dd>0 and dd<=5

	return dd


distanceFile=sys.argv[1]
translateFile=sys.argv[2]

translation=dict()
for line in open(translateFile):
	mcName,ruName = line[:-1].split("\t",1)
	translation[mcName]=ruName

distance=dict()
for line in open(distanceFile):
	ruDistance, ruName = line[:-1].split(' ',1)
	distance[ruName]=ruDistance

# Output

for mcName in translation.keys():
	ruName=translation[mcName]

	if ruName not in distance:
		ruDistance=-1.0
	else:
		ruDistance=float(distance[ruName])
	print "distance(\"Escherichia coli\", \"%s\", %f)." % (mcName, ruDistance)
		
	dd=discretize(ruDistance)
	print "discrete_distance(\"Escherichia coli\", \"%s\", %d)." % (mcName, dd)



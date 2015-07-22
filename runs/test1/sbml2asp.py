#!/usr/bin/env python
# encoding: utf-8

"""
sbml2asp.py

Created by Nicolas Loira on 2013.
Copyright (c) 2013 Universidad de Chile.
"""

import sys

sbmlFile = sys.argv[1]


def getId(line):
	posId=line.find('id="')+4
	lastPos=line.find('"',posId)
	id=line[posId:lastPos]
	return id
	
	
def getSpecies(line):
	posId=line.find('species="')+9
	lastPos=line.find('"',posId)
	species=line[posId:lastPos]
	return species

def is_reversible(line):
	if 'reversible="true"' in line:
		return True
	else:
		return False



lastRID="ERROR"
mode=None

for line in open(sbmlFile):
	# SPECIES
	if line.find("<species ")>-1:
		print 'species("'+getId(line)+'").'
	elif line.find("<reaction ")>-1:
		rid=getId(line)
		print 'reaction("'+rid+'", "draft").'
		lastRID=rid
		if is_reversible(line):
			print 'reversible("'+rid+'").'
		mode=None
	elif line.find("<listOfProducts>")>-1:
		mode="product"
	elif line.find("<listOfReactants>")>-1:
		mode="reactant"
	elif line.find("<speciesReference ")>-1:
		s=getSpecies(line)
		assert mode!=None
		print "%s(\"%s\",\"%s\", \"draft\")." % (mode, s, lastRID)
		
# REACTANT("cpd11590_e","EX_cpd11590_e", "draft")
# cpd11590_b
		
		
		
		
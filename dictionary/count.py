#!usr/bin/python

import pandas
import json

def buildEdgesDict(l1,l2):
 	edgeDict = {}
 	indexlen = (len(l2))
 	for item in range(indexlen):
 		edgeDict[l1[item]] = []
 	return edgeDict

def buildEdgeDict2(l1,l2):
 	edgeDict = buildEdgesDict(l1,l2)
 	indexlen = (len(l2))
 	for item in range(indexlen):
 		l = edgeDict[l1[item]]
 		value = l2[item]
 		l.append(value)
 		edgeDict[l1[item]] = l
 	return edgeDict

def initialigeRecommender(edgeDict):
	d={}
	
	for k in edgeDict.keys():
		key = edgeDict[k]
		for i in key:
			d[i]=[]
	print d
	return d


def builRecommender(edgeDict):
	b = initialigeRecommender(edgeDict)
	
	
	return b

l1 = [1,2,3,3,3,4,4,5]
l2	= ['a','a','b','c','d','e','a','f']
edgeDict=buildEdgeDict2(l1,l2)
# builRecommender(edgeDict)
initialigeRecommender(edgeDict)
# buildEdgesDict(l1,l2)
# buildEdgeDict2(l1,l2)


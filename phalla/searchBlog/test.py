#!usr/bin/python

def buildEdge(l1,l2):
	edgeDict={}
	for i in range(len(l1)):
		edgeDict[l1[i]]=[]
	return edgeDict
l1=[1,2,3,3,3,4,4,5]
l2=[0012,0012,0013,0112,0121,0013,0012,0001]
print buildEdge(l1,l2)


def buildEdge2(l1,l2):
	edgeDict=buildEdge(l1,l2)
	for l in range(len(l2)):
		data=l2[l]
		empty=edgeDict[l1[l]]
		empty.append(data)
		edgeDict[l1[l]]=empty
	return edgeDict
l1=[1,2,3,3,3,4,4,5]
l2=[0012,0012,0013,0112,0121,0013,0012,0001]
print buildEdge2(l1,l2)
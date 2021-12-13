class Group():
	def __init__(self,value):
		self.value = value
		self.parent = self

	def findRootParent(self):
		if self.parent is self:
			return self
		else:
			return self.parent.findRootParent()

	def join(self,GroupObject):
		godParent = self.findRootParent()
		godParent.parent = GroupObject.findRootParent()

def findComponents_undirectedGraph(vertices, edges):
	nodes = {i:Group(i) for i in vertices}
	noOfGroups = len(vertices)
	for e1, e2 in edges:
		if nodes[e1].findRootParent() is not nodes[e2].findRootParent():
			nodes[e1].join(nodes[e2])
			noOfGroups -= 1

	return noOfGroups
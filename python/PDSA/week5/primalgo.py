class Node:
	def __init__(self, data, neighbour, connNeighbour = []):
		self.data = data
		self.neighbour = neighbour
		self.connNeighbour = connNeighbour
		self.visited = False

class primsAlgorithm():
	def __init__(self, graph):
		self.graph = graph
		self.noOfVer = len(self.graph)

	def execute(self):
		vertices = {i:Node(i) for i in range(self.noOfVer)}

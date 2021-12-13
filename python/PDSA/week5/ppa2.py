inf = float('infinity')
mat = [
	[  0,  -1,   4, inf, inf],
	[inf,   0,   3,   2,   2],
	[inf, inf,   0, inf, inf],
	[inf,   1,   5,   0, inf],
	[inf, inf, inf,  -3,   0],
]

class Node:
	def __init__(self,data, cost = float('infinity')):
		self.data = data
		self.cost = cost
		self.parent = None

class bellmanFordAlgo():
	def __init__(self, graph, source):
		self.inf = float('infinity')
		self.graph = graph
		self.noOfVer = len(graph)
		self.source = source
		self.resGraph =  self.computeEndState()

	def nextState(self, state):
		temp = state.copy()
		for i in range(self.noOfVer):
			begin = state[i].cost
			for j in range(self.noOfVer):
				newVal = begin + self.graph[i][j]
				if newVal < temp[j].cost:
					temp[j].cost = newVal
					temp[j].parent = state[i]
		return temp

	def computeEndState(self):
		blankGraph = [[Node(i) if (i != self.source) else Node(i,0) for i in range(self.noOfVer)]]
		for i in range(1,self.noOfVer):
			blankGraph.append(self.nextState(blankGraph[-1]))
		return blankGraph[-1]

	def computeCost(self, dest):
		return self.resGraph[dest].cost

	def computePath(self, dest):
		if self.source == dest:
			return [dest]
		else:
			res = self.computePath(self.resGraph[dest].parent.data)
			res.append(dest)
			return res
		
def min_cost(WL,s,d):
    noOfVar = len(WL)
    inf = float('infinity')
    mat = [[inf if i != j else 0 for j in range(noOfVar)] for i in range(noOfVar)]
    for i in WL:
        for j in WL[i]:
            mat[i][j[0]] = j[1]
    graph = bellmanFordAlgo(mat,s)
    return (graph.computeCost(d), graph.computePath(d))
		
		
size = 8
edges = [(0,1,1000),(0,7,800),(1,5,200),(2,1,100),(2,3,100),(3,4,300),(4,5,500),(5,2,-200),(2,4,-200),(6,1,400),(6,5,100),(7,6,100)]
s = 0
d = 1
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges: #for create list for directed graph
    WL[ed[0]].append((ed[1],ed[2]))
print(min_cost(WL,s,d))
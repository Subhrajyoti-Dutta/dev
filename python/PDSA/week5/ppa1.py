class Node():
	def __init__(self, val):
		self.val = val
		self.time = float('infinity')
		self.parent = None
		self.visited = False

	def newTime(self, time, parent):
		if time < self.time:
			self.time = time
			self.parent = parent

class XYZ_Courier():
	def __init__(self, routeMap):
		self.routeMap = routeMap

	def nextVerFinder(self):
		min = float('infinity')
		ver = None
		for i in self.timeLog:
			if not self.timeLog[i].visited and self.timeLog[i].time < min:
				min = self.timeLog[i].time
				ver = i

		return self.timeLog[ver]

	def computePath(self, s, d):
		if d == s:
			return [d]
		else:
			res = self.computePath(s, self.timeLog[d].parent.val)
			res.append(d)
			return res

	def computeCost(self, s, d):
		return self.timeLog[d].time

	def dijktraAlgorithms(self, s, d):
		self.timeLog = {i:Node(i) for i in self.routeMap.keys()}
		source = self.timeLog[s]
		source.newTime(0, -1)
		while True:
			currVer = self.nextVerFinder()
			if currVer.val == d:
				break

			for child, w in self.routeMap[currVer.val]:
				self.timeLog[child].newTime(w + currVer.time, currVer)

			currVer.visited = True


	def cost(self, s, d):
		self.dijktraAlgorithms(s, d)
		return self.computeCost(s, d)
	
	def route(self, s, d):
		self.dijktraAlgorithms(s, d)
		return self.computePath(s, d)



size = 7
edges = [(0,1,10),(0,2,50),(0,3,300),(5,6,45),(2,1,30),(6,4,37),(1,6,65),(2,5,76),(1,3,40),(3,4,60),(2,4,20)]
s=0
d=4
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges: #for create list for undirected graph
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
C = XYZ_Courier(WL)
print(C.cost(s,d))
print(C.route(s,d))
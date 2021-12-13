a = '''XXXXXXXXXXXXXX
   X    XXX  X
X  X    X X  X
X  X         X
X  XX  X XX  X
X  X  XX  X   
X     XX XXXXX
X  X         X
X  X      *  X
XXXXXXXXXXXXXX'''
res = [[1 if w == 'X' else (2 if w == '*' else 0) for w in i] for i in a.split('\n')]

print(a)



class Maze:
	def __init__(self,mazeLayout):
		self.mazeLayout = mazeLayout
		self.dim = (len(self.mazeLayout), len(self.mazeLayout[0]))
		self.entryLoc = self.entrance(),0
		self.exitLoc = self.exit(),self.dim[1]
		self.keyLoc = self.key()

	def entrance(self):
		for i in range(self.dim[0]):
			if self.mazeLayout[i][0] == 0:
				return i

	def exit(self):
		for i in range(self.dim[0]):
			if self.mazeLayout[i][-1] == 0:
				return i

	def key(self):
		for i in range(self.dim[0]):
			for j in range(self.dim[1]):
				if self.mazeLayout[i][j] == 2:
					return (i,j)
	def valAt(self,i, j):
		if i < 0 or j < 0 or i >= self.dim[0] or j >= self.dim[1]:
			return 1
		return self.mazeLayout[i][j]

	def keyInSurrounding(self,i,j):
		return (self.valAt(i+1,j) == 2) or (self.valAt(i,j+1) == 2) or (self.valAt(i-1,j) == 2) or (self.valAt(i,j-1) == 2)


def modifiedBFS(maze):
	entry = maze.entryLoc
	visited = []
	yetToVisit = [(entry[0],entry[1],0)]
	stepsEntryToKey = -1
	while len(yetToVisit) > 0:
		loci, locj, locsteps = yetToVisit.pop(0)
		if (loci,locj) not in visited:
			if maze.keyInSurrounding(loci,locj):
				stepsEntryToKey = locsteps + 1
				break
			if maze.valAt(loci+1,locj) == 0:
				yetToVisit.append((loci+1,locj,locsteps+1))
			if maze.valAt(loci,locj+1) == 0:
				yetToVisit.append((loci,locj+1,locsteps+1))
			if maze.valAt(loci-1,locj) == 0:
				yetToVisit.append((loci-1,locj,locsteps+1))
			if maze.valAt(loci,locj-1) == 0:
				yetToVisit.append((loci,locj-1,locsteps+1))
			visited.append((loci,locj))

	if stepsEntryToKey == -1:
		return -1
	exit = maze.exitLoc
	visited = []
	yetToVisit = [(exit[0],exit[1],0)]
	stepsExitToKey = -2
	while len(yetToVisit) > 0:
		loci, locj, locsteps = yetToVisit.pop(0)
		if (loci,locj) not in visited:
			if maze.keyInSurrounding(loci,locj):
				stepsExitToKey = locsteps + 1
				break
			if maze.valAt(loci+1,locj) == 0:
				yetToVisit.append((loci+1,locj,locsteps+1))
			if maze.valAt(loci,locj+1) == 0:
				yetToVisit.append((loci,locj+1,locsteps+1))
			if maze.valAt(loci-1,locj) == 0:
				yetToVisit.append((loci-1,locj,locsteps+1))
			if maze.valAt(loci,locj-1) == 0:
				yetToVisit.append((loci,locj-1,locsteps+1))
			visited.append((loci,locj))

	if stepsExitToKey == -2:
		return -2

	return stepsEntryToKey+stepsExitToKey-1


myMaze = Maze(res)
print(modifiedBFS(myMaze))
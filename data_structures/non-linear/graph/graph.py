from vertex import Vertex
class Graph:

	def __init__(self):
		self.vertList = {}
		self.numVertices = 0

	def addVertex(self, key):
		self.vertList[key] = Vertex(key)
		self.numVertices += 1

	def getVertex(self, n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None

	def __contains__(self, n):
		return n in vertList

	def getVertices(self):
		return self.vertList.keys()

	def __iter__(self):
		return iter(self.vertList.values())

	def addEdge(self, f, t, cost=0):
		if f not in self.vertList:
			self.addVertex(n)
		if t not in self.vertList:
			self.addVertex(t)
		self.vertList[f].addNeighbour(self.vertList[t],cost)


#Test Cases
g = Graph()
for i in range(6):
	g.addVertex(i)
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

# for v in g:
# 	for w in v.getConnections():
# 		print("( %s, %s )" % (v.getId(), w.getId()))
assert str(g.getVertex(3)) == '3 connected to : [5, 4]'
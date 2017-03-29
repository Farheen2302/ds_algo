class Vertex:

	def __init__(self, key):
		self.id = key
		self.connectedTo = {}
		self.color = 'white'
		self.pred = None

	def addNeighbour(self, nbr, weight=0):
		self.connectedTo[nbr] = weight

	def __str__(self):
		return str(self.id) + ' is connected to : ' + str([x.id for x in self.connectedTo])

	def getConnections(self):
		return self.connectedTo.keys()

	def getId(self):
		return self.id

	def getWeight(self, nbr):
		return self.connected[nbr]

	def setPred(self, p):
		self.pred = p

	def getPred(self):
		return self.pred

	def setColor(self, color):
		self.color = color

	def getColor(self):
		return self.color
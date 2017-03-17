# Max Heap
class BinaryHeap:

	def __init__(self):
		self.list = [0]
		self.size = 0

	def insert(self, element):
		self.list.append(element)
		self.size += 1
		self._insert(self.size)

	def _insert(self, size):
		while size // 2 > 0:
			if self.list[size] > self.list[size // 2]:
				self.list[size], self.list[size // 2] = self.list[size // 2], self.list[size]
		size = size // 2

	def findMax(self):

	def delMax(self):

	def isEmpty(self):

	def size(self):

	def buildHeap(self):


bh = BinaryHeap([9,5,6,2,3])

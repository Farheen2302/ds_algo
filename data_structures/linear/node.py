class Node:

	def __init__(self, value):
		self.value = value
		self.next = None

	def getValue(self):
		return self.value

	def setValue(self, newVvalue):
		self.value = newVvalue

	def getNext(self):
		return self.next

	def setNext(self, newNext):
		self.next = newNext

	def __str__(self):
		return str(self.getValue())



# Test cases

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.setNext(n2)
n2.setNext(n3)
assert n1.getValue() == 1
assert n2.getNext().getValue() == 3

from linked_list import UOLinkedList


class Queue:

	def __init__(self, first=None):
		self.list = UOLinkedList(first)

	def enqueue(self, item):
		self.list.add(item)

	def size(self):
		return self.list.getSize()

	def dequeue(self):
		self.list.delete(self.size())


#Test Cases
q = Queue()
q.enqueue(23)
q.enqueue(24)
q.enqueue(25)
q.enqueue(26)
assert q.size() == 4
q.dequeue()
assert q.size() == 3

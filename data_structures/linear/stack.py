from linked_list import UOLinkedList


class Stack:

	def __init__(self, first=None):
		self.list = UOLinkedList(first)

	def push(self, item):
		self.list.add(item)

	def pop(self):
		self.list.delete(0)

	def size(self):
		return self.list.getSize()

	def peek(self):
		return self.list.head.getValue()


#Test Cases
s = Stack()
s.push(23)
s.push(24)
s.push(25)
s.push(26)
s.push(27)
assert s.peek() == 27
assert s.size() == 5
s.pop()
assert s.size() == 4
assert s.peek() == 26


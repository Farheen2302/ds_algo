from treenode import TreeNode


class BinarySearchTree:

	def __init__(self):
		self.root = None
		self.size = 0

	def length(self):
		return self.size

	def __len__(self):
		return self.size

	def __iter__(self):
		return self.root.__iter__()

	def __setitem__(self, k, v):
		self.put(k, v)

	def put(self, key, val):
		if self.root:
			self._put(key, val, self.root)
		else:
			self.root = TreeNode(key, val)
		self.size += 1

	def _put(self, key, val, currentNode):
		if key <= currentNode.key:
			if currentNode.hasLeftChild():
				self._put(key, val, currentNode.leftChild)
			else:
				currentNode.leftChild = TreeNode(key, val, parent=currentNode)
		else:
			if currentNode.hasRightChild():
				self._put(key, val, currentNode.rightChild)
			else:
				currentNode.rightChild = TreeNode(key, val, parent=currentNode)

	def __getitem__(self, k):
		return self.get(k)

	def get(self, key):
		if self.root:
			return self._get(key, self.root).payload
		else:
			return None

	def _get(self, key, currentNode):
		if not currentNode:
			return None
		elif key == currentNode.key:
			return currentNode
		elif key < currentNode.key:
			return self._get(key, currentNode.leftChild)
		else:
			return self._get(key, currentNode.rightChild)

	def __delitem__(self, key):
		self.remove(key)

	def remove(self, key):
		if self.size > 1:
			nodeToRemove = self._get(key)
			if nodeToRemove:
				self._remove(nodeToRemove)
				self.size -= 1
			else:
				raise KeyError("Key wasn't there !! ")
		elif self.size == 1 and self.root.key == key:
			self.root = None
			self.size -= 1
		else:
			raise KeyError("Key wasn't there !! ")

	def _remove(self, currentNode):
		if currentNode.isLeaf():
			if currentNode == currentNode.parent.leftChild:
				currentNode.parent.leftChild = None
			else:
				currentNode.parent.rightChild = None
		elif currentNode.hasBothChildren():
			succ = currentNode.findSuccessor()
			succ.spliceOut()
			currentNode.key = succ.key
			currentNode.payload = succ.parent
		else:
			if currentNode.hasLeftChild():
				if currentNode.isLeftChild():
					currentNode.leftChild.parent = currentNode.parent
					currentNode.parent.leftChild = currentNode.leftChild
				elif currentNode.isRightChild():
					currentNode.leftChild.parent = currentNode.parent
					currentNode.parent.rightChild = currentNode.leftChild
				# Root
				else:
					currentNode.replaceNodeData(currentNode.leftChild.key, currentNode.leftChild.payload, 
						currentNode.leftChild.leftChild, currentNode.leftChild.rightChild)
			else:
				if currentNode.isLeftChild():
					currentNode.rightChild.parent = currentNode.parent
					currentNode.parent.leftChild = currentNode.rightChild
				elif currentNode.isRightChild():
					currentNode.rightChild.parent = currentNode.parent
					currentNode.parent.rightChild = currentNode.rightChild
				else:
					currentNode.replaceNodeData(currentNode.rightChild.key, currentNode.rightChild.payload,
						currentNode.rightChild.leftChild, currentNode.rightChild.rightChild)

	def findSuccessor(self):
		





mytree = BinarySearchTree()
mytree[3] = "red"
mytree[4] = "blue"
mytree[6] = "yellow"
mytree[2] = "at"
assert mytree[2] == "at"
assert mytree[4] == 'blue'

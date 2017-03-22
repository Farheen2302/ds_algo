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
				self.updateBalance(currentNode.leftChild)
		else:
			if currentNode.hasRightChild():
				self._put(key, val, currentNode.rightChild)
			else:
				currentNode.rightChild = TreeNode(key, val, parent=currentNode)
				self.updateBalance(currentNode.rightChild)

	def updateBalance(self, node):
		if node.bf > 1 or node.bf < -1:
			self.rebalance(node)
			return
		if node.parent:
			if node.isLeftChild():
				node.parent.bf += 1
			elif node.isRightChild():
				node.parent -= 1
			if node.parent.bf != 0:
				self.updateBalance(node.parent)

	def rotatateLeft(self, rotroot):
		newRoot = rotroot.rightChild
		rotroot.rightChild = newRoot.leftChild
		rotroot.parent = newRoot
		if newRoot.leftChild:
			newRoot.leftChild.parent = rotroot
		newRoot.parent = rotroot.parent
		if rotroot.isRoot():
			self.root = newRoot
		else:
			if rotroot.isLeftChild():
				rotroot.parent.leftChild = newRoot
			else:
				rotroot.parent.rightChild = newRoot
		newRoot.leftChild = rotroot
		rotRoot.bf = rotRoot.bf + 1 - min(newRoot.bf, 0)
    	newRoot.bf = newRoot.bf + 1 + max(rotRoot.bf, 0)

    def rotateRight(self, rotroot):

    def rebalance(self, node):


	def __getitem__(self, k):
		return self.get(k)

	def get(self, key):
		if self.root:
			res = self._get(key, self.root)
			if res:
				return res.payload
			else:
				return None
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
			nodeToRemove = self._get(key, self.root)
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

	""" The successor can have two possiblities (It is either from a left subtree or from a right subtree).
	Left subtree - The successor has to be the largest value from the left subtree so as to maintain the bst property.
	Right subtree - The successor has to be the smallest value from the right subtree so as to maintain the bst property.
	Either of them will never have two children because they are already the smallest or the largest.
	The right subtree is considered here."""

	def findSuccessor(self):
		succ = None
		if self.hasRightChild():
			succ = self.rightChild.findMin()
		return succ

	def findMin(self):
		currentNode = self
		while currentNode.hasLeftChild():
			currentNode = currentNode.leftChild
		return currentNode

	def spliceOut(self):
		if self.isLeaf():
			if self.isLeftChild():
				self.parent.leftChild = None
			else:
				self.parent.rightChild = None
		elif self.hasAnyChildren():
			if self.hasLeftChild():
				if self.isLeftChild():
					self.parent.leftChild = self.leftChild
				else:
					self.parent.rightChild = self.leftChild
				self.leftChild.parent = self.parent
			else:
				if self.isLeftChild():
					self.parent.leftChild = self.rightChild
				else:
					self.parent.rightChild = self.rightChild
				self.rightChild.parent = self.parent

	def __iter__(self):
		if self:
			if self.hasLeftChild():
				for elem in self.leftChild:
					yield elem
			yield self.key
			if self.hasRightChild():
				for elem in self.rightChild:
					yield elem


mytree = BinarySearchTree()
mytree[3] = "red"
mytree[4] = "blue"
mytree[6] = "yellow"
mytree[2] = "at"
assert mytree[2] == "at"
assert mytree[4] == 'blue'
mytree.remove(6)
assert mytree[6] == None
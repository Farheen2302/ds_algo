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
			return self._get(key, self.root)
		else:
			return None

	def _get(self, key, currentNode):
		if not currentNode:
			return None
		elif key == currentNode.key:
			return currentNode.payload
		elif key < currentNode.key:
			return self._get(key, currentNode.leftChild)
		else:
			return self._get(key, currentNode.rightChild)


mytree = BinarySearchTree()
mytree[3] = "red"
mytree[4] = "blue"
mytree[6] = "yellow"
mytree[2] = "at"

assert mytree[2] == "at"

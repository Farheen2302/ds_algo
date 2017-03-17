from binarytree import BinaryTree

def preorder(tree):
	if tree:
		print(tree.getRootVal())
		preorder(tree.getLeftChild())
		preorder(tree.getRightChild())

def inorder(tree):
	if tree:
		inorder(tree.getLeftChild())
		print(tree.getRootVal())
		inorder(tree.getRightChild())

def postorder(tree):
	if tree:
		postorder(tree.getLeftChild())
		postorder(tree.getRightChild())
		print(tree.getRootVal())



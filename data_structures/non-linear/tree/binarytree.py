class BinaryTree:

    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def getRootVal(self):
        return self.key

    def setRootVal(self, newVal):
        self.key = newVal

    def insertLeft(self, newNode):
        if self.getLeftChild() == None:
            self.leftChild = BinaryTree(newNode)
        else:
        	tmp = BinaryTree(newNode)
        	tmp.leftChild = self.leftChild
        	self.leftChild = tmp

    def insertRight(self, newNode):
    	if self.getRightChild() == None:
    		self.rightChild = BinaryTree(newNode)
    	else:
    		tmp = BinaryTree(newNode)
    		tmp.rightChild = self.rightChild
    		self.rightChild = tmp


r = BinaryTree('a')
assert r.getLeftChild() == None
r.insertLeft('b')
assert (r.getLeftChild().getRootVal()) == 'b'
r.insertRight('c')
assert (r.getRightChild().key) == 'c'
r.getRightChild().setRootVal('hello')
assert (r.getRightChild().getRootVal()) == 'hello'
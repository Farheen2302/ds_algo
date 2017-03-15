""" Lists of lists implementation of tree
my_tree = ['a',   # root
	['b', 		  # left tree
		['d', [], []],
		['e', [], []]
	],
	['c',		  # right tree
		['f', [], []],
		['g', [], []]
	]
]
"""


def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    left = root.pop(1)
    if len(left) > 1:
        root.insert(1, [newBranch, left, []])
    else:
        root.insert(1, [newBranch, [], []])


def insertRight(root, newBranch):
    right = root.pop(2)
    if len(right) > 1:
        root.insert(2, [newBranch, [], right])
    else:
        root.insert(2, [newBranch, [], []])


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(tree):
    return tree[1]


def getRightChild(tree):
    return tree[2]


r = BinaryTree(3)
assert r == [3, [], []]
insertLeft(r, 4)
assert r == [3, [4, [], []], []]
insertLeft(r, 5)
assert r == [3, [5, [4, [], []], []], []]
insertRight(r, 6)
insertRight(r, 7)
l = getLeftChild(r)
assert l == [5, [4, [], []], []]
setRootVal(l, 9)
assert r == [3, [9, [4, [], []], []], [7, [], [6, [], []]]]
insertLeft(l, 11)
assert r == [3, [9, [11, [4, [], []], []], []], [7, [], [6, [], []]]]
print()
assert getRightChild(getRightChild(r)) == [6, [], []]

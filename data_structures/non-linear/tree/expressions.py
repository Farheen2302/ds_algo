from binarytree import BinaryTree
import operator


""" 
Parse expressions like ((7+3)*(5−2)) uisng 
a tree data structure print the evaluated result as well

Rules
1. If the character is '(', create a new node and go to the left child of this new node.
2. If character is '+', '/', '*' or '-' set the root key to the operator, create a right child and go to the right child.
3. If character is a nummber, set the root value and go to the parent.
4. If character is ')', go to the parent.

"""


def buildTree(exp):
    tree = BinaryTree('')
    stack = []
    stack.append(tree)
    current = tree
    for char in exp:
        if char == '(':
            current.insertLeft('')
            stack.append(current)
            current = current.getLeftChild()
        elif char not in ['+', '-', '*', '/', '(', ')']:
            current.setRootVal(int(char))
            current = stack.pop()
        elif char in ['+', '-', '*', '']:
            current.setRootVal(char)
            current.insertRight('')
            stack.append(current)
            current = current.getRightChild()
        elif char == ')':
            current = stack.pop()
        else:
            return ValueError
    return tree


def evaluate(tree):
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    leftC = tree.getLeftChild()
    rightC = tree.getRightChild()
    if leftC and rightC:
        fn = opers[tree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return tree.getRootVal()

exp = "((5+4)*(2+4))"
tree = buildTree(exp)
assert evaluate(tree) == 54

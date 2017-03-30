# Enter your code here. Read input from STDIN. Print output to STDOUT
""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
import sys
MAX = sys.maxsize
MIN = -sys.maxsize -1

def check_binary_search_tree_(root):
    return validate_bst(root, MIN, MAX)

def validate_bst(current, min, max):
    if current is None:
        return True
    if current.data <= min or current.data >= max:
        return False
        
    return (validate_bst(current.left, min, current.data)) and (validate_bst(current.right, current.data, max))   

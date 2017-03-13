"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

# Floyd's method
# Other technique may include hashing
def has_cycle(head):
    ptr_a = ptr_b = head
    while ptr_a and ptr_b and ptr_a.next:
        if ptr_a == ptr_b:
            return True
        else:
            ptr_a = ptr_a.next
            ptr_b = ptr_b.next.next
        
    return False
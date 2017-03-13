"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def MergeLists(headA, headB):
    currentA = headA
    currentB = headB
    head = None
    currentm = None
    if (currentA and not currentB) or (currentA and currentB and currentA.data < currentB.data):
        head = Node(currentA.data)
        currentA = currentA.next
        currentm = head
    elif (currentB and not currentA) or (currentA and currentB and currentA.data > currentB.data):
        head = Node(currentB.data)
        currentB = currentB.next
        currentm = head
    while currentA or currentB:
        if currentA and currentB:
            if currentA.data < currentB.data:
                currentm.next = Node(currentA.data)
                currentA = currentA.next
                currentm = currentm.next
            else:
                currentm.next = Node(currentB.data)
                currentB = currentB.next
                currentm = currentm.next
        elif currentA and not currentB:
            currentm.next = Node(currentA.data)
            currentA = currentA.next
        else:
            currentm.next = Node(currentB.data)
            currentB = currentB.next
    return head

# Better Solution
def MergeLists(NodeA, NodeB):
    if NodeA == None:
        return NodeB
    elif NodeB == None:
        return NodeA
    elif NodeA.data < NodeB.data:
        return Node(NodeA.data, MergeLists(NodeA.next, NodeB))
    else:
        return Node(NodeB.data, MergeLists(NodeA, NodeB.next))   
            
            
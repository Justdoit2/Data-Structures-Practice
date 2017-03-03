"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
    holder = []
    while headA is not None:
        holder.append(headA.data)
        headA=headA.next
    while headB is not None:
        if headB.data in holder:
            return headB.data
        headB=headB.next
    return 0;
        
  

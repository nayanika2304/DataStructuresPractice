class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

class doubly_linked_list:

   def __init__(self):
      self.head = None

# Adding data elements on top of another if exists
   '''
   if head is none, make head the new node
   if not make the prev of existing head point to the new Node
   and then make new node as head
   '''
   def push(self, NewVal):
      NewNode = Node(NewVal)
      NewNode.next = self.head
      if self.head is not None:
         self.head.prev = NewNode
      self.head = NewNode

# Print the Doubly Linked list
   def listprint(self, node):
      while (node is not None):
         print(node.data)
         node = node.next

dllist = doubly_linked_list()
dllist.push(12)
#dllist.push(8)
dllist.push(62)
dllist.listprint(dllist.head)
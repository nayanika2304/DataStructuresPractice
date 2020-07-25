class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
    '''
    check the node with root node or make the node as root node
    if node is less check if left is none
    if none left = node
    else insert on left
    if node is greater check if right is none
    if none right = none 
    else insert on right
    '''
    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.PrintTree()
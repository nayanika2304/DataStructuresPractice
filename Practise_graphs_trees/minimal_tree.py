'''
Given a sorted (increasing order) array with unique integer elements, write an algorithm
to create a binary search tree with minimal height.

To create a tree of minimal height,
we need to match the number of nodes in the left subtree
to the number of nodes in the right subtree as much as possible.
This means that we want the root to be the middle of the array,
since this would mean that half the elements would be less than the root
and half would be greater than it.

'''


# Python code to convert a sorted array
# to a balanced Binary Search Tree
import math
# binary tree node
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


# function to convert sorted array to a
# balanced BST
# input : sorted array of integers
# output: root node of balanced BST
def sortedArrayToBST(arr):
    if not arr:
        return None

    # find middle
    mid = math.floor((len(arr)) / 2)
    print(mid)
    # make the middle element the root
    root = Node(arr[mid])

    # left subtree of root has all
    # values <arr[mid]
    root.left = sortedArrayToBST(arr[:mid])

    # right subtree of root has all
    # values >arr[mid]
    root.right = sortedArrayToBST(arr[mid + 1:])
    return root


# A utility function to print the preorder
# traversal of the BST
def preOrder(node):
    if not node:
        return

    print(node.data),
    preOrder(node.left)
    preOrder(node.right)


# driver program to test above function
""" 
Constructed balanced BST is  
    4 
/ \ 
2 6 
/ \ / \ 
1 3 5 7 
"""

arr = [1, 2, 3, 4, 5, 6, 7]
root = sortedArrayToBST(arr)
print
"PreOrder Traversal of constructed BST ",
preOrder(root)

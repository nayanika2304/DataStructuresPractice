# Python3 program to partition a
# linked list around a given value.
import math

'''
Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. lf x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.

faster approach is to keep adding to head or tail based on small or greater
'''
# Link list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# A utility function to create a new node
def newNode(data):
    new_node = Node(data)
    new_node.data = data
    new_node.next = None
    return new_node


# Function to make a new list
# (using the existing nodes)
# and return head of new list.
def partition(head, x):
    # Let us initialize start and
    # tail nodes of new list
    tail = head

    # Now iterate original list
    # and connect nodes
    curr = head
    while (curr != None):
        next = curr.next
        if (curr.data < x):
            # Insert node at head.

            curr.next = head
            head = curr
        else:
            # Append to the list of greater values
            # Insert node at tail.
            tail.next = curr
            tail = curr
        curr = next
    tail.next = None

    # The head has changed, so we need
    # to return it to the user.
    return head


# Function to print linked list
def printList(head):
    temp = head
    while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next


# Driver Code
if __name__ == '__main__':
    # Start with the empty list
    head = newNode(3)
    head.next = newNode(5)
    head.next.next = newNode(8)
    head.next.next.next = newNode(2)
    head.next.next.next.next = newNode(10)
    head.next.next.next.next.next = newNode(2)
    head.next.next.next.next.next.next = newNode(1)

    printList(head)
    print('\n')
    x = 5
    head = partition(head, x)
    printList(head)
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def sum_two_lists(self,llist):
        p = self.head
        q = llist.head

        sum_list = LinkedList()
        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            if s >=10:
                carry = 1
                remainder = s % 10
                sum_list.append(remainder)
            else:
                carry = 0
                sum_list.append(s)

            if p is not None:
                 p = p.next
            if q is not None:
                q = q.next
        sum_list.printList()

first = LinkedList()
second = LinkedList()

# Create first list
first.append(7)
first.append(1)
first.append(6)
print("First List is ")
first.printList()

# Create second list
second.append(5)
second.append(9)
second.append(2)
print("\nSecond List is ")
second.printList()
print("sum",617+295)
first.sum_two_lists(second)
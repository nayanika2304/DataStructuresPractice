'''
Write code to remove duplicates from an unsorted linked list.
(in this case,setting each element in the hash table and
if a duplicate occurs, move the pointer)

How would you solve this problem if a temporary buffer is not allowed?
(using a runner for subsequent node and a current from head)
'''


def deleteDuplicates(head):
    current = head
    while current:
        runner = current
        while runner.next:
            if(runner.next.data == current.data):
                runner.next = runner.runner.next
            else:
                runner = runner.next
            current = current.next
    return head

'''
Given a circular linked list,
implement an algorithm that returns the node at the
beginning of the loop.

1->2->3->4->None

1->2->3->4
   \_____/


1->2->3->4->5->6->7->8->3
the loop is of length c
the beginning is 3
and both fast and slow pointers meet at 7
so 1->3
7->3
4->2
slow`s path = 1->3 + 3->7 + x*C(number of iterations * loop length C)
fast`s path = 2(1->3 + 3->7 + y*C(number of iterations * loop length C))
1->3 + 3->7 + y*C = 1->3 + 3->7 + x*C + 1->3 + 3->7 + x*C
(y-2x) * C = 1->3 + 3->7
3-> 7 = C - 7->3 so
1 -> 3 = N*C + 7->3

https://www.youtube.com/watch?v=iZVBVCpmugI
'''

class Solution(object):
    slow = head
    fast = slow

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            while slow != head:
                slow = slow.next
                head = head.next
            #return slow
    #return None
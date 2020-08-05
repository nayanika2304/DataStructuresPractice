'''
Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.

1) find the length and tails of both linked list
2) if tails are different, return false
3) set two pointers on each linked list
4) on the longer linked list, advance the pointer by diff in length once
5) traverse  on each until pointers are same
'''

class ListNode:
    def __init__(self,data,next= None):
        self.data = None
        self.next = next


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        curA, curB = headA, headB
        lenA, lenB = 0, 0
        while curA is not None:
            lenA += 1
            curA = curA.next
        while curB is not None:
            lenB += 1
            curB = curB.next
        curA, curB = headA, headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                curA = curA.next
        elif lenB > lenA:
            for i in range(lenB - lenA):
                curB = curB.next
        while curB != curA:
            curB = curB.next
            curA = curA.next
        return curA
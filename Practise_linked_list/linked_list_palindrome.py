# Data Structure to store a linked list node

'''
reversing a linked list is not the best approach as it may take more space

here the idea is recursion
'''
class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next


# Recursive function to check if linked list is palindrome or not
def checkPalindrome(left, right):

        # base case
        if right is None:
            return True, left
    
        val, left = checkPalindrome(left, right.next)

        result = val and (left.data == right.data)
        left = left.next

        return result, left


# Function to check if linked list is palindrome or not
def checkPalin(head):
	return checkPalindrome(head, head)[0]


if __name__ == '__main__':

	# input keys
	keys = [1, 3, 5, 3, 1]

	head = None
	for i in reversed(range(len(keys))):
		head = Node(keys[i], head)

	if checkPalin(head):
		print("Linked list is Palindrome")
	else:
		print("Linked list is not Palindrome")


# class Solution:
#     def isPalindrome(self,head:Node):
#         if head is None:
#             return True
#         slow,fast = head, head
#         stk = []
#
#         while fast and fast.next!= None:
#             stk.append(slow.data)
#
#             slow = slow.next
#             fast = fast.next.next
#
#         if fast: # in case of odd numbers
#             slow = slow.next
#         while(slow and len(stk)):
#             if stk.pop() != slow.data:
#                 return False
#             slow = slow.next
#         return True

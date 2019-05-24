# https://leetcode.com/problems/reverse-linked-list/submissions/
# Runtime: 40 ms, faster than 92.28% of Python3 online submissions for Reverse Linked List.

#iterative, traverses the list and change the current nodes next pointer to the previous element. 
# keep track of previous node before hand since the node doesn't keep this reference

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        current = head
        
        while current:
            previous, current.next, current = current, previous, current.next
        return previous
# https://leetcode.com/problems/remove-linked-list-elements/submissions/
# Runtime: 76 ms, faster than 86.12% of Python3 online submissions for Remove Linked List Elements.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        previous = dummy
        current = previous.next
        while current:
            if current.val == val:
                previous.next = current.next
            else:
                previous = previous.next
            current = current.next
        return dummy.next
"""61. Rotate List

https://leetcode.com/problems/rotate-list/

edge cases
----------
singleton
2 elements
the first element needs to be removed
rotation once
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        n = len_of_linkedlist(head)
        k = k % n
        if k == 0:
            return head
        # get to n-k-1 position 
        fast = head
        for _ in range(n-k-1):
            fast = fast.next
        new_head = fast.next
        fast.next = None
        # get the last element of the linkedlist
        last = new_head
        while last.next is not None:
            last = last.next
        last.next = head
        return new_head


def len_of_linkedlist(head):
    n = 0
    while head:
        n += 1
        head = head.next
    return n

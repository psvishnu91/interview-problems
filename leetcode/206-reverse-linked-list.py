"""206. Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

Solution:
---------
3 pointers, lt, rt, rt_nxt
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return _reverse_list(head)


def _reverse_list(head):
    if not (head and head.next):
        return head
    lt, rt = head, head.next
    # Gotcha, first node needs to point to None
    lt.next = None
    while rt is not None:
        rt_nxt = rt.next
        rt.next = lt
        lt = rt
        rt = rt_nxt
    return lt

"""21. Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

Create sentinel head
The idea would to have 2 runners one on
left, one on right and one cur=sentinel

1 - 2 - 4 - N
        l
1 - 3 - N
        r

s - 1 - 1 - 2 - 3 - N
                c

Edge cases
----------
Both empty
One empty
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sentinel = ListNode()
        cur = sentinel
        lt, rt = list1, list2
        while lt is not None and rt is not None:
            if lt.val <= rt.val:
                cur.next = lt
                lt = lt.next
            else:
                cur.next = rt
                rt = rt.next
            cur = cur.next
        if lt is not None:
            cur.next = lt
        if rt is not None:
            cur.next = rt
        return sentinel.next

"""82. Remove Duplicates from Sorted List II

https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii


# Tests
# Nominal case
1 2 3 3 4 4
0 1 2 3 4 5

fake_head =None
fake_head.next = 0

[1,2,4]

prev cur cur.next prev.val cur.val cur.next.val
================================================
-1   0     1        None       1        2
 0   1     2        1          2        3
 1   2     3        2          3        3
 1   3     4        2          3        4
 1   4     5        2          4        4
 1   5     None     2          4        -


# Edge case
[done] None
[done] Unit array
[1] prev=N(None, 1), cur = 1, cur.next=None
[done] Two len array: [done]
[1,2], prev=N(None,0), cur=(1,1), cur.next=(2,None)

[done] all duplicates
[1,1,1]
prev=N(N,0), cur=(1,1), cur.next=(1,2)
cur=(1,2),cur.next=(1,None)
cur=(1,None),cur.next=None

[done] no duplicates
[done] duplicates at beg
[done] duplicates at end
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake_head = ListNode(val=None)
        fake_head.next = head
        # invariant up to prev we are good
        prev = fake_head
        cur = head
        while cur and cur.next:
            if cur.val != cur.next.val:
                prev = cur
                cur = cur.next
            else:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next
                prev.next = cur
        return fake_head.next

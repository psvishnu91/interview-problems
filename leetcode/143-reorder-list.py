"""143. Reorder List

https://leetcode.com/problems/reorder-list/

Idea
-----
Pass in the head and right in a recursion
we keep moving right in recusion until right.next is None

At this phase we set left=head, and then do lt->rt->lt_next 
and we return lt_next up the recursion stack where it will
become the new lt (instead of the head), rt is the penultimate
element and we add lt_next.next to this rt and continue.

Termination condition is if at any lt_next = rt (odd list) or
rt.next = lt_next
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        thread_rec(head=head, rt=head)

def thread_rec(head, rt):
    """Tests

    1-2-3-4-5
    lt head rt  lt_nxt
    ===================
    N   1   1      
    N   1   2
    3   1   3       1-5->2->4->3-> None
    2   1   4     3 1-5->2->4->3
        1   5     2 1->5->2


    1-2-3-4
    lt head rt  lt_nxt
    ===================
    N   1   1      
    N   1   2
    2   1   3    3    1-5->2->3->None
        1   4     2 1-4->2

    """
    if rt.next is not None:
        lt = thread_rec(head=head, rt=rt.next)
    else:
        lt = head
    if lt is None:
        return None
    elif lt == rt:
        lt.next = None
        return None
    lt_next = lt.next
    lt.next = rt
    if lt_next != rt:
        rt.next = lt_next
        return lt_next
    else:
        rt.next = None
        return None

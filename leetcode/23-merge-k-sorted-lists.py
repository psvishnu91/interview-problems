"""23. Merge k Sorted Lists

https://leetcode.com/problems/merge-k-sorted-lists/

Brute force T- O(k^2*n), k num lists, max nodes per list
-----------
- Create a cur = sentinel node as the root node
- we iterate over each node in the k lists, find the smallest
- add that as the next to the cur.next, move cur=cur.next
- iterate over all the k nodes again,


Heap sort T-O(nk logk) S-O(k)
----------
Add the first element of each list into a heap[(val, Node)].
Pop from the heap and add the next node in the list to the heap
The size of the heap is always at most k, to add all the first 
elements it O(k) because heapify is O(k). And then for each of the
nk numbers we do o(logk) operation by popping and adding (T-O(nklogk))
"""
import heapq
import dataclasses
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

@dataclasses.dataclass
class HeapItem:

    val: int
    node: 'ListNode'

    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        1->4->5
        1->3->4
        2->6

        s->1->1->2->4->4

        cur hp
        -------
        s   [(1, 1->4),(1, 1->3),(2, 2-6)]
        1->4 [(1, 1->3),(2, 2-6), (4,4->5)]
        1->3 [(2, 2-6), (4,4->5), (4, 4->N)]
        2->6 [(4,4->5), (4, 4->N), (6, 6->N)]

        """
        head = cur = ListNode(val=None)
        # Add all the first nodes of the linkedlists
        heap = []
        for ll_node in lists:
            if ll_node is None:
                continue
            heap.append(HeapItem(val=ll_node.val, node=ll_node))
        heapq.heapify(heap)
        while heap:
            node = heapq.heappop(heap).node
            if node.next:
                nxt = node.next
                heapq.heappush(heap, HeapItem(val=nxt.val, node=nxt))
            cur.next = node
            cur = node
        return head.next       

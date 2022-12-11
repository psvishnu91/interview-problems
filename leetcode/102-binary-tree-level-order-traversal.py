"""102. Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/

Solution 1: BFS
--------------
- We keep track of the level we are at.
- We begin at the root level = 0
- Keep track of cur_level = 0
- First add (0,root) to queue
- Pop from front
    if level is same add it to level_list
    if level has changed add level_list to output and update cur_level

Solution 2: BFS [invalid]
-------------------------
- Every time length of queue is a power of 2 add it to output
only works for balanced/complete binary tree

Edge cases
----------
empty node

Test
----
        3
    /       \
    9        20
            /   \
           15   7

lvl node cur_lvl     lvl_list    q              output 
--------------------------------------------------------
           0          []        [(0,3)]          []
0    3     0         [3]      [(1,9), (1,20)]
1    9     0->1      [9]      [(1,20),(2,N),(2,N)]            [[3]]
1    20    1         [9,20]    [(2,N),(2,N),(2,15),(2,7)]
2    N     1
2    N     1                    [(2,15),(2,7)]
2    15    1        [15]          [(2,7)]                 [[3], [9,20]]

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return level_order(root)


def level_order(root) -> list[list[int]]:
    if root is None:
        return []
    output = []
    lvl_list = []
    cur_lvl = 0
    q = deque([(0, root)])
    while q:
        lvl, node = q.popleft()
        if not node:
            continue
        qvals = [(l,n.val) if n else None for l,n in q ]
        if lvl == cur_lvl:
            lvl_list.append(node.val)
        else:
            output.append(lvl_list)
            lvl_list = [node.val]
            cur_lvl = lvl
        q.extend([(lvl+1, node.left), (lvl+1, node.right)])
        qvals = [(l,n.val) if n else None for l,n in q ]
    if lvl_list:
        output.append(lvl_list)
    return output




"""103. Binary Tree Zigzag Level Order Traversal

https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque([root])
        dirn_fns = itertools.cycle(
            [lambda x: x, lambda x: list(reversed(x))]
        )
        lvl_order = []
        while q:
            qlen = len(q)
            row = []
            for _ in range(qlen):
                n = q.popleft()
                row.append(n.val)
                if n.left is not None:
                    q.append(n.left)
                if n.right is not None:
                    q.append(n.right)
            lvl_order.append(next(dirn_fns)(row))
        return lvl_order

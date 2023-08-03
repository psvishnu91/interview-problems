"""230. Kth Smallest Element in a BST

https://leetcode.com/problems/kth-smallest-element-in-a-bst/editorial/

Key Idea:
Recurse to the left and get the size. If left.size + 1 == k, you are the node.
Recurse to the right with **k - ()left.size + 1)**.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from dataclasses import dataclass


@dataclass
class Result:
    size: int
    found: Optional[int]


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return dfs(node=root, k=k).found


def dfs(node, k) -> None:
    """
    k=4
            5
        /           \
        3           6
  (2,N)/ \
      2   4
     /(1,N)
    1 l,r=0,N
    """
    if node is None:
        return Result(size=0, found=None)
    lt_res = dfs(node=node.left, k=k)
    if lt_res.found is not None:
        # Left has the answer
        return lt_res
    elif lt_res.size + 1 == k:
        # I am the answer
        return Result(size=None, found=node.val)
    else:
        rt_res = dfs(node.right, k=k - (lt_res.size + 1))
        if rt_res.found is not None:
            # Right has the answer
            return rt_res
        else:
            # Answer is not in this subtree
            return Result(size=1 + lt_res.size + rt_res.size, found=None)

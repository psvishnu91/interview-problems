"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""

from typing import Optional

import dataclasses as DC

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


@DC.dataclass(frozen=True)
class Result:
    # Max value of any path under this node
    max_path: int
    # Max path that goes through this node
    max_through_path: int


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return max_path_sum(node=root).max_path


def max_path_sum(node: Optional[TreeNode]) -> Result:
    if node is None:
        # Set max path at None to large negative value
        return Result(max_through_path=0, max_path=-1_000_000)
    lt_rec = max_path_sum(node=node.left)
    rt_rec = max_path_sum(node=node.right)
    max_through_path = (
        node.val
        # zero is to indicate we are simply beginning at this node
        # we can also have a single node path
        + max(0, lt_rec.max_through_path, rt_rec.max_through_path)
    )
    return Result(
        max_through_path=max_through_path,
        max_path=max(
            max_through_path,
            node.val + lt_rec.max_through_path + rt_rec.max_through_path,
            lt_rec.max_path,
            rt_rec.max_path,
        ),
    )

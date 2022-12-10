"""
https://leetcode.com/problems/diameter-of-binary-tree/solution/
"""
import dataclasses as DC
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


@DC.dataclass(frozen=True)
class Result:
    # Max diameter bubbled up.
    max_dm: int
    max_depth: int


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return _dm_of_bt_recusion(root=root)


def _dm_of_bt_recusion(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return _dm_of_bt_helper(root).max_dm


def _dm_of_bt_helper(node: TreeNode) -> Result:
    if node is None:
        return Result(max_dm=-1, max_depth=-1)
    lt_rec = _dm_of_bt_helper(node.left)
    rt_rec = _dm_of_bt_helper(node.right)
    return Result(
        max_depth=(1 + max(lt_rec.max_depth, rt_rec.max_depth)),
        max_dm=max(
            (2 + lt_rec.max_depth + rt_rec.max_depth),
            lt_rec.max_dm,
            rt_rec.max_dm,
        ),
    )

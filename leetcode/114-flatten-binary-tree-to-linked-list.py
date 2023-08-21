"""114. Flatten Binary Tree to Linked List

https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import dataclasses


@dataclasses.dataclass
class RecRes:
    node: Optional['TreeNode']
    rightmost: Optional['TreeNode']


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        flat_rec(root)
    
    
def flat_rec(root) -> Optional[RecRes]:
    """
    rightmost child is itself when it has no right child, if it has a
    rightchild, it's what the rightchild returns

    lt child is none
    rt child is none
    neither child is none
    both are none
                1
            /       \
            2       6
        /
        1
    /       \
    3       4

    """
    if not root:
        return None
    lt_res = flat_rec(root=root.left)
    rt_res = flat_rec(root.right)
    root.left = None
    if lt_res is not None and rt_res is not None:
        root.right = lt_res.node
        lt_res.rightmost.right = rt_res.node
        rightmost = rt_res.rightmost
    elif lt_res is None and rt_res is not None:
        root.right = rt_res.node
        rightmost = rt_res.rightmost
    elif lt_res is not None and rt_res is None:
        root.right = lt_res.node
        rightmost = lt_res.rightmost
    else:
        # lt_res is None and rt_res is None:
        root.right = None
        rightmost = root
    return RecRes(node=root, rightmost=rightmost)
    

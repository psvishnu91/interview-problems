"""101. Symmetric Tree

https://leetcode.com/problems/symmetric-tree/

Algorithm
---------
Run match trees recursion, where we compare the values of the
leftsubtree with the right subtree.

    n1.left with n2.right
    n1.right with n2.left

In the example below, we want to compare the left subtree of 2
rooted at 3, with the 2 subTree of the right 2 rooted at 3.

            1
        /       \
        2       2
    /   \       /   \
    3   4       4   3
/   \               /   \
0   -1              -1  0
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return match_trees(n1=root.left, n2=root.right)

def match_trees(n1, n2):
    if n1 is None and n2 is None:
        return True
    elif n1 is None or n2 is None:
        return False
    return (
        n1.val == n2.val
        and match_trees(n1.left, n2.right)
        and match_trees(n1.right, n2.left)
    )

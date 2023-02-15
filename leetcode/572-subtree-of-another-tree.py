# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            return False
        return (
            is_match(root_1=root, root_2=subRoot)
            or self.isSubtree(root=root.left, subRoot=subRoot)
            or self.isSubtree(root=root.right, subRoot=subRoot)
        )

def is_match(root_1, root_2):
    # either both should be none or neither
    if root_1 is None and root_2 is None:
        return True
    elif root_1 is None or root_2 is None:
        return False
    return (
        root_1.val == root_2.val
        and is_match(root_1=root_1.left, root_2=root_2.left)
        and is_match(root_1=root_1.right, root_2=root_2.right)
    )

"""98. Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

Logic
Recurse left and right. Keep track of is_valid, min_val, max_val.
Handle null node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import dataclasses

@dataclasses.dataclass
class RecResult:
    valid: bool
    min_val: Union[int, float] = float('inf')
    max_val: Union[int, float] = -float('inf')


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return is_valid_bst_rec(node=root).valid
    

def is_valid_bst_rec(node):
    """
                        5
                /                       \
                2                           8    
            /       \                    /      \      
            1       3                    6       9
        (T,i,-i)   (T,i,-i)            /   \
                                       4     7
    """
    if node is None:
        return RecResult(valid=True)
    lt_res = is_valid_bst_rec(node=node.left)
    if not lt_res.valid or lt_res.max_val >= node.val:
        return RecResult(valid=False)
    rt_res = is_valid_bst_rec(node=node.right)
    if not rt_res.valid or rt_res.min_val <= node.val:
        return RecResult(valid=False)
    return RecResult(
        valid=True,
        min_val=min(lt_res.min_val, node.val),
        max_val=max(rt_res.max_val, node.val),
    )

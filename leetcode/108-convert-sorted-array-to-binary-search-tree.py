"""108. Convert Sorted Array to Binary Search Tree

https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

Solution Recursion:
- let's think of odd lengths
n//2 -> n=5, mid=2
n//2 -> n=6, mid=3

[0,1,2,3,4,5,6,7,8]


                4
            /       \
           1        6
        /   \       /    \
        0   2      5     7
            \             \
             3            8

Things to consider
=================
even and odd lengths
empty array
one node
duplicates
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return sorted_to_bst(nums=nums)


def sorted_to_bst(nums)  -> Optional[TreeNode]:
    return sorted_to_bst_helper(nums, lt=0, rt=len(nums)-1)


def sorted_to_bst_helper(nums, lt, rt)  -> Optional[TreeNode]:
    if rt < lt:
        # handles 0-len arrays as well
        return None
    mid = (lt+rt)//2
    return TreeNode(
        val=nums[mid],
        left=sorted_to_bst_helper(nums, lt=lt, rt=mid-1),
        right=sorted_to_bst_helper(nums, lt=mid+1, rt=rt),
    )

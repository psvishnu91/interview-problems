"""112. Path Sum

https://leetcode.com/problems/path-sum/

Two solns: recursion or do recursion w a stack
T - O(n) each node is visited once
S - Worst case O(n) (unbalanced tree -> linkedlist) and best case O(log n)
    fully balanced
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return iterative(node=root, target=targetSum)  # or dfs(root, targetSum)


def dfs(node, target):
    if not node:
        return False
    rem = target - node.val
    if rem == 0 and node.left is None and node.right is None:
        return True
    return (
        dfs(node=node.left, target=rem)
        or dfs(node=node.right, target=rem)
    )

def iterative(node, target):
    stk = [(node, target)]
    while stk:
        n, tgt = stk.pop()
        rem = tgt - n.val
        if rem == 0 and n.left is None and n.right is None:
            return True
        for child in [n.left, n.right]:
            if child is None:
                continue
            stk.append([child, rem])
    else:
        return False

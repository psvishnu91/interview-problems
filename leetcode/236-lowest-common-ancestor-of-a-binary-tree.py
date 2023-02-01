"""236. Lowest Common Ancestor of a Binary Tree

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Possibilities

Not found
---------
- i am not the node and no descendants

I am the parent
---------------
- one node is on the left and i am the other node 
- one node is on the right and i am the other ndoe
- one node is on the left and one is on the right

I have one descendant
---------------------
- i am the node but no child nodes
- only my left has a node
- only my right has a node

If there is a parent downstream, i need to bubble it up
def rec(node):
    if node is None:
        return Result(p_found=False, q_found=False, lca=None) # default
    lt_result = rec(node.left)
    if lt_result.lca is not None:
        return Result(p_found=True, q_found=True, lca=lt_result.lca)
    rt_result = rec(node.right)
    if rt_result.lca is not None:
        return Result(p_found=True, q_found=True, lca=rt_result.lca)
    # i am parent
    p_found = node.val == p.val or lt_result.p_found or rt_result.p_found:
    q_found = node.val == q.val or lt_result.q_found or rt_result.q_found:
    Result(
        p_found=p_found,
        q_found=q_found,
        # if not none simply return
        lca=node if p_found and q_found else None,
    )
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import dataclasses


@dataclasses.dataclass
class Result:
    p_found: bool
    q_found: bool
    lca: Optional['TreeNode']


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return lca_rec(node=root, p=p, q=q).lca


def lca_rec(node, p, q):
    if node is None:
        return Result(p_found=False, q_found=False, lca=None) # default
    lt_result = lca_rec(node=node.left, p=p, q=q)
    if lt_result.lca is not None:
        return Result(p_found=True, q_found=True, lca=lt_result.lca)
    rt_result = lca_rec(node=node.right, p=p, q=q)
    if rt_result.lca is not None:
        return Result(p_found=True, q_found=True, lca=rt_result.lca)
    p_found = node.val == p.val or lt_result.p_found or rt_result.p_found
    q_found = node.val == q.val or lt_result.q_found or rt_result.q_found
    return Result(
        p_found=p_found,
        q_found=q_found,
        # if i am parent
        lca=node if p_found and q_found else None,
    )

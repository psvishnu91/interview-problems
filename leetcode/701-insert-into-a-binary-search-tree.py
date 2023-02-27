"""701. Insert into a Binary Search Tree

https://leetcode.com/problems/insert-into-a-binary-search-tree/

SOLUTION
========
T - O((log n)^2)

Invariant we want to maintain is that all the elements to the
left are smaller than the new_node=Node(val) and all the elements
to right are greater.

Invariant
        largest val on left < val < smallest val on right
        (None=-∞)                      (None=∞)

If largest val on left > val: recurse left (you want the larger number on the rt of val)
If smallest val on right < val: recurse right (you want the smaller to be on the lt of val)

When the invariant is met
if new_node.val > root.val put the root on the left and set root's right to the new_node's right
if new_node.val < root.val put the root on the right and move root's left to the new_node's left

We also have to pass the parent so that the parent's left or right where root belongs gets
set to the new_node.

Optimisation
------------
At every node we need to the largest on left and smallest on right. We cache this in two
dicts so that we don't search repeatedly.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#   

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return insert_bst(root=root, val=val)

def insert_bst(root, val):
    if not root:
        return TreeNode(val)
    return insert_bst_rec(parent=None, root=root, val=val, lt_cache={}, rt_cache={})

def insert_bst_rec(parent, root, val, lt_cache, rt_cache):
    if root.val in lt_cache:
        largest_on_lt = lt_cache[root.val]
    else:
        largest_on_lt = lt_cache[root.val] = find_largest(root.left)
    if root.val in rt_cache:
        smallest_on_rt = rt_cache[root.val]
    else:
        smallest_on_rt = rt_cache[root.val] = find_smallest(root.right)
    if largest_on_lt < val < smallest_on_rt:
        new_node = TreeNode(val)
        if val > root.val:
            new_node.left = root
            new_node.right = root.right
            root.right = None
        elif val < root.val:
            new_node.right = root
            new_node.left = root.left
            root.left = None
        else:
            raise ValueError("Not unique")
        if parent:
            if parent.val > val:
                parent.left = new_node
            else:
                parent.right = new_node
        return new_node
    elif largest_on_lt > val:
        insert_bst_rec(parent=root, root=root.left, val=val, lt_cache=lt_cache, rt_cache=rt_cache)
        return root
    else:
        # smallest_on_rt < val
        insert_bst_rec(parent=root, root=root.right, val=val, lt_cache=lt_cache, rt_cache=rt_cache)
        return root

def find_largest(root):
    if not root:
        return -float("inf")
    if root.right is None:
        return root.val
    else:
        return find_largest(root=root.right)

def find_smallest(root):
    if not root:
        return float("inf")
    if root.left is None:
        return root.val
    else:
        return find_smallest(root.left)

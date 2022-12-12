"""105. Construct Binary Tree from Preorder and Inorder Traversal

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Problem reasoning
-----------------
Something to notice is that for the inorder traversal all elements
left of the array mid node will be the left half of it's tree and
all elements to the right will be the right half.

The preorder[0] will have the root.

- we take preorder[0] -> Create root node
pre_ix=0, in_lt=0, in_rt=inorder.index(preorder[0])-1 (0)

- assign left child to recursion on left, with in_lt and in_rt
and preorder[1]
- assign right child -> recurse right, in_lt=2, in_rt=n-1=4, preorder[2]
    create root node with index of right

Cases 1
    1
     \
     2
     \ 
     3
     \
     4

preorder = [1,2,3,4]
inorder = [1,2,3,4]

Cases 2
    1
    /
    2
    /
    3
    /
    4
preorder = [1,2,3,4]
inorder = [4,3,2,1]

                inl=0,inr=3,prix=0,inix=3
                N(1,lt=,rt=None)
                /                         \
inl=0,inr=2,prix=1,inix=2                  inl=4,inr=3 
         N(2,lt=,rt)
            /        \
                    l=3,r=2

Cases 3
                        3
                    /          \
                   9            20
                                /    \    
                            15        7

    preorder = [3,9,20,15,7]
     inorder = [9,3,15,20,7]

                           v=3,pix=0,inl=0,inr=4,inix=1
                            N(3, lt=9, rt=),pix
                            /                                  \
           v=9,pix=1,inl=0,inr=0,inix=0                     pix=2,
                 N(9, lt=None, rt=N),pix=2
                    /               \
            pix=2,inl=0,inr=-1      pix=2,inl=1,inr
Algorithm
--------
pre_ix = 0
in_lt = 0, in_rt= n-1 (3)

if in_lt > in_rt:
    return pix, None
in_ix = inorder.index(po[pre_ix]) [build a hashmap of val to index for optimisation]

return  Node(
    val=po[pre_ix],
    lt=rec(pre_ix+1, in_lt=in_lt, in_rt=in_ix-1),
    rt=rec(pre_ix+1, in_lt=in_ix+1, in_rt=in_rt),
)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return build_tree(preorder=preorder, inorder=inorder)


def build_tree(preorder, inorder) ->  Optional[TreeNode]:
    if not preorder:
        return None
    # unique values given
    inorder_ix_map = {n: i for i, n in enumerate(inorder)}
    return build_tree_rec(
        preorder, pre_ix=0, in_lt=0, in_rt=len(preorder)-1,
        inorder_ix_map=inorder_ix_map,
    )[1]


def build_tree_rec(
    preorder, pre_ix, in_lt, in_rt,
    inorder_ix_map,
) -> Tuple[int, Optional[TreeNode]]:
    if in_lt > in_rt:
        return (pre_ix, None)
    nval = preorder[pre_ix]
    in_ix = inorder_ix_map[nval]
    after_lt_pre_ix, lt_node = build_tree_rec(
        preorder=preorder,
        pre_ix=pre_ix+1,
        in_lt=in_lt,
        in_rt=in_ix-1,
        inorder_ix_map=inorder_ix_map,
    )
    after_rt_pre_ix, rt_node = build_tree_rec(
        preorder=preorder,
        pre_ix=after_lt_pre_ix,
        in_lt=in_ix+1,
        in_rt=in_rt,
        inorder_ix_map=inorder_ix_map,
    )
    return (
        after_rt_pre_ix,
        TreeNode(val=nval, left=lt_node, right=rt_node)
    )

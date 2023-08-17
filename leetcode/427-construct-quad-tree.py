"""427. Construct Quad Tree

https://leetcode.com/problems/construct-quad-tree/

Simple Algo:
3 functions
1. split_rec(grid, top_lt, bot_rt) -> recursion_wrapper
    2. _is_same(grid, top_lt, bot_rt)
    3. _iter_quads(grid, top_lt, bot_rt) -> split into quads and yield
2. Check if whole grid is same, if so, done return leaf node
    if not iterate over each quad, if all same create leaf node, if not
    recurse. Then assign to each of the child nodes, done.

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return _construct(grid)

def _construct(grid):
    n = len(grid)
    return split_rec(
        grid=grid,
        tl=(0,0),
        br=(n-1,n-1),
    )

def split_rec(grid, tl, br) -> 'Node':
    if _is_same(grid=grid, tl=tl, br=br):
        i_tl, j_tl = tl
        return Node(
            val=bool(grid[i_tl][j_tl]),
            isLeaf=True,
            topLeft=None,
            topRight=None,
            bottomLeft=None,
            bottomRight=None,
        )
    loc2node = {}
    for nloc, qtl, qbr in _iter_quads(tl, br):
        if _is_same(tl=qtl, br=qbr, grid=grid):
            _i, _j = qtl
            loc2node[nloc] = Node(
                val=bool(grid[_i][_j]),
                isLeaf=True,
                topLeft=None,
                topRight=None,
                bottomLeft=None,
                bottomRight=None,
            )
        else:
            loc2node[nloc] = split_rec(tl=qtl, br=qbr, grid=grid)
    return Node(
        val=True,
        isLeaf=False,
        topLeft=loc2node["tl"],
        topRight=loc2node["tr"],
        bottomLeft=loc2node["bl"],
        bottomRight=loc2node["br"],
    )

def _is_same(grid, tl, br):
    i_tl, j_tl = tl
    i_br, j_br = br
    val = grid[i_tl][j_tl]
    for i, j in itertools.product(range(i_tl, i_br+1), range(j_tl, j_br+1)):
        if grid[i][j] != val:
            return False
    else:
        return True


def _iter_quads(tl, br):
    i_tl, j_tl = tl
    i_br, j_br = br
    i_mid, j_mid = (i_tl + i_br)//2, (j_tl + j_br)//2
    yield "tl", (i_tl, j_tl), (i_mid, j_mid)  # top lt
    yield "tr", (i_tl, j_mid+1), (i_mid, j_br)  # top rt
    yield "bl", (i_mid+1, j_tl), (i_br, j_mid)  # bot lt
    yield "br", (i_mid+1, j_mid+1), (i_br, j_br)  # bot rt

"""1289. Minimum Falling Path Sum II

https://leetcode.com/problems/minimum-falling-path-sum-ii/

[Time limit exceeded] Solution 1: DP T - O(N^3) 
=================================================
In recursive solution we look at what is the minimum value if
I pick this row and col and proceed down. In bottoms up solution
we compute what is the path with the minimum distance to get here.

Bottomsup (same idea for recursion)
-----------------------------------
This is O(N^3) because for each element we need to find the min
value to reach every col in the previous besides this column.
We touch each element in grid once, ie., O(N^2) elements and for
each element we do O(N) operation.

[Accepted] Solution 2: DP+Heap T - O(N^2 log N) 
===================================================
For every element grid[(row, col)]
All we need to know is the smallest path in the prev row
(row-1) and the next smallest path in the last row if the
smallest path happens to in the column right above us ie.,
(row-1, col). We address this with a heap. We simply insert
each path length into a heap_cur. When we compute distance to
grid[row, col], we do
if heap_pr.peek() != path[row-1, col]:
    path[row, col] =  heap_pr.peek() + grid[row, col]
else:
    mv_pr = heap_pr.pop()
    path[row, col] = heap_pr.peek() + grid[row, col]
    heap_pr.push(mv_pr)
"""
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        return _min_path_botup(grid)

#######################################################################
# Solution 2: Bottom up DP + Heap
# 
# Accepted
#######################################################################

def _min_path_botup(grid):
    nrows, ncols = len(grid), len(grid[0])
    mv_cache = [[None]*ncols for _ in range(nrows)]
    heap_pr = None
    for r in range(nrows):
        heap_cur = []
        for c in range(ncols):
            cell = grid[r][c]
            if r == 0:
                cur_path = cell
            else:
                if mv_cache[r-1][c] == heap_pr[0]:
                    mv_pr = heapq.heappop(heap_pr)
                    # next min val
                    cur_path = cell + heap_pr[0]
                    heapq.heappush(heap_pr, mv_pr)
                else:
                    cur_path = cell + heap_pr[0]
            heapq.heappush(heap_cur, cur_path)
            mv_cache[r][c] = cur_path
        heap_pr = heap_cur
    return heap_pr[0]


#######################################################################
# Solution 1: Recursive DP
#
# Times out in python
#######################################################################

def min_fall_path(grid):
    n,m=len(grid), len(grid[0])
    if n==m==1:
        return grid[0][0]
    cache = [[None]*m for _ in range(n)]
    return min(
        _min_fall_path_rec(grid, row=0, col=col, cache=cache)
        for col in range(m)
    )


def _min_fall_path_rec(grid, row, col, cache):
    if row==len(grid):
        return 0
    if cache[row][col] is not None:
        return cache[row][col]
    min_val_nxt = float('inf')
    for nc in range(len(grid[0])):
        if nc == col:
            continue
        min_val_nxt =  min(
            min_val_nxt,
            _min_fall_path_rec(grid=grid, row=row+1, col=nc, cache=cache),
        )
    cell_min = grid[row][col] + min_val_nxt
    cache[row][col] = cell_min
    return cell_min

"""931. Minimum Falling Path Sum

https://leetcode.com/problems/minimum-falling-path-sum/

Solution: DP
"""

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        return _min_path_sum_botup(grid=matrix)

####################################################################
#               recursive solution
####################################################################

def _min_path_sum(grid: list[list[int]]) -> int:
    nrows, ncols = len(grid), len(grid[0])
    cache = [[None]*ncols for _ in range(nrows)]
    return min(
        _min_path_sum_rec(grid=grid, row=0, col=c, cache=cache)
        for c in range(ncols)
    )


def _min_path_sum_rec(
    grid: list[list[int]],
    row: int,
    col: int,
    cache: list[list[Optional[int]]],
) -> int:
    nrows, ncols = len(grid), len(grid[0])
    if row == nrows:
        return 0
    if cache[row][col] is not None:
        return cache[row][col]
    min_val = grid[row][col]  + min(
        _min_path_sum_rec(grid=grid, row=row+1, col=nc, cache=cache)
        for nc in (col-1, col, col+1)
        if 0 <= nc < ncols
    )
    cache[row][col] = min_val
    return min_val

####################################################################
#               bottom up solution
####################################################################

def _min_path_sum_botup(grid):
    nrows, ncols = len(grid), len(grid[0])
    # contains minimum value of getting here.
    # we add an extra row at the top to better handle edge case
    mv_cache = [[0]*ncols for _ in range(nrows+1)]
    minval = float('inf')
    for crow in range(1, nrows+1):
        for ccol in range(0, ncols):
            mv_cache[crow][ccol] = grid[crow-1][ccol] + min(
                mv_cache[crow-1][pc]
                for pc in (ccol-1, ccol, ccol+1)
                if 0 <= pc < ncols
            )
            if crow == nrows:
                minval = min(minval, mv_cache[crow][ccol])
    return minval

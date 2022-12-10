"""1289. Minimum Falling Path Sum II

https://leetcode.com/problems/minimum-falling-path-sum-ii/description/
"""


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        return min_fall_path(grid)


def min_fall_path(grid):
    n, m = len(grid), len(grid[0])
    if n == m == 1:
        return grid[0][0]
    cache = [[None] * m for _ in range(n)]
    return min(
        _min_fall_path_rec(grid, row=0, col=col, cache=cache) for col in range(m)
    )


def _min_fall_path_rec(grid, row, col, cache):
    if row == len(grid):
        return 0
    if cache[row][col] is not None:
        return cache[row][col]
    min_val_nxt = float("inf")
    for nc in range(len(grid[0])):
        if nc == col:
            continue
        min_val_nxt = min(
            min_val_nxt,
            _min_fall_path_rec(grid=grid, row=row + 1, col=nc, cache=cache),
        )
    cell_min = grid[row][col] + min_val_nxt
    cache[row][col] = cell_min
    return cell_min

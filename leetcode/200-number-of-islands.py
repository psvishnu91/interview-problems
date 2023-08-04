"""200. Number of Islands

https://leetcode.com/problems/number-of-islands/

Solution:
---------
- Create a seen 2-D matrix same size as the grid.
- Iterate over the grid
- If we find a "1" that is not seen before this
  is a new island, increment island counter.
- DFS and mark all connected "1"s as seen.
"""

import itertools

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = [[False]*n for _ in range(m)]
        num_islands = 0
        for i, j in itertools.product(range(m), range(n)):
            if grid[i][j] == "0" or seen[i][j]:
                continue
            num_islands += 1
            _dfs(i=i, j=j, grid=grid, seen=seen)
        return num_islands


def _dfs(i, j, grid, seen):
    seen[i][j] = True
    for adj_i, adj_j in _get_neibs(i=i, j=j, grid=grid):
        if seen[adj_i][adj_j]:
            continue
        _dfs(i=adj_i, j=adj_j, grid=grid, seen=seen)


def _get_neibs(i, j, grid):
    m, n = len(grid), len(grid[0])
    for adj_i, adj_j in [
        (i-1, j),
        (i+1, j),
        (i, j-1),
        (i, j+1),
    ]:
        if (
            (0 <= adj_i < m)
            and (0 <= adj_j < n)
            and grid[adj_i][adj_j] == "1"
        ):
            yield (adj_i, adj_j)

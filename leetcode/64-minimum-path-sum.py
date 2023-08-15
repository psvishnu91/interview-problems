"""64. Minimum Path Sum

https://leetcode.com/problems/minimum-path-sum/

Solution: DP T-S-O(mxn)
Create a mxn matrix. To get to any dp[i,j] = grid[i,j] + min(dp[i-1,j], dp[i,j-1]).
Gotcha handle dp[0,0]=grid[0,0]
"""

import itertools


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[None]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i, j in itertools.product(range(m), range(n)):
            if i==0 and j==0:
                continue
            top = dp[i-1][j] if i > 0 else float('inf')
            left = dp[i][j-1] if j > 0 else float('inf')
            dp[i][j] = grid[i][j] + min(top, left)
        return dp[m-1][n-1]

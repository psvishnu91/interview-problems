"""55. Jump Game

https://leetcode.com/problems/jump-game/description

Optimal Greedy - O(n)
---------------------
We start at the rightmost position and we want to find the first
index from the right that can reach this.
2 3 5 1 4
0 1 2 3 4
In the example above index 3 num[3] = 1 is the first index that can
reach four. Here on, we check if index 3 can be reached instead of
final index index 4. In our example thought index=2, num[2]=5
can also reach index 4 but this is not a problem. If it can
reach index=4, it can reach index=3 and since index=3 can reach
the end we don't care that it reaches further. 

Brute force solution: DP
------------------------
Try every possible option.
T - O(n^2) 

Suboptimal Greedy + DP (faster)
-------------------------------
We try to find the first index from the left
that can reach the last index. And then we
recursively check if that index can be reached
from the first index from the left and until
we arrive at the starting index.

"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target_ix = n - 1
        for ix in range(n-2, -1, -1):
            if nums[ix] + ix >= target_ix:
                target_ix = ix
        return nums[0] >= target_ix

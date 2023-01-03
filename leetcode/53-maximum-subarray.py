"""53. Maximum Subarray

https://leetcode.com/problems/maximum-subarray

Algorithm
---------
- Keep track of run_sum and max_sum
- If run_sum is neg make it zero
- max_sum = max(num+rs, max_sum)

Test
[-2,1,-3,4,-1,2,1,-5,4]

num     rs      ms
------------------
        0       -2
-2      0      -2
1       1       1
-3      0       1
4       4       4
-1      3       4
2       5       5
1       6       6
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, run_sum = nums[0], 0
        for num in nums:
            run_sum += num
            max_sum = max(max_sum, run_sum)
            run_sum = max(0, run_sum)
        return max_sum

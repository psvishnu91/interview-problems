"""643. Maximum Average Subarray I

https://leetcode.com/problems/maximum-average-subarray-i
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        max_total = total
        for prev, cur in zip(nums, nums[k:]):
            total += cur - prev
            max_total = max(max_total, total)
        return max_total / k

"""1. Two Sum

https://leetcode.com/problems/two-sum

"Gotcha: Same number can appear twice. 

Create a dict mapping each element to set of indices. Iterate over each element find diff=target-num, if diff in map, get indices. Remove index of num and if there is another index return value."
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_ix_map = defaultdict(set)
        for i, num in enumerate(nums):
            num_ix_map[num].add(i)
        for i, num in enumerate(nums):
            diff = target - num
            if diff not in num_ix_map:
                continue
            diff_ixes = num_ix_map[diff]
            other_ixes = [j for j in diff_ixes if i!=j]
            if other_ixes:
                return [i, other_ixes[0]]
                

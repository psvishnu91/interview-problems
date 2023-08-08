"""167. Two Sum II - Input Array Is Sorted

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

Solution: Two pointer - O(n)
if sum < tgt, move lt ptr fwd,
if sum > tgt, move rt ptr back

The reason this works is because the array is sorted
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lt, rt = 0, len(numbers)-1
        while lt < rt:
            this_total = numbers[lt] + numbers[rt]
            if this_total == target:
                return [lt + 1, rt + 1]
            elif this_total < target:
                lt += 1
            else: 
                # this_total > target
                rt -= 1
        else:
            raise ValueError("No solution found")

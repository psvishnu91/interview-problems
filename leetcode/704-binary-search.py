"""704. Binary Search

https://leetcode.com/problems/binary-search/description/
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lt, rt = 0, n - 1
        while lt <= rt:
            mid = (lt + rt) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lt = mid + 1
            else:
                rt = mid - 1
        else:
            return -1

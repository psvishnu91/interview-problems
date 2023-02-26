"""35. Search Insert Position

https://leetcode.com/problems/search-insert-position/

Idea is same as bisect_left and solution is binary search.
Find the first index larger than target if not found
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        1 3 5 6
        0 1 2 3
        t=2
        l r m n[m] ix
        ----------
        0 3 1 3     1
        0 1 0 1  
        1 1 1 3     1
        1 0
        """
        n = len(nums)
        lt, rt, insert_ix = 0, n-1, n
        while lt <= rt:
            mid = (lt + rt) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lt = mid + 1
            else:
                # nums[mid] > target
                insert_ix = mid
                rt = mid - 1
        else:
            return insert_ix

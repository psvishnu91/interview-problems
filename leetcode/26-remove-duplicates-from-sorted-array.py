"""26. Remove Duplicates from Sorted Array

https://leetcode.com/problems/remove-duplicates-from-sorted-array


Rough
-----
0 0 1 1 1 2 2 3 3 4
  l r
0 1 0 1 1 2 2 3 3 4
    l     r
0 1 2 1 1 0 2 3 3 4
      l       r
0 1 2 3 1 0 2 3 3 4
        l         r
0 1 2 3 4 0 2 3 3 1
          l         r
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        lt = rt = 0
        while lt < n and rt < n:
            while rt < n and nums[lt] == nums[rt]:
                rt += 1
            if rt == n:
                break
            lt += 1
            nums[lt] = nums[rt]
        return lt + 1

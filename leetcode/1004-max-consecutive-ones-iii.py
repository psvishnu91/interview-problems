"""1004. Max Consecutive Ones III

https://leetcode.com/problems/max-consecutive-ones-iii

edge case
-------
k=0, starts w 1 and 0
empty list
all zeros and all ones
nominal
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Idea sliding window
        -------------------
        1 1 1 0 0 0 1 1 1 1 0
        0 1 2 3 4 5 6 7 8 9 0
        k = 2

        l   r 0cnt max 
        ---------------
        0   0   0     1
            1   0         2
            2   0         3
            3   1         4  = r-l+1
            4   2         5
            5 3
        1
        2
        3     2
        4 5   2   2

        k=0 case
        0 0 1 0 0 0 1 1 1 1 0 
        """
        lt, zero_cnt, max_sz = 0, 0, 0
        for rt, num in enumerate(nums):
            if num == 1:
                max_sz = max(max_sz, rt - lt + 1)
            else:
                zero_cnt += 1
                while lt <= rt and zero_cnt > k:
                    if nums[lt] == 0:
                        zero_cnt -= 1
                    lt += 1
                max_sz = max(max_sz, rt - lt + 1)
        return max_sz

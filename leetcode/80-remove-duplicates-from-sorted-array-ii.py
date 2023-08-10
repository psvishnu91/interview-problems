"""80. Remove Duplicates from Sorted Array II

https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        lt = rt = 0
        cur_num, cnt = nums[lt], 0
        """
        0 1 1 1 1 2 2 2 3
        0 1 2 3 4 5 6 7 8

        i ni j nj arr
        0 0         [0 1 1 1 1 2 2 2 3]
        1 1  3 1    [0 1 1 N N 2 2 2 3]
             5 2
        5 2  7 2    [0 1 1 N N 2 2 N 3]
             8 3

        [0 1 1 2 2 3 N N 3]
         0 1 2 3 4 5 6 7 8
                     l     r
        l nl r nr arr
        0 0  0 0
        1
        2
        3 N  4 N [0 1 1 N N 2 2 N 3]
             5 2 [0 1 1 2 N 2 2 N 3]
              
        """
        # -----------------------------------------------------
        # Go through the array and mark all duplicates as None
        #
        # We will go from the front with i. If i+1 is not the
        # same num, we move i to i+1. If it is the same, we
        # create j = i + 2, mark all nums from j which are equal
        # nums[i] as None. Then, we move i to j (first different)
        # num.
        # -----------------------------------------------------
        i = 0
        while i < n - 1:
            if nums[i] != nums[i+1]:
                i += 1
                continue
            j = i + 2
            while j < n and nums[j] == nums[i]:
                nums[j] = None
                j += 1
            i = j
        # -----------------------------------------------------
        # Go through the array again and move all the Nones to
        # the end.
        #
        # We move a lt pointer until we ecounter a None.
        # If we encounter a None, we move
        # a rt pointer either from it's current pos or lt + 1
        # whichever is greater. We move rt until it's not None
        # and we swap the first not None with lt. Then we move
        # both lt and rt.
        # -----------------------------------------------------
        lt = rt = 0
        while lt < n and rt < n:
            if nums[lt] is not None:
                lt += 1
            else:
                rt = max(rt, lt+1)
                while rt < n and nums[rt] is None:
                    rt += 1
                if rt == n:
                    break
                nums[lt], nums[rt] = nums[rt], nums[lt]
                lt += 1
                rt += 1
        return lt

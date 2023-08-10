"""189. Rotate Array

https://leetcode.com/problems/rotate-array

Solution:
---------
Reverse the last k elements.
Reverse the first n-k elements.
Reverse the whole array

1 2 3 4 5 k=2
3 2 1 5 4
5 4 3 2 1
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        # k can be greater than the length of the array. Notice
        # that if k = n, then we don't rotate the array at all,
        # which means we want k to be 0 (so no off by 1 errors).
        k = k % n
        # reverse last k elements
        reverse(nums, start_ix=n-k, end_ix=n-1)
        # reverse first n-k elements
        reverse(nums, start_ix=0, end_ix=n-k-1)
        # reverse the whole array
        reverse(nums, start_ix=0, end_ix=n-1)


def reverse(nums, start_ix, end_ix):
    while start_ix < end_ix:
        nums[start_ix], nums[end_ix] = nums[end_ix], nums[start_ix]
        start_ix += 1
        end_ix -= 1

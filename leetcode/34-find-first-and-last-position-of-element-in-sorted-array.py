"""34. Find First and Last Position of Element in Sorted Array

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
"""
import functools as ft

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        bisect_left = ft.partial(bisect, shift_fn=lambda lt, rt, mid: (lt, mid-1))
        bisect_right = ft.partial(bisect, shift_fn=lambda lt, rt, mid: (mid+1, rt))
        left_ix = bisect_left(nums, target)
        if left_ix == -1:
            return [-1, -1]
        right_ix = bisect_right(nums, target)
        return [left_ix, right_ix]


def bisect(nums, target, shift_fn):
    n = len(nums)
    lt, rt, target_ix = 0, n-1, -1
    while lt <= rt:
        mid = (lt + rt) // 2
        if nums[mid] == target:
            target_ix = mid
            lt, rt = shift_fn(lt, rt, mid)
        elif nums[mid] > target:
            rt = mid - 1
        else:
            # nums[mid] < target
            lt = mid + 1
    return target_ix

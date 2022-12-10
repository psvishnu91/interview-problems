"""34. Find First and Last Position of Element in Sorted Array

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Solution
========
Perform binary search twice once looking for the lt
boundary once for rt boundary. The bin search function takes
what side it should search for. left size, one go to the left
when target is seen after updating return value to mid. similarly
for rt boundary.

Gotcha
======
You might feel it makes sense to recursively search left and right
unless you see the target in which case you are tempted to search
both sides. But this will be O(n), imagine all numbers are the target.
Then the recursion can be written as

T(n) = 2 T(n/2) + O(n^0)
From master method: https://vishnu.uk/blogs/algorithms.html#master-method
T(n) = a T(n/b) + O(n^d)
a > b^d => 2 > 2^0
This is the third case, O(n^(log_b(a))) => O(n^(log_2(2))) = O(n)
"""
from enum import Enum


class Boundary(Enum):
    LEFT = 1
    RIGHT = 2


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return search_range_it(nums=nums, tgt=target)


def search_range_it(nums, tgt):
    return [
        _search_it(nums=nums, tgt=tgt, boundary=Boundary.LEFT),
        _search_it(nums=nums, tgt=tgt, boundary=Boundary.RIGHT),
    ]


def _search_it(nums, tgt, boundary):
    lt, rt = 0, len(nums) - 1
    ix = -1
    while lt <= rt:
        mid = (lt + rt) // 2
        if nums[mid] < tgt:
            lt = mid + 1
        elif nums[mid] > tgt:
            rt = mid - 1
        else:
            ix = mid
            if boundary == Boundary.LEFT:
                rt = mid - 1
            else:
                lt = mid + 1
    return ix


"""
Incorrect solution:

This implementation below runs in O(N) time.
"""


def search_range(nums, tgt):
    if not nums:
        return [-1, -1]
    return _search_rec(nums, tgt=tgt, lt=0, rt=len(nums) - 1)


def _search_rec(nums, tgt, lt, rt):
    if lt > rt:
        return [-1, -1]
    mid = (lt + rt) // 2
    lt_kwargs = dict(nums=nums, tgt=tgt, lt=lt, rt=mid - 1)
    rt_kwargs = dict(nums=nums, tgt=tgt, lt=mid + 1, rt=rt)
    if nums[mid] < tgt:
        min_ix, max_ix = _search_rec(**rt_kwargs)
    elif nums[mid] > tgt:
        min_ix, max_ix = _search_rec(**lt_kwargs)
    else:
        min_ix, _ = _search_rec(**lt_kwargs)
        _, max_ix = _search_rec(**rt_kwargs)
        min_ix = mid if min_ix == -1 else min_ix
        max_ix = mid if max_ix == -1 else max_ix
    return [min_ix, max_ix]

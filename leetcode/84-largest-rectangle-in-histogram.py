"""84. Largest Rectangle in Histogram

https://leetcode.com/problems/largest-rectangle-in-histogram/

Intuition
---------

I want to build two arrays left and right which such that
left[i] and right[i] the left_most and the right_most indices
that are at least of height nums[i]. This is the window up to
which i can expand with the current height.

Datastructures: one Stack and two lists left and right

    * left[i] contains the index of the nearest element to the left
    of the nums[i] that is < nums[i]. So all the numbers
    nums[lt[i]+1:i+1] are of size at least nums[i].
    
    * |||ly, right[i] contains the nearest element to the rt
    of the nums[i] that is < nums[i], in other words
    all the numbers between nums[i:rt[i]] are at least
    nums[i].

- [-inf] + [nums] + [-inf], so that min val of lt[i] is -1
    and max val of rt[i] is n
- iterate over nums lt to right and build lt. Use a stack
    the stack will have invariant smallest num seen so far
    at the bottom and largest num at top, we remove all stack
    elements that are gt than nums[i], and add nums[i] to top
    of stack. This is so that all future numbers need to end
    at this number as this is the first smallest number lt of
    them. Bigger numbers to the left of it don't help the number
    to the right to build a bigger hist.
- iterate from rt to lt maintaining the same invariant in the stack
- iterate over nums, lt, rt and compute max size histogram as
    (rt-lt-1) * nums[i]. This is because nums[i] is the smallest
    height in this bin. We keep track of max rect area as we compute this.
"""
import dataclasses
from collections import deque

@dataclasses.dataclass(frozen=True)
class StackItem:
    ix: int
    ht: int


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return largest_rect_area_rfctd(heights)


########################
# Refactored Stack
########################


def largest_rect_area_rfctd(heights: list[int]) -> int:
    n = len(heights)
    lt = _build_max_window(heights=heights, reversed=False)
    rt = _build_max_window(heights=heights, reversed=True)
    max_hist = heights[0]
    for l, r, ht in zip(lt, rt, heights):
        max_hist = max(max_hist, ht * (r - l - 1))
    return max_hist


def _build_max_window(heights, reversed=False):
    """Builds a window to lt or right depending on reversed
    such that all values in window[i] are greater than or equal
    to hts[i].
    """
    n = len(heights)
    window = [None] * n
    if not reversed:
        iterand = range(n)
        stk = deque([StackItem(ix=-1, ht=-float("inf"))])
    else:
        iterand = range(n - 1, -1, -1)
        stk = deque([StackItem(ix=n, ht=-float("inf"))])
    for i in iterand:
        ht = heights[i]
        while stk[-1].ht >= ht:
            stk.pop()
        window[i] = stk[-1].ix
        stk.append(StackItem(ix=i, ht=ht))
    return window


##############
# Stack unrefactored
################


def largest_rect_area(heights: list[int]) -> int:
    n = len(heights)
    lt, rt = [None] * n, [None] * n
    stk = dequedeque([StackItem(ix=-1, ht=-float("inf"))])
    for i, ht in enumerate(heights):
        while stk[-1].ht >= ht:
            stk.pop()
        lt[i] = stk[-1].ix + 1
        stk.append(StackItem(ix=i, ht=ht))
    stk.clear()
    stk.append(StackItem(ix=n, ht=-float("inf")))
    for i in range(n - 1, -1, -1):
        ht = heights[i]
        while stk[-1].ht >= ht:
            stk.pop()
        rt[i] = stk[-1].ix - 1
        stk.append(StackItem(ix=i, ht=ht))
    max_hist = heights[0]
    for l, r, ht in zip(lt, rt, heights):
        max_hist = max(max_hist, ht * (r - l + 1))
    return max_hist

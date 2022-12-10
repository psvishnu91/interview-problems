"""1856. Maximum Subarray Min-Product

https://leetcode.com/problems/maximum-subarray-min-product/description/

You need to know that this problem is similar to the histogram problem etc.

TRICK
In these problems, you need to keep track of which was the last element greater
than or less than the element in the current index.
You need three datastructures
- STACK<(index, num)>
- Two lists left and right

If you want to keep track of the last number smaller than the current number the
invariant you need to maintain is that the stack has the smallest element at the
bottom and the largest element in the top. Additionally the current element should
be the largest element, any element larger than this element should be popped out.
Similarly if you want to keep track of the last number greater than the current
number, keep the invariant that the stack has the largest element at the bottom
and the smallest element on top. current number should be the smallest element,
pop out elements smaller than this pop until you get to this invariant.

You have to do this twice, once populating the left list and once for the right list.
"""
from queue import deque


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        return max_sum_min_pdct(nums=nums)


def max_sum_min_pdct(nums):
    if not nums:
        return 0
    n = len(nums)
    stk = deque()
    lt, rt, = [
        None
    ] * n, [None] * n
    ps = build_ps(nums)
    for i, num in enumerate(nums):
        while stk and stk[-1][1] >= num:
            stk.pop()
        lt[i] = 0 if not stk else stk[-1][0] + 1
        stk.append((i, num))
    stk.clear()
    for i, num in reversed(list(enumerate(nums))):
        while stk and stk[-1][1] >= num:
            stk.pop()
        rt[i] = n - 1 if not stk else stk[-1][0] - 1
        stk.append((i, num))
    max_min_prod = 0
    for i in range(n):
        max_min_prod = max(
            max_min_prod, nums[i] * (ps[rt[i]] - ps[lt[i]] + nums[lt[i]])
        )
    return max_min_prod % (10**9 + 7)


def build_ps(nums):
    ps = [None] * len(nums)
    rs = 0
    for i, num in enumerate(nums):
        rs += num
        ps[i] = rs
    return ps

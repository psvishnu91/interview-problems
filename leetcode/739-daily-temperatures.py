"""739. Daily Temperatures

https://leetcode.com/problems/daily-temperatures/

Invariant: We maintain monotonic decreasing stack of (index, temp)
(non-increasing to be precise to account for duplicates).
If we see a higher value than the top of the stack, we
keep popping from the stack until the invariant is met.
As we pop out, we update answer[ix].

if not stk:
    stk.append((i, tmp))
else:

"""
from dataclasses import dataclass


@dataclass
class StkItem:
    ix: int
    temp: int


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        73 74 75 71 69 72 76 73
        0   1  2  3  4  5  6  7

        ans
        1 1 4 2 1 1
        0 1 2 3 4 5 6 7

        i   tmp    stk          ans
        0   73      [(0, 73)]   []
        1   74      [(1, 74)]   [1,...]
        2   75      [(2, 75)]   [1,1,...]
        3   71      [(2, 75), (3, 71)]
        4   69      [(2, 75), (3, 71), (4, 69)]  [1,1,,,,]
        5   72      [(2,75), (5,72)]
        6   76      [(6,76)]
        7   73      [(6,76), ()]

        """
        stk, ans = [], [0] * len(temperatures)
        for ix, temp in enumerate(temperatures):
            while stk and stk[-1].temp < temp:
                popped = stk.pop()
                ans[popped.ix] = ix - popped.ix
            stk.append(StkItem(ix=ix, temp=temp))
        return ans

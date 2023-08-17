"""69. Sqrt(x)

https://leetcode.com/problems/sqrtx/

Binary search O(log n)
-------------
x = 8

l r m ms 
--------
1 5 3 9
1 2
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        return binsearch(x=x)


def binsearch(x):
    if x == 0 or x == 1:
        return x
    lt, rt = 1, x // 2 + 1
    while lt <= rt:
        mid = (lt + rt) // 2
        mid_sq = mid * mid
        if mid_sq > x:
            rt = mid - 1
        elif mid_sq < x:
            lt = mid + 1
        else:
            # mid_sq == x
            return mid
    return lt - 1

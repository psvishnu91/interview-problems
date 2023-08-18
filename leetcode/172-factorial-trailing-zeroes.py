"""Factorial trailing zeros

https://leetcode.com/problems/factorial-trailing-zeroes/

Idea
-----
Sum the number of integers up to n, divisible by 5, 25, 625, 3125

The idea is
1. We always have a lot more 2s than 5s, so the bottleneck is 5s.
2. For every multiple of 5, we get one zero
3. For every multiple of 25, 125, 625, 3125 we get extra one
    zero each

Number of zero contributions
5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100
1  1  1  1 2   1 1   1  1 2  1  1  1  1  2   1  1  1  1  2

Exploration
-----------
11!
11 x 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1
"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        assert 0 <= n <= 10**4
        # p - 1,2,3,4,5 because 5^5 -> 3125 and 5^6 > 10
        return sum(n // (5**p) for p in range(1, 6))
            

"""238. Product of Array Except Self

https://leetcode.com/problems/product-of-array-except-self/

Algorithm:
- Create an output array of Nones
- First pass lt to rt, keep track of run_prod rp
    iterate from i range(0, n-1): assign rp to i+1
- Second pass rt to lt, keep track of run_prod rp
    iterate from i range(n-1,0,-1): multiply output[i-1]*rp

Test

Nominal
1 2 3 4
0 1 2 3

i    num   rp   out
-------------------
            1    [N N N N]
0      1    1    [N 1 N N]
1      2    2    [N 1 2 N]
2      3    6    [N 1 2 6]


Edge cases
i    num   rp   out
-------------------
            1    [N 1 2 6]
3      4    4    [N 1 8 6]
2      3    12   [N 12 8 6]
1      2    24   [24 12 8 6]
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rp, output = 1, [1]*n
        for i in range(0,n-1):
            rp *= nums[i]
            output[i+1] = rp
        rp = 1
        for i in range(n-1, 0, -1):
            rp *= nums[i]
            output[i-1] *= rp
        return output

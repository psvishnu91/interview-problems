"""2333. Minimum Sum of Squared Difference

https://leetcode.com/problems/minimum-sum-of-squared-difference/

Brute force
===========
- Compute sum of squared difference of all elements with no change
- begin with i=0
    each time upto 2(k1+1)*2(k2+1) options (2(k+1) because we can plus or minus or do nothing
    min_sum = min(
        (n1_mod-n2_mod)**2 + min_sqrd(i+1,k1) 
        for n1_mod, n2_mod in options(n1, n2, k1, k2) 
    )
    cache[(i, k1, k2)] = min_sum

T- O(n^(k1*k2))
M- O(n * k1 * k2)    
"""

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        return min_sum_sqrd(nums1, nums2, k1, k2)

    
def min_sum_sqrd(nums1, nums2, k1, k2):
    cache = [[[None]*(k2+1) for _ in range(k1+1)] for _ in range(len(nums1))]
    return _min_sum_sqrd_rec(
        nums1=nums1, nums2=nums2, k1=k1,
        k2=k2, i=0, cache=cache,
    )


def _min_sum_sqrd_rec(nums1, nums2, k1, k2, i, cache):
    if i == len(nums1):
        return 0
    if cache[i][k1][k2] is not None:
        return cache[i][k1][k2]
    min_sqrd = min(
        (
            ((n1_mod - n2_mod)**2)
            + _min_sum_sqrd_rec(
                nums1, nums2, k1=k1_mod, k2=k2_mod,
                i=i+1, cache=cache
            )
        )
        for n1_mod, n2_mod, k1_mod, k2_mod in _modifications(
            n1=nums1[i], n2=nums2[i], k1=k1, k2=k2,
        )
    )
    cache[i][k1][k2] = min_sqrd
    return min_sqrd


def _modifications(n1, n2, k1, k2):
    for n1_diff, n2_diff in itertools.product(
        range(0, k1+1), range(0, k2+1)
    ):
        k1_mod = k1 - n1_diff
        k2_mod = k2 - n2_diff
        for (n1_mult, n2_mult) in itertools.product((-1,1), (-1,1)): 
            n1d = n1_diff * n1_mult
            n2d = n2_diff * n2_mult
            n1_mod = n1 + n1d  
            n2_mod = n2 + n2d
            if (n1_mod < 0)  or (n2_mod < 0):
                continue
            yield (n1_mod, n2_mod, k1_mod, k2_mod)

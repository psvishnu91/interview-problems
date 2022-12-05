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
            _sqrd_dist(n1_mod, n2_mod)
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
    """Adjacent nodes, potential modifications of these numbers.
    
    Based on whichever is greater, we only go in one
    direction for each
    n1  n2
    ------
    10, 15
    4    4
    [(10,11,12,13,14)] [(15,14,13,12,11)]
    
    n1  n2
    ------
    10, 12
    4    4
    [(14,13,12)] [(15,14,13,12,11)]
    
    In the above ex, n1 inc and n2 dec
    Additionally we don't have to search for values where now
    new_n1 is greater than new_n2. Equivalently n2 need not
    decrease below n1.
    
    Alogirthm
    ---------
    if n1==n2:
        yield (n1, n2, k1, k2, min_dist=0)
        return
    if n1 > n2:
        # We reduce n1 towards n2, no point reducing beyond n2
        min_n1 = max(n1-k1, n2)
        search_n1_k1 = [
            (new_n, k1-kdiff) for kdiff, new_n in enumerate(range(n1,min_n1-1, -1))
        ] 
        max_n2 = min(n2+k2, n1)
        search_n2_k2 = [
            (new_n, k2-kdiff) for kdiff, new_n in enumerate(range(n2,max_n2+1))
        ]
        search_space = [
            (new_n1, new_k1, new_n2, new_k2)
            for (new_n1, new_k1), (new_n2, new_k2) in itertools.product(
                search_n1_k1,  search_n2_k2
            )
            # no point searching space where we either dec n1 or inc n2
            # so that now new_n1 < new_n2
            if new_n1 >= new_n2
        ]
    if n2 > n1:
        same but opposite
    """
    if n1 == n2:
        yield (n1, n2, k1, k2)
    elif n1 > n2:
        yield from _iter_new_nks(
            big_n=n1, small_n=n2, big_k=k1, small_k=k2,
        )
    else:
        # n2 > n1
        for new_n2, new_n1, new_k2, new_k1 in _iter_new_nks(
            big_n=n2, small_n=n1, big_k=k2, small_k=k1,
        ):
            yield (new_n1, new_n2, new_k1, new_k2)


def _iter_new_nks(big_n, small_n, big_k, small_k):
    max_small_n = min(small_n+small_k, big_n)
    # new big vals
    min_big_n = max(big_n-big_k, small_n)
    search_big_nk = [
        (new_n, big_k-kdiff) for kdiff, new_n in enumerate(
            range(big_n, min_big_n-1, -1)
        )
    ]
    # new small vals
    search_small_nk = [
        (new_n, small_k-kdiff) for kdiff, new_n in enumerate(
            range(small_n, max_small_n+1)
        )
    ]
    for (new_big_n, new_big_k), (new_small_n, new_small_k) in itertools.product(
        search_big_nk,  search_small_nk
    ):
        # no point searching space where we either dec big_n or inc small_n
        # so that we cross over
        if new_big_n < new_small_n:
            continue
        yield (new_big_n, new_small_n, new_big_k, new_small_k) 


def _sqrd_dist(n1, n2):
    return (n1 - n2) ** 2

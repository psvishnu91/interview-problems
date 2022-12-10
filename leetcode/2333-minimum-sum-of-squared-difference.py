"""2333. Minimum Sum of Squared Difference

https://leetcode.com/problems/minimum-sum-of-squared-difference/

Ideas
=====
Squared error is worst for higher values diff = 1, sqrd dist 1, diff=3, sqrd_dist=9.
So our approach should be to reduce the current max dist to the next max dist
using k=k1+k2. Keep repeating till we exhaust k or the largest value becomes
0.

Datastructure: Binary Search Tree (TreeMap, Python - sortedcontainers.SortedDict)
--------------

Scenarios:
----------
1. k is exhaustible
- This happens if there is only one distance (max_dist) or k < num(max_dist)
- In either case compute max_redn = k // num(max_dist), reduce the
    all max values by this number (this can be 0 if k<num(max_dist)).
- compute remainder rem = k % num(max_dist), further reduce rem number
    of max_dists by 1

2. k is not exhaustible
- This happens when either there is another distance (next_max_dist), or
    k > num(max_dist)
- In this case reduce the max_dist by min(next_max_dist, k//num(max_dist)).
    If there exists next_max_dist
        and is the lowerbound, all num(max_dist) will be converted to next_max_dist
        else if not binding, then we reduce all max_dist as much as possible
        and then in next iteration k < num(max_dist) and will reduce as many max_dists
        in the previous clause.
    If there is no next_max_dist but k > num(max_dist),
        then we exhaust in as much as possible so that in the next round k is
        exhaustible (k < num(max_dist))

k = (k1+k2)
T- O(n log n + k log n))
M- O(n)
"""
import sortedcontainers


class Solution:
    def minSumSquareDiff(
        self, nums1: List[int], nums2: List[int], k1: int, k2: int
    ) -> int:
        return min_sum_sqrd(nums1, nums2, k1, k2)


def min_sum_sqrd(nums1, nums2, k1, k2):
    dists = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
    # maintains a sorted map of dist to count of distance
    dists_ctr = sortedcontainers.SortedDict(Counter(dists))
    k = k1 + k2
    while k > 0:
        max_dist, num_max_dists = dists_ctr.popitem(index=-1)
        if max_dist == 0:
            break
        if not dists_ctr or k < num_max_dists:
            # 1. k is exhaustible
            # In this scenario we exhaust k to 0
            #
            # 1) all dists are same
            # k - 11, num_mx_dists=4, max_redn=2, num_reduc_by_1=3
            # 2) k < num_mx_dists
            # k -3, num_mx_dists = 4, max_redn=0, num_reduc_by_1=3
            max_redn = k // num_max_dists
            num_reducible_by_1 = k % num_max_dists
            lrg_dist = max(max_dist - max_redn, 0)
            sml_dist = max(lrg_dist - 1, 0)
            dists_ctr[lrg_dist] = (
                dists_ctr.get(lrg_dist, 0) + num_max_dists - num_reducible_by_1
            )
            dists_ctr[sml_dist] = dists_ctr.get(sml_dist, 0) + num_reducible_by_1
            k = 0
        else:
            # 2. k is not exhaustible in this iteration
            #
            # In this case we move all max_dist to the next largest max_dist. If
            # not enough k, we move as much as possible. We move all `max_dist`
            # by the same amount. After this step k is guaranteed to be smaller
            # than the number of max dist. So it will be used up in the above
            # if clause in the next iteration.
            next_dist, _ = dists_ctr.peekitem(index=-1)
            max_redn = k // num_max_dists
            new_max_dist = max(next_dist, max_dist - max_redn)
            k -= num_max_dists * (max_dist - new_max_dist)
            dists_ctr[new_max_dist] = dists_ctr.get(new_max_dist, 0) + num_max_dists
    return sum(cnt * (dist**2) for dist, cnt in dists_ctr.items())

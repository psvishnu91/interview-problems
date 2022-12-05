"""2333. Minimum Sum of Squared Difference

https://leetcode.com/problems/minimum-sum-of-squared-difference/

Algorithm
=========

Logic, squared error is worst for higher values diff = 1, sqrd dist 1, diff=3, sqrd_dist=9
- compute abs(diff) and push them into a heap
- ki = k1+k2

k = (k1+k2)
T- O(n*k))
M- O(n)


next_max_dist not None
-----------------------
4, 4, 4, 4, 2, 1
num_eql_dists = 4
next_max_dist = 2
k=3, k=4, k=8, k=12

[
k=3: k < num_eql_dists:
-> insert k, max_dist-1 and num_eql_dists-k, max_dist

k=4: k == num_eql_dists
    -> insert k, max_dist-1 and num_eql_dists-k, max_dist
]
k=8: k > num_eql_dists:
    max_redn = k // num_eql_dists = 2
    new_max_dist = max(next_max_dist, max_dist-max_redn)
    new_max_dist = max(2, 4-2)= 2
    insert num_eql_dists of value new_max_dist
k=12: k > num_eql_dists:
    max_redn = k // num_eql_dists = 3
    new_max_dist = max(next_max_dist, max_dist-max_redn)
    new_max_dist = max(2, 4-3) = 2
    insert num_eql_dists of value new_max_dist

4, 4, 4, 4
num_eql_dists = 4
next_max_dist = None
k=2, k=4, k=7, k=8

next_max_dist is None
---------------------
max_redn = k//num_eql_dists
rem_reducible = k%num_eql_dists
num_eql_dists - rem_reducible => max_dist - max_redn
rem_reducible = max_dist - max_redn - 1
"""
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        return min_sum_sqrd(nums1, nums2, k1, k2)

    
def min_sum_sqrd(nums1, nums2, k1, k2):
    # max heap so negation
    dists = [abs(n1-n2) for n1, n2 in zip(nums1, nums2)]
    # maintains a dist to count of it
    dist_ctr = Counter(dists)
    k = k1+k2
    while k > 0:
        max_dist = max(dist_ctr)
        num_max_dists = dist_ctr[max_dist]
        if max_dist == 0:
            break
        # print(f"{k=}, {max_dist=}, {dist_ctr=}")
        if len(dist_ctr) == 1:
            # all dists are same
            del dist_ctr[max_dist]
            max_redn = k // num_max_dists
            num_reducible_by_1 = k % num_max_dists
            dist_ctr[max(max_dist - max_redn,0)] += num_max_dists - num_reducible_by_1
            dist_ctr[max(max_dist - max_redn - 1,0)] += num_reducible_by_1
            k = 0
        else:
            next_dist = max(d for d in dist_ctr if d != max_dist)
            if k < num_max_dists:
                dist_ctr[max_dist] -= k
                dist_ctr[max_dist-1] += k
                k = 0
            else:
                max_redn = k // num_max_dists
                new_max_dist = max(next_dist, max_dist-max_redn)
                del dist_ctr[max_dist]
                dist_ctr[new_max_dist] += num_max_dists
                k -= num_max_dists * (max_dist-new_max_dist)
    # print(f"{k=}, {max_dist=}, {dist_ctr=}")
    return sum(cnt*(dist**2) for dist, cnt in dist_ctr.items())

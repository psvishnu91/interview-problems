"""373. Find K Pairs with Smallest Sums

https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

Understanding the problem
-------------------------
There are many tricky things to note. Look at the following examples

Example 1: Simple
-----------------
[1,2,3,4,5], [1,2,3] k=5

The logical thing to do looks like just have a lt pointer and a rt
pointer. Move over the rt array once [(1,1), (1,2), (1,3)] and
then update lt pointer [(2,1), (2,2)].

Example 2: Repeated
-------------------
[1,1,1,2,3,4,5], [1,2,3] k=5
Here correct answer is [[1,1], [1,1], [1,1], [1,2], [1,2]]
The above approach will fail.

Okay we may think we keep count of same numbers repeate second
array until we reach end. This is also wrong

Example 3: Large num in second array
------------------------------------
[1,2,3,4,5], [1,2,1000] k=5

With the above approach we will return [[1,1], [1,2], [1,1000], [2,1], [2,2]]
whereas the correct answer is [[1,1], [1,2], [2,1], [2,2], [3,1]]

=================================================
Solution 1: Use heaps
----------------------
- We create a heap with one entry [PS(total=n1[0]+n2[0], lt=0, rt=0)]
- The heap will always have the smallest value pair at the front.
- While the heap is not empty,
    - we pop from the heap, where for the first time we get lt=0 rt=0.
    - we inject [Example: n1=[1,2,3],n2=[1,9999]]
        * rt=1 into the heap, PS(total=n1[0]+n2[1]), (check, [1, 9999])
        * we should also inject, lt=1, and rt=0 ([2,1])
- so everytime, [lt,0] is used up [rt,0] is to the heap. This way
    we can keep track of the last rt for each lt as well.

Complexity
------------
m,n = len(nums1), len(nums2)
- T-O(m log m), every element in nums1 can only appear in heap 
    once for the second array start_ix
- S-O(m log m)

Optimisation: Swap smaller array to be nums1
---------------------------------------------
We saw in previous case the complexity depends only on size of
nums1. We make the smaller array nums1 to optimise.

m,n = len(nums1), len(nums2)
k = min(m, n)
- T-O(k log k)
- S-O(k log k)
"""
from dataclasses import dataclass
import heapq as hq

@dataclass(order=True)
class PairSum:
    total: int
    lt: int
    rt: int

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        return approach_heap(nums1=nums1, nums2=nums2, k=k)

def approach_heap(nums1, nums2, k):
    """
    Testing
    ------
    1 1 2
    0 1 2

    1 2 3
    0 1 2

    heap=[(2, 0,0), (2, 1,0), (3, 2,0)]

    ps lt rt nlt nrt
    ----------------
       0  0   1   1   [[1,1]]
       1  0   1   1    [[1,1]] 
    """
    # Time complexity depends on which array is nums1
    # We swap the smaller array to be nums1 as a further optimisation.
    len1, len2 = len(nums1), len(nums2)
    to_swap = len1 > len2
    if to_swap:
        pairs = _solve_w_heap(nums1=nums2, nums2=nums1, k=k)
        return [[p2, p1] for p1, p2 in pairs]
    else:
        return _solve_w_heap(nums1=nums1, nums2=nums2, k=k)


def _solve_w_heap(nums1, nums2, k):
    len1, len2 = len(nums1), len(nums2)
    heap = [PairSum(total=nums1[0]+nums2[0], lt=0, rt=0)]
    pairs = []
    while heap:
        ps = hq.heappop(heap)
        lt, rt = ps.lt, ps.rt
        pairs.append([nums1[lt], nums2[rt]])
        if len(pairs) == k:
            return pairs
        if rt == 0 and lt + 1 < len1:
            hq.heappush(
                heap,
                PairSum(total=nums1[lt+1]+nums2[0], lt=lt+1, rt=rt),
            )
        if rt+1 < len2:
            hq.heappush(
                heap,
                PairSum(total=nums1[lt]+nums2[rt+1], lt=lt, rt=rt+1)
            )
    else:
        return pairs

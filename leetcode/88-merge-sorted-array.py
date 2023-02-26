"""88. Merge Sorted Array

https://leetcode.com/problems/merge-sorted-array

Solution
--------
Have 3 pointers

nums1 = [1,2,3,0,0,0]
         0 1 2 3 4 5
nums2 = [2, 5, 6]
         0  1  2

p1 = 2
p2 = 2
a = nums2
p1 p2 p a[p1] a[p2] a
--------------------------
2  2  5   3     6   [1,2,3,0,0,6]
2  1  4   3     5   [1,2,3,0,5,6]
2  0  3   3     2   [1,2,3,3,5,6]
1  0  2   2     2   [1,2,2,3,5,6]
0  0  1   1     2   [1,2,2,3,5,6]
0  -1 0   1     -  

nums1[:0]=nums2[:0]
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2, p = m-1, n-1, m+n-1
        while p1 >= 0 and  p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1 
            p -= 1
        # copy over the remaining element, we don't need to copy
        # over the remaining if it existed in p1, only p2. And the
        # elements we need to copy over is [0, p2] inclusive.
        nums1[:p2+1] = nums2[:p2+1]

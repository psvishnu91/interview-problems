"""88. Merge Sorted Array

https://leetcode.com/problems/merge-sorted-array
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        nums1=[1,2,3,0,0,0]
               0 1 2 3 4 5
        nums2=[2,5,6]
               0 1 2
        m=3 n=3
        p1, p2, pout = m-1,n-1, m+n-1

        p1 p2  p  nums1
        =============
        2   2  5  [1,2,3,0,0,0]
        2   1  4  [1,2,3,0,0,6]
        2   0  3  [1,2,3,0,5,6]
        1   0  2  [1,2,3,3,5,6]
        1   -1 1  [1,2,2,3,5,6]
        """
        p1, p2, pout = m-1, n-1, m+n-1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[pout] = nums1[p1]
                p1 -= 1
            else:
                nums1[pout] = nums2[p2]
                p2 -= 1
            pout -= 1
        while p1 >= 0:
            nums1[pout] = nums1[p1]
            pout -= 1
            p1 -= 1
        while p2 >= 0:
            nums1[pout] = nums2[p2]
            pout -= 1
            p2 -= 1

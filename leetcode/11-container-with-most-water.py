"""11. Container With Most Water

https://leetcode.com/problems/container-with-most-water/

[1,8,6,2,5,4,8,3,7]
 0 1 2 3 4 5 6 7 8

Brute force will be double for loop
-----------------------------------
 T-O(n^2)  S- O(1)

keep track of a var max_area
for each height find the last height that is at least this
 height to right.
    max_area = max(max_area, min(nums[i], nums[j])* (i-j))

Optimal solution Two pointer O(n)
---------------------------------
Have a left pointer at the left most position and the right
pointer at the rightmost position. Move the smaller of the two
pointers because this is the maximum area the smaller of the 
two heights cna generate. 

Termination conditions is when left and right are at the same
position.
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        lt, rt, max_area = 0, n-1, 0
        while lt != rt:
            max_area = max(max_area, (rt-lt) * min(height[lt], height[rt]))
            if height[lt] < height[rt]:
                lt += 1
            else:
                rt -= 1
        return max_area


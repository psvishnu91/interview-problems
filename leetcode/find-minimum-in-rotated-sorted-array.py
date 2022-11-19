"""https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Solution:

- Idea is to use iterative binary search
- Always keep track of the min_num = float('inf')
- find pivot point
    - we can be in two sides of the rotated array higher side or lower side
    [4,5,6,7,0,1,2] higher 4-7, lower 0-2
    - if a[mid] >= a[lt] and a[mid] >= a[rt]: 
        # higher side (lt side)
        lt = mid + 1
      elif a[mid] <= a[lt] and a[mid] <= a[rt]:
        # lower side (rt side)
            rt = mid - 1
        min_num = min(min_num, a[mid])

Test
=====

4 5 6 7 0 1 2
0 1 2 3 4 5 6

lt  rt  mid a[lt]   a[rt]   a[mid]   min_num
--------------------------------------------
0    6   3   4       2         7        7
4    6   5   0       2         1        1
4    4   4   0       0         0        0
5    4 

Edge case:

unit length array

-1
 0

lt  rt  mid a[lt]   a[rt]   a[mid]   min_num
--------------------------------------------
0    0   0   -1      -1        -1        -1
1    0 
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return find_min(a=nums)
  
    
def find_min(a: List[int]) -> int:
    lt, rt = 0, len(a) - 1
    min_val = float('inf')
    while lt <= rt:
        mid = (lt + rt) // 2
        if a[mid] >= a[lt] and a[mid] >= a[rt]:
            # Higher side: [4,5,6,7,0,1,2]  4-7
            lt = mid + 1
        else:
            # Lower side: [4,5,6,7,0,1,2]  0-2
            rt = mid - 1
        min_val = min(min_val, a[mid])
    return min_val

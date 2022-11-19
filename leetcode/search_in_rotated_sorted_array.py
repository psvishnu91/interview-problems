"""33. Search in Rotated Sorted Array


https://leetcode.com/problems/search-in-rotated-sorted-array/

Solution
=========
"I first found the pivot. Then I searched on lt or rt side of 
the pivot based on where the tgt belonged.


Two pass
Finding the pivot is not trivial. Say we are looking at this array
[4,5,6,7,0,1,2], mid can be in either half of the array.
In left, Look right: if a[mid] >= a[lt] and a[mid] >=rt (btw 4, 7), 
then we check if next number is smaller (we could be at seven 
if so return the next ix pointing to zero, if not look for the pivot 
on the rt side of the array)
In right, look left: if a[mid] <= a[lt] and a[rt], (btw 0,1,2); then 
check if prev number larger (we could be at 0 if so return mid), otherwise
look for the pivot on the left side of the array.

Single pass binary search

just watch neetcode"


Problem solving - finding pivot
==============================

# find pivot (first element)
# check equality
if a[lt] <= a[mid] >= a[rt]:
    if a[mid] > a[mid+1]:
        return mid + 1
    else:
        rec_rt()
elif a[lt] >= mid and a[rt] <=mid:
    if a[mid] < a[mid-1]:
        return mid
    else:
        rec_lt()

2,3,4,7,0,1
0 1 2 3 4 5
pvt = 3

lt   rt   mid    nums[mid] nums[lt]  nums[rt]
==============================================
0     5     2     4            2        1
3     5     4     0            2        1

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return _search(nums=nums, tgt=target)
        
        

def _search(nums, tgt):
    n = len(nums)
    if n == 1:
        return 0 if nums[0] == tgt else - 1
    pivot = _find_pivot(nums=nums) 
    if pivot == 0:
        return _bin_search(nums, tgt=tgt, lt=0, rt=n-1)
    elif nums[0] <= tgt <= nums[pivot-1]: 
        return _bin_search(nums, tgt=tgt, lt=0, rt=pivot-1)
    else:
        return _bin_search(nums, tgt=tgt, lt=pivot, rt=n-1)
    

def _find_pivot(nums) -> int:
    if nums[0] < nums[-1]:
        return 0
    lt, rt = 0, len(nums) - 1
    while lt <= rt:
        mid = (lt + rt) // 2
        if nums[mid] >= nums[lt] and nums[mid] >= nums[rt]:
            # [4,5,6,7,0,1,2], we are somewhere btw 4 and 7
            if nums[mid] > nums[mid + 1]:
                # we are at 7 above return pos of 0
                return mid + 1
            else:
                lt = mid + 1
        elif nums[mid] <= nums[lt] and nums[mid] <= nums[rt]:
            # [4,5,6,7,0,1,2], we are somewhere btw 0 and 2
            if nums[mid] < nums[mid-1]:
                # this is being at 0
                return mid
            else:
                rt = mid - 1
    raise RuntimeError("Should never happen")
            
        
        
def _bin_search(nums, tgt, lt, rt):
    while lt <= rt:
        mid = (lt + rt) // 2
        if nums[mid] == tgt:
            return mid
        elif nums[mid] < tgt:
            lt = mid + 1
        else:
            rt = mid - 1
    else:
        return -1
        

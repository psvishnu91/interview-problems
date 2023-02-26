"""81. Search in Rotated Sorted Array II


https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

Solution:
This is like rotated array but with duplicate elements.

There are several cases to handle:

* Idea is to find which side the pivot is, on the other side it has 
 be ascending, then we check if value is within ascending side, if so,
 we recurse that side, if not we recurse on the side with the pivot.

* We can check which side the pivot is on by checking if nums[0] 
 and nums[mid]. If nums[0] < nums[mid], pivot is on the right side 
 and left side is increasing, if nums[0]>  nums[mid], then pivot is
 on left side, and right side is increasing.

* GOTCHA: duplicate numbers (think about all numbers are same case
 and a case like 2 2 2 0 2 2 2 2 2), where we are looking for 0. 
 There are 3 cases here if nums[0] == nums[mid] == nums[n-1], recurse
 both sides, else nums[0]==nums[mid] (then all nums on left are same),
 recurse right, if nums[mid]==nums[n-1], then all nums on right are
 same, recurse on left."
"""
import functools


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return bsearch_rec(lt=0, rt=len(nums)-1, nums=nums, target=target)
    

def bsearch_rec(lt, rt, nums, target):
    if lt > rt:
        return False
    n = len(nums)
    mid = (lt + rt) // 2
    rec = functools.partial(bsearch_rec, nums=nums, target=target)
    if nums[mid] == target:
        return True
    elif nums[0] == nums[mid] == nums[n-1]:
        # recurse both sides
        return rec(lt=lt, rt=mid-1) or rec(lt=mid+1, rt=rt)
    elif nums[0] == nums[mid]:
        # recurse right side
        return rec(lt=mid+1, rt=rt)
    elif nums[mid] == nums[n-1]:
        # recurse left
        return rec(lt=lt, rt=mid-1)
    elif nums[mid] < nums[0]:
        # pivot on left, right side is increasing
        if nums[mid] < target <= nums[n-1]:
            # recurse right
            return rec(lt=mid+1, rt=rt)
        else:
            # recurse left
            return rec(lt=lt, rt=mid-1)
    elif nums[mid] > nums[0]:
        # pivot on right, left side is increasing
        if nums[0] <= target < nums[mid]:
            # rec left
            return rec(lt=lt, rt=mid-1)
        else:
            # rec right
            return rec(lt=mid+1, rt=rt)
    else:
        raise RuntimeError("Should not happen")

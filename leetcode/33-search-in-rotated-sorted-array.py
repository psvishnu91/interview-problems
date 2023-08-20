"""33. Search in Rotated Sorted Array

https://leetcode.com/problems/search-in-rotated-sorted-array/

Find pivot, binary search both sides
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        pvt_ix = find_pivot(nums=nums, target=target)
        pvt = nums[pvt_ix]
        if target == pvt:
            return pvt_ix
        lt_val = bsearch(nums=nums, lt=0, rt=pvt_ix-1, target=target)
        if lt_val != -1:
            return lt_val
        return bsearch(nums=nums, lt=pvt_ix+1, rt=len(nums)-1, target=target)


def bsearch(nums, lt, rt, target):
    while lt <= rt:
        mid = (lt + rt) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            rt = mid - 1
        else:
            lt = mid + 1
    else:
        return -1


def find_pivot(nums, target):
    """Find pivot which is the min element.

    If the number is greater than the last element
    then we are in the left subarray (higher subarray)
    we move right, else we move left.

    4,5,6,7,0,1,2
    0 1 2 3 4 5 6

    l r m nm 
    =======================
    0 6 3 7
    4 6 5 1 
    4 4 4 0
    4 3
    """
    lt, rt = 0, len(nums) - 1
    while lt <= rt:
        mid = (lt + rt) // 2
        if nums[mid] > nums[-1]:
            lt = mid + 1
        else:
            rt = mid - 1
    return lt

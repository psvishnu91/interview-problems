"""137. Single Number II

https://leetcode.com/problems/single-number-ii/

Three solutions
1. counter
2. sort
3. use bit manipulation to identify each set bit of loner
    by taking % 3
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return bit_cnt(nums)

def bit_cnt(nums):
    lone = 0
    for shift in range(32):
        mask = 1 << shift
        cnt = 0
        for num in nums:
            cnt += bool(num & mask)
        if cnt % 3:
            lone |= mask
    # To make python understand that 32 bit is sign bit.
    if lone >= (1 << 31):
        lone = lone - (1 << 32)
    return lone


def sorting(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    nums.sort()
    # Edge cases smallest and largest num are unique
    if nums[0] != nums[1]:
        return nums[0]
    if nums[-1] != nums[-2]:
        return nums[-1]
    for i in range(1,n-1):
        if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
            return nums[i]


def counter_soln(nums):
    # Because there are at most 10^4+1 unique numbers in
    # nums, nums.length = 3*10^4, we could consider 10^4 as
    # constant space.
    cnts = collections.Counter(nums)
    for num, cnt in cnts.items():
        if cnt == 1:
            return num

"""209. Minimum Size Subarray Sum

https://leetcode.com/problems/minimum-size-subarray-sum/

Solution 1 | T-O(n logn) | binary search through subarray size
--------------------------------------------------------------
lt_sz = 0, rt_sz = n
sz = (lt_sz + rt_sz)//2
if check_any_solution(ps, sz):
    rt_sz = sz - 1
else:
    lt_sz = sz + 1

Solution 2 | T-O(n) | Sliding window
------------------------------------
expand rt until total >= target, move lt until total is smaller than 
target and then expand rt again. We know that moving left has to reduce
total sum.
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        return msa_sliding_window(target, nums)

##################################
# Sliding window
##################################
def msa_sliding_window(target, nums):
    n = len(nums)
    lt, rt = 0, 0
    total = 0
    smallest_win = float('inf')
    while rt < n:
        total += nums[rt]
        while total >= target:
            smallest_win = min(smallest_win, rt-lt+1)
            total -= nums[lt]
            lt += 1
        rt += 1
    return 0 if smallest_win == float('inf') else smallest_win

##################################
# BINARY SEARCH OVER SIZE
##################################

def msa_binsearch(target, nums):
    n = len(nums)
    lt_sz, rt_sz = 1, n
    smallest_win_sz = float('inf')
    prefix_sum = _build_prefix_sum(nums=nums)
    # print("lt_sz\trt_sz\tsz\tsmallest_win_sz")
    while lt_sz <= rt_sz:
        sz = (lt_sz + rt_sz) // 2
        # print(f"{lt_sz}\t\t{rt_sz}\t\t{sz}\t\t{smallest_win_sz}")
        if _has_solution(
            nums=nums,
            ps=prefix_sum,
            target=target,
            win_sz=sz,
        ):
            # if this window size has a solution, try a smaller window size
            rt_sz = sz - 1
            smallest_win_sz = min(smallest_win_sz, sz)
        else:
            # this window size has no solution, let's try a larger window size
            lt_sz = sz + 1
    return 0 if smallest_win_sz == float('inf') else smallest_win_sz


def _build_prefix_sum(nums):
    n = len(nums)
    ps = [None] * n
    rs = 0
    for i, num in enumerate(nums):
        rs += num
        ps[i] = rs
    return ps


def _has_solution(nums, ps, target, win_sz):
    """
    n= 5, ws=3
        0 1 2 3 4
    ps  0 1 3 6 10
    ps[2]-ps[0]+nums[0]=>3-0+0=3
    ps[3]-ps[1]+nums[1]=>6-1+1=6
    ps[4]-ps[2]+nums[2]=>10-3+2=9
    """
    n = len(nums)
    for ix in range(n-win_sz+1):
        win_sum = ps[ix+win_sz-1]-ps[ix]+nums[ix]
        if win_sum >= target:
            return True
    else:
        return False

"""228. Summary Ranges

https://leetcode.com/problems/summary-ranges/

Edge cases
----------
empty array
single entry array
same number array
array with both ranges and single element range

 [0,1,2,4,5,7]
  0 1 2 3 4 5

s p c ranges
0 0 1 []
0 1 2
0 2 4 ["0->2"]
4 4 5 
4 5 7 ["0->2", "4->5"]
7
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        return _summary(nums)


def _summary(nums):
    n = len(nums)
    if not nums:
        return []
    if n == 1:
        return [str(nums[0])]
    st_val = nums[0]
    ranges = []
    for prev, cur in zip(nums[:-1], nums[1:]):
        if prev + 1 == cur:
            # in range
            continue
        _add_range(ranges=ranges, st_val=st_val, prev=prev)
        st_val = cur
    _add_range(ranges=ranges, st_val=st_val, prev=nums[-1])
    return ranges

def _add_range(ranges, st_val, prev):
    # end of a range
    if prev == st_val:
        # single value range
        ranges.append(str(st_val))
    else:
        # range of cardinality > 1
        ranges.append(f"{st_val}->{prev}")

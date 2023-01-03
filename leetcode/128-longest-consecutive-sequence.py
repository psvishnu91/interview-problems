"""128. Longest Consecutive Sequence

https://leetcode.com/problems/longest-consecutive-sequence/

Solutions
1. Brute force, sort sliding window
2. Solution: Disjoint union set
    - create a set of inputs
    - DUS with all numbers
    - Iterate over numbers, check if +1, -1 neightbours exist in set, if so 
    attach them in the DUS.
    - DUS when you union keeps track of max size.

    Max size from DUS
3. Solution: Check if smallest num in consec sequence and iteratively check.

    IDEA: If we find next nums in set of nums we could simply keep track of max sz.
    The problem with this approach is that we might be re-searching from the
    middle of the sequence over and over again. 

    Iterate over set of nums, if num-1 not in set, iterate over all elements
    num+curlen in set. update max sz.
"""
class DUS:

    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1]*n
        self.max_sz = 1

    def leader(self, x):
        if x == self.parents[x]:
            return x
        self.parents[x] = self.leader(x=self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        xlead = self.leader(x=x)
        ylead = self.leader(x=y)
        if xlead == ylead:
            return
        if self.sizes[xlead] >= self.sizes[ylead]:
            self.parents[ylead] = xlead
            self.sizes[xlead] += self.sizes[ylead]
            self.max_sz = max(self.sizes[xlead], self.max_sz)
        else:
            # ylead bigger
            self.parents[xlead] = ylead
            self.sizes[ylead] += self.sizes[xlead]
            self.max_sz = max(self.sizes[ylead], self.max_sz)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return _longest_simple(nums)

def _longest_dus(nums):
    if not nums:
        return 0
    nums_ix_map = {num: i for i, num in enumerate(set(nums))}
    n = len(nums_ix_map)
    dus = DUS(n=n)
    for num, ix in nums_ix_map.items():
        for nb in [num-1, num+1]:
            if nb not in nums_ix_map:
                continue
            dus.union(x=ix, y=nums_ix_map[nb])
    return dus.max_sz


def _longest_simple(nums):
    nums = set(nums)
    maxsz = 0
    for num in nums:
        # ensure we only begin at the smallest num
        if num-1 in nums:
            continue
        curlen = 1
        while num + curlen in nums:
            curlen += 1
        maxsz = max(curlen, maxsz)
    return maxsz

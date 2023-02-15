"""435. Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/

Solution, sort and iterate left to right
-----------------------------------------
T-O(nlogn) S-O(n) for sorted output array

Main idea: Once sorted, if the next intval st >= prev_end
we are all good. We don't have to remove anything, we just move
on. If st < prev_end, then these two intervals overlap. But which
one should we remove, it make sense to remove the one with the
smaller end, so we update num_rmv and update prev_end to
min(prev_end, end).
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        [[1,2], [1,3], [2,3], [3,4]]
        prev_end, st, end, num_rem
        2          1   3        1
        2          2   3        1
        3          3   4        1
        4

        [[1,2],[1,2],[1,2]]

        prev_end, st, end, num_rem
        2          1    2     1
        2          1    2     2
        """
        intvals = sorted(intervals)
        prev_end = intvals[0][1]
        num_rmv = 0
        for st, end in intvals[1:]:
            if st < prev_end:
                num_rmv += 1
                prev_end = min(prev_end, end)
            else:
                prev_end = end
        return num_rmv

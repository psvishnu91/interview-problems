"""57. Insert Interval

https://leetcode.com/problems/insert-interval/

Simplest solution
-----------------
Insert in the proper location - O(log n) operation with bisect, insort
Then iterate and merge intervals

edge cases
----------
empty list
needs to added to the beg, to the end

"""
import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intval = newInterval
        if not intervals:
            return [new_intval]
        # insert in proper location
        # can also be implemented manually using _insort()
        # bisect is faster as it's written in C
        bisect.insort(a=intervals, x=new_intval)  # OR _insort(a=intervals, x=new_intval)
        # fix the intervals which are already sorted
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            last_end = merged[-1][1]
            if start <= last_end:
                # same interval, potentially update end
                merged[-1][1] = max(last_end, end)
            else:
                # new interval
                merged.append([start, end])
        return merged


def _insort(a, x):
    n = len(a)
    lt, rt = 0, n - 1
    while lt <= rt:
        mid = (lt + rt) // 2
        if a[mid] == x:
            rt = mid
            break
        elif a[mid] > x:
            rt = mid - 1
        else:
            # a[mid] < x:
            lt = mid + 1
    a.insert(rt+1, x)
    return a

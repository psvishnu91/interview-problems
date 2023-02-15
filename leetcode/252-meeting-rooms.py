"""252. Meeting Rooms

https://leetcode.com/problems/meeting-rooms/

Sort and check if arrays are overlapping T-O(nlogn) M-O(n)
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intvals = sorted(intervals)
        prev_end = intvals[0][1]
        for st, end in intvals[1:]:
            if st < prev_end:
                return False
            else:
                prev_end = end
        else:
            return True

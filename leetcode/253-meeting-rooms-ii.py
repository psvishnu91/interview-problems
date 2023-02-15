"""253. Meeting Rooms II

https://leetcode.com/problems/meeting-rooms-ii/

Solution - Use a heap for end times.
------------------------------------------
- sort the intervals
- create a heap for the end times
- keep track of max(rooms, len(heap))
- iterate over intervals
- if heap is empty add simply add the end time and update `rooms`
- else: pop all ends that are smaller than or equal to cur start, add cur
    end. update `rooms`.

The idea here is that when we move into the next meeting we need
to know the first meeting to end (to see if this room can take its spot).
We need to keep track of a running count of overlapping meetings.
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intvals_sorted = sorted(intervals)
        end_heap = [intvals_sorted[0][1]]
        rooms = 1
        for st, end in intvals_sorted[1:]:
            while end_heap and end_heap[0] <= st:
                heapq.heappop(end_heap)
            heapq.heappush(end_heap, end)
            rooms = max(rooms, len(end_heap))
        return rooms

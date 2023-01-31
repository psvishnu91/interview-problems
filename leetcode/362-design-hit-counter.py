"""362. Design Hit Counter

https://leetcode.com/problems/design-hit-counter/

We want the hit function to be fast and the getHits function to be slower.
More hits than getHits. So we create a python deque Q and then a linkedlist
Node(ts, cnt). 
"""
from collections import deque
import dataclasses

WINDOW = 300

@dataclasses.dataclass
class TsCountNode:
    ts: int
    cnt: int


class HitCounter:

    def __init__(self, window=WINDOW):
        self.q = deque()
        self.total = 0
        self.window = window

    def hit(self, timestamp: int) -> None:
        self.total += 1
        if self.q and self.q[-1].ts == timestamp:
            self.q[-1].cnt += 1
        else:
            self.q.append(TsCountNode(ts=timestamp, cnt=1))

    def getHits(self, timestamp: int) -> int:
        # We need to remove all nodes window distance in the past.
        # if window=4, ts=9, we want to keep 6,7,8,9, remove_ts <= 5 (9-4)
        remove_ts = timestamp - self.window
        while self.q and self.q[0].ts <= remove_ts:
            self.total -= self.q[0].cnt
            self.q.popleft()
        return self.total
            
"""
Testing
========
Simplify let's say we want last 3 seconds

ts-1 to index

Keep a queue of (timestamp, count)

input = [1,1,1,3,3,5,5,6,100]
getcnt= [1,2,3,4,5,3,4,3,1  ,0]
                            200

input       q        
-----------------------------
1        [(t=1,c=1)]
1        [(t=1,c=2)]
1        [(t=1,c=3)]
3        [(t=1,c=3),(t=3,c=1)]                   # check if the head timestamp is more than 3 away, if so we need to trim the head
3        [(t=1,c=3),(t=3,c=2)]
5        [(t=1,c=3),(t=3,c=2)]                   # (head.ts-new_ts)=> d=4 >=win(3), remove all ts <= new_ts(5)-win(3)=2
        [(t=3,c=2),(t=5,c=1)]
5       [(t=3,c=2),(t=5,c=2)]
6       [(t=3,c=2),(t=5,c=2)]
        [(t=5,c=2),(t=6,c=2)] # d=6-3>=win(3), remove all ts <= 3 (new_ts-win)
100     [(t=100,c=1)]
200     []
"""

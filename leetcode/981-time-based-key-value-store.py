"""981. Time Based Key-Value Store

https://leetcode.com/problems/time-based-key-value-store/
"""

import sortedcontainers as sc

class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            self.time_map[key][timestamp] = value
        else:
            self.time_map[key] = sc.SortedDict({timestamp: value})

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        sorted_dict = self.time_map[key]
        if timestamp in sorted_dict:
            return sorted_dict[timestamp]
        else:
            # We bisect left and just want to return the previous
            # element here. The only catch is if the number is smaller
            # than the smallest timestamp, we should return an empty string
            # when we bisect left and get position as 0, then we should return
            # empty string because, if the ts at 0 matched we would have returned
            # already.
            possible_ix = sorted_dict.bisect_left(timestamp)
            if possible_ix == 0:
                return ""
            else:
                return sorted_dict.peekitem(possible_ix-1)[1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

"""347. Top K Frequent Elements

https://leetcode.com/problems/top-k-frequent-elements
"""
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_cnts = Counter(nums)
        heap = []
        for num, cnts in num_cnts.items():
            if len(heap) < k:
                heapq.heappush(heap, (cnts, num))
            elif heap[0][0] < cnts:
                # the k-th smallest in heap is smaller than this nums
                # count, replace with this num
                heapq.heappop(heap)
                heapq.heappush(heap, (cnts, num))
            # else, the heap is full and this count is smaller do nothing
        return [num for _, num in heap] 

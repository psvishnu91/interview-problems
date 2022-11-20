"""162. Find Peak Element

https://leetcode.com/problems/find-peak-element

Algo
- if a[mid-1] > a[mid]: recurse left
- elif a[mid+1] > a[mid]: recurse rt
- else: return mid

Why does this work?
- if a[mid-1] > a[mid]: recurse left
What are the cases:
say mid=4, mid-1=3, mid-2=2
now wkt a[3] > a[4]
either the left half is ascending in which case 3 is the peak
else left half is decreasing in which case the first element is the peak
the only gotcha would have been if all of a[1:3] = a[3], but this is not
possible because a[i] != a[i+1] as a constraint

Edge cases:
- Unit array

Tests
[1]
lt rt mid a[lt] a[rt] a[mid] _prev _next
=========================================
0  0   0   1     1     1      -inf   -inf

"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return find_peak(a=nums)

    
def find_peak(a: List[int]) -> int:
    n = len(a)
    lt, rt = 0, n-1
    while lt <= rt:
        mid = (lt + rt) // 2
        _prev = a[mid-1] if mid > 0 else -float('inf')
        _next = a[mid+1] if mid <= n-2 else -float('inf')
        if _prev > a[mid]:
            rt = mid - 1
        elif _next > a[mid]:
            lt = mid + 1
        else:
            return mid
    raise RuntimeError("Should never happen if there exists a peak")

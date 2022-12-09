"""42. Trapping Rain Water

https://leetcode.com/problems/trapping-rain-water/

- For each element we want to know max ht from left
    mx height from rt. Water stored here is 
    max(min(lt_mx[i], rt_mx[i])-hts[i], 0).
- We do one pass rt to left to keep track of max ht so far.
- We keep running max lt to right and keep adding water
    trapped using above formula as we go lt to right.
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        return _trap(hts=height)

def _trap(hts: list[int]) -> int:
    # cumulative max height from right end
    right_max = _build_rt_max_hts(hts=hts)
    # running max height from lt
    lt_mx = 0
    trapped = 0
    for ht, rt_mx in zip(hts, right_max):
        lt_mx = max(ht, lt_mx)
        mx_ht = min(lt_mx, rt_mx)
        trapped += mx_ht - min(mx_ht, ht)
    return trapped


def _build_rt_max_hts(hts):
    n = len(hts)
    window = [None] * n
    mx_ht = 0
    for i in range(n-1, -1, -1):
        mx_ht = max(hts[i], mx_ht)
        window[i] = mx_ht
    return window
        

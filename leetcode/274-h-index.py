"""274. H-Index

https://leetcode.com/problems/h-index

Algorithm: Sorting
--------–---------
- h index is the max number where the author has at least
    h papers of cited at least h times
- So let's sort the citations and
    * start with the paper with the maximum citations at the end.
        if this paper has 
        - citations[-1] == 0: then h-index has to be zero
            no papers have any citations
        - citations[-1] == 1: **h is exactly 1** 
            then highest num citations is
            1 and there's at least one paper with it, so
            h=1 (cannot be more). If h was higher
            say 2, then max citns, ie., citations[-1] needs
            to be at least 2.
        - citations[-1] > 1: h is at least 1, but possibly higher
    * next we go to index -2, if citations[-2]>=2 then there is
        at least 2 papers with citations>=2, so h is updated to 2
    * we keep going from the back and if citations[-i] >= i then
        h = i (at least i)
    * if we encounter a scenario where the invariant is broken
        say citations[-4] = 3, then there isn't 4 papers with
        at least 4 citations, h can be at most 3 and we break
        the loop.

Rough work
----------
arr     0 1 3 5 5 5 6
ix      0 1 2 3 4 5 6
ix + 1  1 2 3 4 5 6 7
        7 6 5 4 3 2 1
n = 7
ix = n - i
if c[ix] >= ix:
    h = max(h, ix)
i   ix   h
6    1   1
     2   2
     3   3
     4   4
     5   

3 0 6 1 5

c 0 1 3 5 6
i 0 1 2 3 4

n=5
ix, i, citns[i], h
-------------------
1   4   6        1
2   3   5        2
3   2   3        3
4   1   1 
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citns = sorted(citations)
        n = len(citns)
        h = 0
        for ix in range(1, n+1):
            if citns[-ix] < ix:
                break
            h = ix
        return h

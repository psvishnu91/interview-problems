"""97. Interleaving String

https://leetcode.com/problems/interleaving-string/

DP - DFS and cache, T-S-O(m x n)
We can also build the DP table but it's way more confusing imo.
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return  is_interleave(s1, s2, s3)

def is_interleave(s1, s2, s3):
    n1, n2, n3 = len(s1), len(s2), len(s3)
    if n1 + n2 != n3:
        return False
    return rec(
        p1=0,
        p2=0,
        p3=0,
        s1=s1,
        s2=s2,
        s3=s3,
        cache=[[None]*(n2+1) for _ in range(n1+1)]
    )



def rec(p1, p2, p3, s1, s2, s3, cache) -> bool:
    n1, n2, n3 = len(s1), len(s2), len(s3)
    # We've reached the end of the string
    if p3 == n3:
        return True
    # One of the strings has ended
    if cache[p1][p2] is not None:
        return cache[p1][p2]
    elif p1 == n1:
        cache[p1][p2] = s2[p2:] == s3[p3:]
        return cache[p1][p2]
    elif p2 == n2:
        cache[p1][p2] = s1[p1:] == s3[p3:]
        return cache[p1][p2]
    # We are in middle of both strings, recurse on both
    # potential options
    c1, c2, c3 = s1[p1], s2[p2], s3[p3]
    if c3 != c1 and c3 != c2:
        cache[p1][p2] = False
    else:
        kwargs = dict(p3=p3+1, s1=s1, s2=s2, s3=s3, cache=cache)
        if c3 == c1 and rec(p1=p1+1, p2=p2, **kwargs):
            cache[p1][p2] = True
        elif c3 == c2 and rec(p1=p1, p2=p2+1, **kwargs):
            cache[p1][p2] = True
        else:
            cache[p1][p2] = False
    return cache[p1][p2]

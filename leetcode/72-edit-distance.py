"""72. Edit Distance

https://leetcode.com/problems/edit-distance/


Solution top-down DP | T - S - O(MN)
------------------------------------
Scenarios
1. termination if p1 or p2 is at the end, then the other
    other strings remaining chars need to be deleted
3. c1 == c2:
    p1 += 1, p2 += 1
    move on
   c1 != c2:
    delete c1, p1 += 1
    replace c1 w c2, p1 += 1, p2 += 1
    insert c2, p2 += 1

"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return md_dp(word1=word1, word2=word2)


def md_dp(word1, word2):
    n1, n2 = len(word1), len(word2)
    cache = [[None]*n2 for _ in range(n1)]
    return _dfs_dp(
        p1=0,
        p2=0,
        word1=word1,
        word2=word2,
        cache=cache,
    )


def _dfs_dp(p1, p2, word1, word2, cache):
    """
            horse
            /        |         \
           orse     rorse       rhose
        /  |    \
      rse  rrse 
    """
    if p2 == len(word2):
        # delete the requisite chars
        return len(word1) - p1
    if p1 == len(word1):
        # insert all the requisite chars
        return len(word2) - p2
    if cache[p1][p2] is not None:
        return cache[p1][p2]
    c1, c2 = word1[p1], word2[p2]
    _kwargs = dict(
        word1=word1,
        word2=word2,
        cache=cache,
    )
    if c1 == c2:
        dist = _dfs_dp(p1=p1+1, p2=p2+1, **_kwargs)
    else:
        dist = 1 + min(
            # deletion
            _dfs_dp(p1=p1+1, p2=p2, **_kwargs),
            # replacement
            _dfs_dp(p1=p1+1, p2=p2+1, **_kwargs),
            # insertion
            _dfs_dp(p1=p1, p2=p2+1, **_kwargs),
        )
    cache[p1][p2] = dist
    return dist

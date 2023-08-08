"""392. Is Subsequence

https://leetcode.com/problems/is-subsequence

Solution:
Iterate over chars in t. Have a pointer on s.
If s[p] == t, increment p, If p ==len(s) return true

Edge cases:
1. s is empty
2. t is empty
3. nominal
4. same word
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        ix_s, slen = 0, len(s)
        for c in t:
            if c != s[ix_s]:
                continue
            ix_s += 1
            if ix_s == slen:
                return True
        else:
            return False

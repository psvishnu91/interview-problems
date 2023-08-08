"""125. Valid Palindrome

https://leetcode.com/problems/valid-palindrome

Rough
-----
a b a
0 1 2
l   r

a b b a
0 1 2 3
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # given below is two ptr approach
        lt, rt = 0, len(s) - 1
        s = s.lower()
        while lt < rt:
            c_lt, c_rt = s[lt], s[rt]
            if not c_lt.isalnum():
                lt += 1
                continue
            if not c_rt.isalnum():
                rt -= 1
                continue
            if s[lt] != s[rt]:
                return False
            lt += 1
            rt -= 1
        else:
            return True

"""58. Length of Last Word

https://leetcode.com/problems/length-of-last-word
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        maxlen = 0
        seen_char = False
        for i in range(n-1, -1, -1):
            if s[i] == " " and seen_char:
                break
            elif s[i] == " ":
                continue
            else:
                maxlen += 1
                seen_char = True
        return maxlen

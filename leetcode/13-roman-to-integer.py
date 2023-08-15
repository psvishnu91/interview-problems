"""13. Roman to Integer

https://leetcode.com/problems/roman-to-integer

Iterate lt to rt adding values. If ever val[next_char] > val[cur_char]
then subtract the current value.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        sym2val = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        n = len(s)
        val = sym2val[s[-1]]
        for i,c in enumerate(s[:-1]):
            # if the next character is greater than this character
            # we subtract current value
            this_val = sym2val[c]
            if this_val < sym2val[s[i+1]]:
                val -= this_val
            else:
                val += this_val
        return val

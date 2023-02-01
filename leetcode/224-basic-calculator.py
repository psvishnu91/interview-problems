"""224. Basic Calculator

https://leetcode.com/problems/basic-calculator/
"""
class Solution:
    def calculate(self, s: str) -> int:
        return calc_rec(pos=0, s=s)[0]

def calc_rec(pos, s):
    total, sign = 0, 1
    while pos < len(s):
        c = s[pos]
        if c == " " or c == "+":
            pos += 1
        elif c == "-":
            sign = -1
            pos += 1
        elif c.isnumeric():
            num, pos = _get_number(pos=pos, s=s)
            total += num * sign
            sign = 1
        elif s[pos] == "(":
            num, pos = calc_rec(pos+1, s)
            total += num * sign
            sign = 1
        elif s[pos] == ")":
            pos += 1
            break
        else:
            raise ValueError("Unknown char")
    return total, pos


def _get_number(pos, s):
    num_chars = []
    while pos < len(s) and s[pos].isnumeric():
        num_chars.append(s[pos])
        pos += 1
    return int("".join(num_chars)), pos

"""20. Valid Parentheses

https://leetcode.com/problems/valid-parentheses/

"Hashmap = {'(': ')', '{': '}', '[': ']'}. Iterate over chars of str,
if in hashmap they are lt parens, add to stk, c if is map[stk.pop()].

Edge case: ')'. Stk.pop will fail as it will be empty."
"""
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close_map = {op: end for op, end in ["{}", "[]", "()"]}
        close_to_open_map = {end: op for op, end in open_to_close_map.items()}
        stk = []
        for char in s:
            if char in open_to_close_map:
                # it's an opening character
                stk.append(char)
            elif not stk or close_to_open_map[char] != stk[-1]:
                return False
            else:
                stk.pop()
        return not bool(stk)

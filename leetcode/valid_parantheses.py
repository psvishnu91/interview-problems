"""20. Valid Parentheses

https://leetcode.com/problems/valid-parentheses/

"Hashmap = {'(': ')', '{': '}', '[': ']'}. Iterate over chars of str, 
if in hashmap they are lt parens, add to stk, c if is map[stk.pop()]. 

Edge case: ')'. Stk.pop will fail as it will be empty."
"""
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        lt_to_rt_map = {'(': ')', '{': '}', '[': ']'}
        stk = deque()
        for c in s:
            if c in lt_to_rt_map:
                # lt parens
                stk.append(c)
            else:
                # rt parens
                if not stk:
                    return False
                lst_open_paren = stk.pop()
                if c != lt_to_rt_map[lst_open_paren]:
                    return False
        else:
            return not bool(stk)
        

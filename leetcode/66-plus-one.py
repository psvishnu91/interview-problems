"""66. Plus One

https://leetcode.com/problems/plus-one/
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res, carry = [], 1
        for d in reversed(digits):
            added = (d + carry)
            carry = added // 10
            res.append(added % 10)
        if carry:
            res.append(carry)
        return list(reversed(res))

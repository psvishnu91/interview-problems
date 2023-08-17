"""202. Happy Number

https://leetcode.com/problems/happy-number

Scenarios
----------
Cases, n dwindles down to 1: happy case
       cycles to a different number: hashset
       grows to infinity? There's a crazy explanation as to why
        if there's a cycle the number needs to be <= 243

Option 1: hashset and find_next_num
-----------------------------------
Implemented below

Option 2: Assume that we are in a linkedlist and we want to find loops
----------------------------------------------------------------------
Use fast (2 jumps) and slow (1 jump) runner
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}
        while n:
            n = sum(d**2 for d in _digits(n))
            if n in seen:
                break
            seen.add(n)
        return n == 1


def _digits(n):
    while n:
        yield n%10
        n = n//10

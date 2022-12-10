"""278. First Bad Version

https://leetcode.com/problems/first-bad-version/description/

Test
====
# G G G G B B B B B B
# 0 1 2 3 4 5 6 7 8 9
# l=0, r=9, m=4, B
# l=0, r=4, m=2, G
# l=2, r=4, m=3, G
# l=4, r=4, m=3, B
# l=5, r=5, m=5, B
# B B B
# 0 1 2
# l=0,rt=2,m=1
# l=0,rt=1,m=0,
# l=0, rt=0
# B
# l=0,rt=0,m=0
"""


class Solution:
    def firstBadVersion(self, n: int) -> int:
        lt, rt, first_bad = 0, n, n + 1
        while lt <= rt:
            mid = (lt + rt) // 2
            if isBadVersion(mid):
                first_bad = mid
                rt = mid - 1
            else:
                lt = mid + 1
        return first_bad

"""74. Search a 2D Matrix

https://leetcode.com/problems/search-a-2d-matrix/

Input
======
1 2 3
4 5 5
6 6 7
9 9 10

Solution
=========
Two passes.

First binary search over the first element of each row.
Keep track of last_lower row. Always move forward mid+1
and mid-1. Return last_lower. Initiate to 0 for the edge
case that the number might be smaller than mat[0][0].

Once you've found the row, simple binary search.

Problem solving
---------------
vertical bin search

tgt=-1
last_lower = -1

-> mid[mid][0] == tgt: return mid
-> mat[mid][0] < tgt: lt = mid+1, last_lower=mid
-> mat[mid][0] > tgt: rt = mid-1

lt rt mid mat[mid][0]   last_lower
====================================
0   3   1   4               1
2   3   2   6               2
3   3   3   9
3   2

tgt=2
lt rt mid mat[mid][0]   last_lower
==================================
0   3   1   4
0   0   0   1               0
1   0

Then simple binary search for rest
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return _search_mat(mat=matrix, tgt=target)


def _search_mat(mat, tgt) -> bool:
    row = _find_lower_row(mat=mat, tgt=tgt)
    return _bin_search(mat=mat, tgt=tgt, row=row)


def _find_lower_row(mat, tgt) -> int:
    lt, rt = 0, len(mat) - 1
    last_lower_row = 0
    while lt <= rt:
        mid = (lt + rt) // 2
        if mat[mid][0] == tgt:
            last_lower_row = mid
            break
        elif mat[mid][0] < tgt:
            last_lower_row = mid
            lt = mid + 1
        else:
            rt = mid - 1
    return last_lower_row


def _bin_search(mat, tgt, row) -> bool:
    lt, rt = 0, len(mat[0]) - 1
    found = False
    while lt <= rt:
        mid = (lt + rt) // 2
        if mat[row][mid] == tgt:
            found = True
            break
        elif mat[row][mid] < tgt:
            lt = mid + 1
        else:
            rt = mid - 1
    return found

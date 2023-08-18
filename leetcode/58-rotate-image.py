"""48. Rotate Image

https://leetcode.com/problems/rotate-image/

Idea
- Move by rings, first outer ring then inner ring and so on.
- To move all the elements in the outermost ring i=0, j=n-1,i=n-1,j=0,
    we iterate over every element of i except the last one and swap
    say n=5, 0,0 -> 0,4 -> 4,4 -> 4,0 -> 0,0 (4 swaps in total)
- The when we move to the inner ring say i, we do iterate over j btw
    range(i, n-i-1) and then perform the swaps.
- I found expressing the positions to swap to excruciating.

T - O(n^2) S - O(1)
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(i, n - i - 1):
                prev = matrix[i][j]
                for q, r in [
                    (j, n-i-1),  # right
                    (n-i-1, n-j-1), # bottom
                    (n-j-1, i), # left
                    (i, j),  # top
                ]:
                    matrix[q][r], prev = prev, matrix[q][r]

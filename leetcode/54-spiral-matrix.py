"""54. Spiral Matrix

https://leetcode.com/problems/spiral-matrix/

Algorithm
Not impossible but very tricky to get right without debugging

- Outer while loop where we increment ring variable.
- ring implies which matrix ring we are working on rn.
- We move and add elements in the ring to spiral list
    1. lt to rt
    2. then top to bottom
    3. then right to left
    4. and finally bottom to top
- If we reach the numel in original matrix we stop

Exploration
===========
We start at
- row=0, cols[0:n-1]
- col=n-1, rows[1:n-1]
- row=n-1, cols[n-2:0]
- col=0,rows[n-2:1]

- row=1, cols[1:n-2] = [1:n-1-row]  # top
- col=n-2=[n-1-row], rows[2:n-2]=[1+row:n-1-row] # rt
- row=n-2=[n-1-row], cols[n-3:1]=[n-2-row:row] # bot
- col=1=row, rows[n-2:1]=[n-3:2]=[n-2-row:row+1] # lt
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        numel = m * n
        spiral = []
        ring = 0
        while True:
            for dirn in ["l2r", "t2b", "r2l", "b2t"]:
                if dirn == "l2r":
                    spiral.extend(matrix[ring][ring:n-ring])
                elif dirn == "r2l":
                    spiral.extend(reversed(matrix[m-1-ring][ring:n-2-ring+1]))
                elif dirn == "t2b":
                    spiral.extend(matrix[i][n-1-ring] for i in range(ring+1, m-ring))
                else:
                    # b2t
                    spiral.extend(matrix[i][ring] for i in range(m-2-ring, ring, -1))
                print(f"{dirn=}\t{spiral=}")
                if len(spiral) == numel:
                    return spiral
            ring += 1
        else:
            raise RuntimeError("Can't happen")

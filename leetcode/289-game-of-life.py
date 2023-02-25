"""289. Game of Life

https://leetcode.com/problems/game-of-life/

Trick: T-O(mxn) S-O(1)
------ 
Because we need to know what was the previous state while
simultaneously modifying the table, create new state values
that can be decoded later.

For ones:   1=> neigb_sum in {2,3} -> 1 else -> 0
For zeroes: 0=> neigb_sum == 3 -> 1 else -> 0

Mapping
-------
transition    new_cell
0 -> 0 =>       0 
1 -> 0 =>       1
0 -> 1 =>       2
1 -> 1 =>       3

While summing up neighbours:
old_cell = new_cell % 2

While decoding neigbours:
decoded_new_cell = new_cell//2

if cell == 1:
    new_cell = 3 if neigb_sum in {2, 3} else 1
elif cell == 0:
    new_cell = 2 if neigb_sum == 3 else 0
"""

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i, j in itertools.product(range(m), range(n)):
            neib_sum = sumup_neighbours(i=i, j=j, board=board)
            if board[i][j] == 1:
                board[i][j] = 3 if neib_sum in {2, 3} else 1
            else:
                # board[i][j] == 0
                board[i][j] = 2 if neib_sum == 3 else 0
        for i, j in itertools.product(range(m), range(n)):
            board[i][j] //= 2
    

def sumup_neighbours(i, j, board):
    m, n = len(board), len(board[0])
    return -board[i][j] + sum(
        board[adj_i][adj_j]%2
        for adj_i, adj_j in itertools.product((i-1, i, i+1), (j-1, j, j+1))
        if (0 <= adj_i < m) and (0 <= adj_j < n)
    )

"""909. Snakes and Ladders

https://leetcode.com/problems/snakes-and-ladders/

CORRECT SOLUTION BFS
--------------------
Start at 1, and bfs every option. The first time we see
n^2, we know the move number.

INCORRECT SOLUTION DP
---------------------
In DP smaller subproblems should not depend on larger subproblems.

DP is wrong? This is because
 -------
 |     | snake
 v     | 
13 14 15

To find min_dist[13] = we need to min( min_dist[14], min_dist[15]...).
But 15 will point to 13 forming a loop.
"""
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        return snakes_and_ladders(board=board)


def snakes_and_ladders(board):
    n = len(board)
    # BFS
    q, seen, moves = deque([1]), {1}, 0
    while q:
        qlen = len(q)
        for _ in range(qlen):
            pos = q.popleft()
            if pos == n ** 2:
                return moves
            for next_pos in _iter_next_pos(pos=pos, board=board):
                if next_pos in seen:
                    continue
                seen.add(next_pos)
                q.append(next_pos)
        moves += 1
    else:
        return -1


def _iter_next_pos(pos, board):
    n = len(board)
    for next_pos in range(pos + 1, pos + 7):
        if next_pos > n ** 2:
            return
        ni, nj = _bp_to_ij(bp=next_pos, n=n)
        if board[ni][nj] == -1:
            next_pos = _ij_to_bp(i=ni, j=nj, n=n)
        else:
            next_pos = board[ni][nj]
        yield next_pos


def _bp_to_ij(bp, n):
    i = (n - 1) - ((bp - 1) // n)
    _j = (bp - 1) % n
    if ((n - 1) - i) % 2 == 0:
        # even rows from bot where last row is 0
        j = _j
    else:
        # odd rows from bot
        j = (n - 1) - _j
    return (i, j)


def _ij_to_bp(i, j, n):
    """
    n = 4
      0  1  2  3
    0 16 15 14 13
    1 9  10 11 12
    2 8  7  6  5
    3 1  2  3  4

    1,1 -> (3 - 1 ) * 4 + 1 -> 9
        3 - 1 % 2 = 0 -> 10
    2,2 -> (3 - 2) * 4 + 1 -> 5
        3 - 2 % 2 = 1 -> 3-2 -> 5 + 1 => 6
    """
    bp = (n - 1 - i) * n + 1
    if ((n - 1) - i) % 2 == 0:
        # even rows from bot where last row is 0
        bp += j
    else:
        bp += n - 1 - j
    return bp

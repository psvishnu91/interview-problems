"""130. Surrounded Regions

https://leetcode.com/problems/surrounded-regions/

Idea:
- Os at the border and other Os connected to it are safe
- Look at all border cells, when we find O, we will mark it and
    all connected cells as SAFE (through DFS).
- Then we go through board and decode it, if we see O, X -> X
    and SAFE -> O
"""

import itertools

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i, j in itertools.chain(
            itertools.product([0, m-1], range(n)),
            itertools.product(range(m), [0, n-1]),
        ):
            if board[i][j] == 'O':
                _dfs_mark_safe(i=i, j=j, board=board)
        # Decode
        for i, j in itertools.product(range(m), range(n)):
            if board[i][j] == 'SAFE':
                board[i][j] = 'O'
            else:
                board[i][j] = 'X'


def _dfs_mark_safe(i, j, board):
    board[i][j] = 'SAFE'
    for adj_i, adj_j in _get_neibs(i=i, j=j, board=board):
        _dfs_mark_safe(i=adj_i, j=adj_j, board=board)


def _get_neibs(i, j, board):
    m, n = len(board), len(board[0])
    for adj_i, adj_j in [
        (i-1, j),
        (i+1, j),
        (i, j-1),
        (i, j+1),
    ]:
        if (
            (0 <= adj_i < m)
            and (0 <= adj_j < n)
            and board[adj_i][adj_j] == 'O'
        ):
            yield (adj_i, adj_j)

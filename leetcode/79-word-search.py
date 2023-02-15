"""79. Word Search

https://leetcode.com/problems/word-search/

Solution DFS
------------
Find the first character which matches the first
character of the word and then dfs to see if the word
can be constructed. Keep a hashset to ensure you don't
revisit the same node multiple times.

Optimisation: Beats 85% of solutions
-------------------------------------
T-(mn 3^l) where l is the length of the word

Fast exit if all the characters in the target
word don't exist in the input matrix.
"""
import itertools


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        if _fast_exit(board, word):
            return False
        for i, j in itertools.product(range(m), range(n)):
            if board[i][j] != word[0]:
                continue
            if _dfs(
                i=i, j=j, wpos=1, cur_seen={(i, j)},
                board=board, word=word,
            ):
                return True
        else:
            return False


def _fast_exit(board, word):
    word_set = set(word)
    board_set = set(char for row in board for char in row)
    return not (board_set.issuperset(word_set))

def _dfs(i, j, wpos, cur_seen, board, word):
    m, n = len(board), len(board[0])
    if wpos == len(word):
        return True
    for adj_i, adj_j in neigbs(
        i=i, j=j, m=m, n=n,
        cur_seen=cur_seen,
    ):
        if board[adj_i][adj_j] != word[wpos]:
            continue
        adj = (adj_i, adj_j)
        cur_seen.add(adj)
        if _dfs(
            i=adj_i, j=adj_j, wpos=wpos+1, cur_seen=cur_seen,
            board=board, word=word,
        ):
            return True
        cur_seen.discard(adj)
    else:
        return False


def neigbs(i, j, m, n, cur_seen):
    for adj_i, adj_j in [(i-1,j), (i+1, j), (i,j-1), (i, j+1)]:
        if not ((0 <= adj_i < m) and (0 <= adj_j < n)):
            continue
        if (adj_i, adj_j) in cur_seen:
            continue
        yield (adj_i, adj_j)

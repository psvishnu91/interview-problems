"""296. Best Meeting Point

https://leetcode.com/problems/best-meeting-point/


Brute force
----------- 
- Create a set of positions of 1s
- BFS from every position until we find all the 1s. We keep track of total
    sum.
- We find max over all positions.
T - O(n^2,m^2)  S - O(NM)


Slightly more optimal
---------------------
K - num 1s
O(KNM)

- We create matrix of zeros of NxM
- Starting at every one, we bfs out and add the current depth to the
value of the matrix.
- Iterate over the matrix and find the min.


More optimal: Consider each dimension separately O(m^2+n^2)
----------------------------------------------
Because we are using manhattan distance. The x-dist and y-dist are independent.
In other words, we can consider finding the optimal x position and the y position
separately. Imagine all the ones are on the same row (first row) and all the columns
positions of ones are on the same column (first column). The distance will remain the
same.

Optimal solution: Need to realise that the median minimises the manhattan distance.
"""
import itertools
import collections


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        return solution_coords_indep_median(grid)

##############################################################################
# Optimal solution: Need to realise that the median minimises the manhattan
#  distance.
#
# Treat each coordinate independent. Find the ones positions in each coordinate.
# Find the median in each coordinate and take the difference in positions as
# distance.
# O(nm + mlogm + nlogn)
##############################################################################

def solution_coords_indep_median(grid):
    n, m =len(grid), len(grid[0])
    row_ones, col_ones = [], []
    for i, j in itertools.product(range(n), range(m)):
        if grid[i][j] != 1:
            continue
        row_ones.append(i)
        col_ones.append(j)
    row_ones, col_ones = sorted(row_ones), sorted(col_ones)
    return (
        _dist_from(arr=row_ones, from_ix=_find_median(row_ones))
        + _dist_from(arr=col_ones, from_ix=_find_median(col_ones))
    )

def _find_median(arr_ones):
    n = len(arr_ones)
    if n % 2 == 1:
        # odd just pick mid position
        return arr_ones[n//2]
    else:
        up_ix = n//2
        return (arr_ones[up_ix-1] + arr_ones[up_ix]) / 2.0


def _dist_from(arr, from_ix):
    return int(sum(abs(one_ix-from_ix) for one_ix in arr))

##############################################################################
# Treat each coordinate independent. Sort and find the best position between
# positions of the min 1 and max 1 positions in the coordinate
# O(n^2 + m^2 + nm)
##############################################################################

def solution_coords_indep(grid):
    n, m = len(grid), len(grid[0])
    row_ones, col_ones = [], []
    for i, j in itertools.product(range(n), range(m)):
        if grid[i][j] != 1:
            continue
        row_ones.append(i)
        col_ones.append(j)
    # O(n^2) check to find the best row_ix
    min_row_dist = _find_min_dist(sorted(row_ones))
    # O(m^2) check to find the best col_ix
    min_col_dist = _find_min_dist(sorted(col_ones))
    return min_row_dist + min_col_dist


def _find_min_dist(one_arr):
    """
    one_arr is assumed to be sorted
    """
    return min(
        # find the abs diff with each one
        sum(abs(ix-one_ix) for one_ix in one_arr)
        # for every ix between the min 1 and max 1 position
        # in this coordinate
        for ix in range(one_arr[0], one_arr[-1]+1)
    )

##############################################################################
# BFS solution, where you bfs out of the ones. Time limit exceeded
# O(n^2m^2)
##############################################################################

def solution_bfs(grid):
    n, m = len(grid), len(grid[0])
    dists = [[0]*m for _ in range(n)]
    for one_pos in _iter_ones(grid):
        _bfs(one_pos=one_pos, dists=dists)
    return min(
        dists[i][j]
        for i, j in itertools.product(range(n), range(m))
    )

def _iter_ones(grid):
    n, m = len(grid), len(grid[0])
    for i, j in itertools.product(range(n), range(m)):
        if grid[i][j] == 1:
            yield i, j


def _bfs(one_pos, dists):
    n, m = len(dists), len(dists[0])
    seen = set([one_pos])
    q = deque([one_pos])
    level = 0
    while q:
        qlen = len(q)
        for i in range(qlen):
            cur = q.popleft()
            cur_i, cur_j = cur
            dists[cur_i][cur_j] += level
            for adj in _get_adjs(pos=cur, n=n, m=m):
                if adj in seen:
                    continue
                seen.add(adj)
                q.append(adj)
        level += 1


def _get_adjs(pos, n, m):
    i, j = pos
    for adj_i, adj_j in [
        (i, j-1),
        (i, j+1),
        (i-1, j),
        (i+1, j),
    ]:
        if (
            (0 <= adj_i < n)
            and (0 <= adj_j < m)
        ):
            yield (adj_i, adj_j)

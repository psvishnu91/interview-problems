"""1861. Rotating the Box

https://leetcode.com/problems/rotating-the-box

Steps
-----
- Efficiently move the stones
- Then rotate box

["#",".","*","#"]
["#","#","*","."]
["#","#",".",".", "*", "."]
  0   1   2   3    4    5

algo is 
- rotated_row = [. . . . # #]
- rt_max = []
- if see '.' update rt_max append [3,2] LIFO
- pop out first val, and then add a 

- rotated_row = [. . # # * .]
rt_max [1,0]

[
    [1,2],
    [3,4],
    [6,7],
    [8,9]
]
n, m = len(box), len(box[0])
[
    [6,3,1]
    [7,4,2]
]
0,0 => 0,m-1
0,1 => 1,m-1
1,0 => 1,m-2
2,0 => 0,m-3
for i, j in itertools.product(range(n), range(m)):
    rotated_box[j][i] = box[i][j]


"""
from collections import deque
import itertools

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        box = move_stones(box)
        return rotate_box(box)


def move_stones(box):
    return [move_stone_row(row=row) for row in box]

def move_stone_row(row):
    """

    ["#","#",".",".", "*", "."]

    ["#",".", ".", "*", '.', "#"]
      0   1    2    3    4    5
    
    [. . # * . #]

    ix  char    q
    5    #      []
    4    .      [4]
    3    *      []
    2    .      [2]
    1    .      [2,1]
    0    #      [1,0]
    """
    q = deque()
    output = [None]*len(row)
    for ix, obj in reversed(list(enumerate(row))):
        match obj:
            case '.':
                output[ix] = '.'
                q.append(ix)
            case '*':
                output[ix] = '*'
                q.clear()
            case '#':
                if not q:
                    output[ix] = '#'
                else:
                    fallen_ix = q.popleft()
                    output[fallen_ix] = '#'
                    output[ix] = '.'
                    q.append(ix)
    return output


def rotate_box(box):
    n, m = len(box), len(box[0])
    rotated_box = [[None]*n for _ in range(m)]
    for i, j in itertools.product(range(n), range(m)):
        # This is not a normal transpose. You need to flip correctly.
        rotated_box[j][n-1-i] = box[i][j]
    return rotated_box

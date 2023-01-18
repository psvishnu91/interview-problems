from pprint import pprint
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        return gen_mat(n=n)

def gen_mat(n):
    mat = [[0]*n for _ in range(n)]
    offset, num, max_n = 0, 1, n*n
    while True:
        last_off = n-1-offset
        for iter_fn, beg_ix, end_ix in [
            (_iter_rt, (offset, offset), (offset,last_off)),
            (_iter_down, (offset+1, last_off), (last_off, last_off)),
            (_iter_lt, (last_off, last_off-1), (last_off, offset)),
            (_iter_up, (last_off-1, offset), (offset+1,offset)),
        ]:
            if num == max_n:
                mat[beg_ix[0]][beg_ix[1]] = max_n
                return mat
            num = assign(mat=mat, beg_ix=beg_ix, end_ix=end_ix, beg_num=num, iter_fn=iter_fn)
        offset += 1
    return mat

def assign(mat, beg_ix, end_ix, beg_num, iter_fn):
    num = beg_num
    for i, j in iter_fn(beg_ix=beg_ix, end_ix=end_ix):
        mat[i][j] = num
        num += 1
    return num


def _iter_rt(beg_ix, end_ix):
    i, beg_j = beg_ix
    _, end_j = end_ix
    for j in range(beg_j, end_j+1):
        yield i, j

def _iter_down(beg_ix, end_ix):
    beg_i, j = beg_ix
    end_i, _ = end_ix
    for i in range(beg_i, end_i+1):
        yield i, j

def _iter_lt(beg_ix, end_ix):
    i, beg_j = beg_ix
    _, end_j = end_ix
    for j in range(beg_j, end_j-1,-1):
        yield i, j

def _iter_up(beg_ix, end_ix):
    beg_i, j = beg_ix
    end_i, _ = end_ix
    for i in range(beg_i, end_i-1, -1):
        yield i, j

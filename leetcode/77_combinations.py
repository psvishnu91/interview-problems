
"""77. Combinations

https://leetcode.com/problems/combinations

Binary mask solution

 n = 4, k = 2
 max_num = 2^4 - 1 = 15 => 1 1 1 1


mask            chosen_ix   bit_ix   chosen_num
------------------------------------------------
1  - 0001           1          2        [1, None]
2  - 0010
3  - 0011           2          3        [1, 2]  


Backtracking solution 
n = 4
k = 2
i                       1           2               3          4        2       
firstnum    1           1           2       3       2          2        1
pos         0           0           1       3       1          1        0
cur         [N,N]       [1,N]       [1,2]           [1, 3]     [1,4]    [2,N]
output      []                             [[1,2]]  [[],[]]  [[],[],[]]
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return _combine_backtrack(n, k)

    
    
def _combine_backtrack(n, k):
    output = []
    _combine_backtrack_rec(n=n, k=k, firstnum=1, cur=[None]*k, pos=0, output=output)
    return output


def _combine_backtrack_rec(n, k, firstnum, pos, cur, output):
    if pos == k:
        output.append(cur.copy())
        return
    for i in range(firstnum, n+1):
        cur[pos] = i
        _combine_backtrack_rec(n=n, k=k, firstnum=i+1, pos=pos+1, cur=cur, output=output)

    
def _combine_binary_mask(n, k):
    max_num = 2**n - 1
    chosen_sets = []
    for mask in range(1, max_num+1):
        nums = generate_nums_with_mask(mask, k)
        if nums is not None:
            chosen_sets.append(nums)
    return chosen_sets


def generate_nums_with_mask(mask, k):
    chosen_nums = [None] * k
    chosen_ix = 0
    bit_ix = 1
    while mask:
        lsb_match = (mask & 1)
        if lsb_match and chosen_ix < k:
            chosen_nums[chosen_ix] = bit_ix
            chosen_ix += 1
        elif lsb_match and chosen_ix == k:
            return None
        mask >>= 1
        bit_ix += 1
    return chosen_nums if chosen_ix == k else None

"""40. Combination Sum II

https://leetcode.com/problems/combination-sum-ii/

Brute force
–––––––––––
Create all combinations using bit mask and iterate over array with bit mask and compute sum
Keep a seen set of indices. If the bit mask suggests a previously selected index we reject.
 - 2^n O(n)

Optimal solution
–––––––––––––––––
It's important to realise that if you have an array like [1,7,1,2,2] and target is 8,
you will generate both 1,7 and 7,1. The position of ones doesn't matter so it would
be ideal if we keep all the ones at the beginning. One way to do this is
to keep a counter table that is sorted by the numbers. 

[(1, 2), (2,2), (7,1)]

We dfs through this table and each time we decrement the count of one of the counters
(if non-zero) by iterating left to right of the array. As we decrement the counter, we
add the corres number to the combination array and then continue dfs. We remove the
number from the combination array and add back the counter after dfs in the iteration.

Very fast pruning optimisation:
–––––––––––––––––––––––––––––––
if we find that total + num > tgt, we break and don't dfs into the other subtrees
as they will also be greater (as we have ordered the counters in a sorted fashion).
"""
from collections import Counter


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        return _combine_sum(cands=candidates, tgt=target)


def _combine_sum(cands, tgt):
    output = []
    counter = sorted([num, cnt] for num, cnt in Counter(cands).items())
    _dfs(
        pos=0,
        counter=counter,
        total=0,
        combination=[],
        cands=cands,
        output=output,
        tgt=tgt,
    )
    return output


def _dfs(pos, counter, total, combination, cands, output, tgt):
    if total > tgt:
        return
    if total == tgt:
        output.append(combination.copy())
        return
    for i in range(pos, len(counter)):
        num, cnt = counter[i]
        if cnt == 0:
            continue
        new_total = total + num
        if new_total > tgt:
            break
        combination.append(num)
        counter[i] = [num, cnt-1]
        _dfs(
            pos=i,
            counter=counter,
            total=new_total,
            combination=combination,
            cands=cands,
            output=output,
            tgt=tgt,
        )
        counter[i] = [num, cnt]
        combination.pop(-1)

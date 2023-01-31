"""39. Combination Sum

https://leetcode.com/problems/combination-sum/

Algorithm
--------
cands = sorted(cands)
combin, output = [], []
pos=0
def rec(pos, total, combin, output, cands, target):
    if total == target:
        output.append(combin.copy())
    for i in range(pos, len(cands)):
        num = cands[i]
        new_total = num + total
        if new_total > target:
            break
        combin.append(num)
        rec(pos=i, total=total, combin=combin, output=output, cands=cands, target=target)
        combin.pop()
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        _dfs(
            pos=0,
            total=0,
            combin=[],
            output=output,
            cands=sorted(candidates),
            target=target,
        )
        return output

def _dfs(pos, total, combin, output, cands, target):
    """
    [1,2,3,6] target=6
     0 1 2 3
                    pos=0,v=1,t=0,nt=1
                    /   |                |                  \ 
            p=0,v=1    p=1,v=2          p=2,v=3           p=3,v=6
                /
            p=0,v=1,t=3
    """
    if total == target:
        output.append(combin.copy())
    for i in range(pos, len(cands)):
        num = cands[i]
        new_total = num + total
        if new_total > target:
            # Optimisation. Since we sorted the candidates,
            # all the subsequent numbers are larger.
            break
        combin.append(num)
        _dfs(pos=i, total=new_total, combin=combin, output=output, cands=cands, target=target)
        combin.pop()

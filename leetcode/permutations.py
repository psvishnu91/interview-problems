"""
https://leetcode.com/problems/permutations/

Solution
output_list = []
start at each node and then dfs recursively populating the rest of the nodes.
have to keep a hashset of visited so that i don't revisit

dfs(cur, pos, seen_ixes)

# Test dfs
nums = [1, 2, 3]
n = 3
cur      num       pos          seen              output
-------------------------------------------------------------
[N,N,N]             0              []               []
[1,N,N]   1         1              [1]              []
[1,2,N]   2         2              [1,2]            []
[1,2,3]   3         3              [1,2,3]          []
[1,2,3]   -         -              [1,2,3]          [[1,2,3]]
[1,2,3]   3         2              [1,2]          [[1,2,3]]



"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return permute(nums)


def permute(nums):
    n = len(nums)
    if n == 1:
        return [nums]
    output = []
    perm_dfs(nums=nums, cur=[None] * n, pos=0, seen=set(), output=output)
    return output


def perm_dfs(nums, cur, pos, seen, output):
    n = len(nums)
    if pos == n:
        output.append(cur.copy())
        return
    for num in nums:
        if num in seen:
            continue
        seen.add(num)
        cur[pos] = num
        perm_dfs(nums=nums, cur=cur, pos=pos + 1, seen=seen, output=output)
        seen.discard(num)

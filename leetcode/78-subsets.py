"""78. Subsets

https://leetcode.com/problems/subsets/

Solution 1: Generate bit masks
------------------------------
2^n unique subsets time and memory complexity same
generate bit masks for all numbers between 0 - 2^n-1
[1,2,3]
 
000
001
010
011
100
101
110
111

Edge cases:

nums - single element [0] [0, 2) -> mask =>{0, 1}

Solution 2: DFS
---------------
1 2 3
0 1 2

pos = 0
path = []
output = []

output = [[]]

def _dfs(pos, path, output, nums):
    output.append(path.copy())
    for i in range(pos, len(nums)):
        path.append(nums[i])
        _dfs(pos=i+1, path=path, output=output, nums=nums)
        path.pop()

                        pos=0,o=[]
                            o=[[]]
                        /                                   |                                   \ 
                pos=1,pt=[1]                                pos=2,pt=[2]    
                    o=[[], [1]]                             
                    /                       \            
                pos=2,pt=[1,2]              pos=3,pt=[1,3]    
                    o=[[], [1], [1,2]]      o=[[1], [1,2], [1,2,3], [1,3]]
                    /                
                pos=3,pt=[1,2,3]        
        o=[[],[1], [1,2],[1,2,3]]       
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return subsets_dfs(nums)


#############################################################
# DFS
def subsets_dfs(nums):
    output = []
    _dfs(pos=0, path=[], output=output, nums=nums)
    return output

def _dfs(pos, path, output, nums):
    output.append(path.copy())
    for i in range(pos, len(nums)):
        path.append(nums[i])
        _dfs(pos=i+1, path=path, output=output, nums=nums)
        path.pop()


###############################################################
# BIT MASK

def subset_masks(nums):
    n = len(nums)
    output = []
    for mask in range(0, 2**n):
        output.append(build_subset(nums, mask))
    return output


def build_subset(nums, mask):
    """
    123
    012

    101

    ix mask sbs
    ------------
    0  101  [1]
    1  10   [1]
    2  1    [1,3]
    3  0
    """
    subset  = []
    ix = 0
    while mask:
        if mask & 1:
            subset.append(nums[ix])
        ix += 1
        mask >>= 1
    return subset

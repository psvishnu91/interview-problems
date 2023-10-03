"""1679. Max Number of K-Sum Pairs

https://leetcode.com/problems/max-number-of-k-sum-pairs

Solution two pointer after sorting
---------------------------------
T - O(n log n)
S - O(n) if we use mergesort of O(1) if we use quicksort
    mergesort is preferred so that we don't mutate the input

have a lt and rt pointer. if sum of two nums is smaller than
target move lt fwd and if greater move rt back. If sum is
equal to target then update counter and move both.
"""

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        lt, rt = 0, len(nums) - 1
        num_pairs = 0
        while lt < rt:
            total =  nums[lt] + nums[rt] 
            if total == k:
                num_pairs += 1
                lt += 1
                rt -= 1
            elif total < k:
                lt += 1
            else:
                # total > k
                rt -= 1
        return num_pairs

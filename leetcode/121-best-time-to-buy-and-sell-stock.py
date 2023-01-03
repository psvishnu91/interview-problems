"""121. Best Time to Buy and Sell Stock

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Problem:

    [7, 1, 5, 3, 6, 4]
    Max profit = 5 (buy at 1 and sell at 6)

Solutions:

1. Brute force, assume we buy at every index and iterate and
    sell at every after index, update max_profit variable.

    O(n^2)

2. Single pass
Keep min_val=nums[0] and max_profit=0
keep num-with min_val and update max_profit.

Testing:
7,1,5,3,6,4
0 1 2 3 4 5

p   mv, mp, 
---------
    7   0  
7   7   0
1   1   0
5   1   4
3   1   4
6   1   5
4   1   5
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val, max_profit = prices[0], 0
        for p in prices:
            min_val = min(p, min_val)
            max_profit = max(max_profit, p-min_val)
        return max_profit

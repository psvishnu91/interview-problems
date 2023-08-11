"""122. Best Time to Buy and Sell Stock II

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Idea:
We just check the next day prices, if it's higher we buy now and
sell then. there's no point in holding a stock when the price goes
down, we should sell now and buy it the next day.
"""
class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        max_profit = 0
        for i in range(n-1):
            if prices[i] < prices[i+1]:
                max_profit += prices[i+1] - prices[i]
        return max_profit

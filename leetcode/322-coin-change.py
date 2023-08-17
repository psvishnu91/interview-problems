"""322. Coin Change

https://leetcode.com/problems/coin-change/

Does it ever make sense to not use the largest number? [Greedy]
Yes, take the example [3, 5] - Target 6. So greedy doesn't work.

Solution - DFS with caching
--------------------------
T - O(amount * num_coins): For each amount we iterate over all coins.
    We only ever compute an amount once.
S - O(amount)
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return coin_change((coins), amount)


def coin_change(coins, amount):
    val = coin_change_rec(coins=sorted(coins), amount=amount, cache=[None]*(amount+1)) 
    if val == float('inf'):
        return -1
    else:
        return val

def coin_change_rec(coins, amount, cache):
    if amount == 0:
        return 0
    if cache[amount] is not None:
        return cache[amount]
    min_coins = float('inf')
    for c in coins:
        rem =  amount - c
        if rem < 0:
            break
        min_coins = min(
            min_coins,
            1 + coin_change_rec(coins=coins, amount=rem, cache=cache),
        )
    cache[amount] = min_coins
    return min_coins

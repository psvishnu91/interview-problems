from typing import *
from dataclasses import dataclass

MAX_NEG = int(-1e7)

@dataclass(frozen=True)
class CacheKey:
    pos: int
    bought: int
    sold: int


def _max_profit(prices) -> int:
    return _max_profit_rec(
        i=0,
        bought=0,
        sold=0,
        prices=prices,
        cache={},
    )


def _max_profit_rec(
        i: int, bought: int, sold: int, prices: List[int],
        cache) -> int:
    cache_key = CacheKey(pos=pos, bought=bought, sold=sold)
    try:
        return cache[cache_key]
    except KeyError:
        pass
    n = len(prices)
    if i == n or sold == 2:
        return 0
    opt_buy, opt_sell, opt_do_nothing = MAX_NEG, MAX_NEG, MAX_NEG
    if (sold == bought):
        opt_buy = -prices[i] + _max_profit_rec(
            i=i+1, bought=bought+1, sold=sold,
            prices=prices, cache=cache,
        )
    if (bought > sold):
        opt_sell = prices[i]+_max_profit_rec(
            i=i+1, bought=bought, sold=sold+1,
            prices=prices, cache=cache,
        )
    opt_do_nothing = _max_profit_rec(
        i=i+1, bought=bought, sold=sold,
        prices=prices, cache=cache,
    )
    max_profit = max(opt_buy, opt_sell, opt_do_nothing)
    cache[cache_key] = max_profit
    return max_profit


if __name__ == "__main__":
    print(_max_profit([3,3,5,0,0,3,1,4]))
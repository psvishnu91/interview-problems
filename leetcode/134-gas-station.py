"""134. Gas Station

https://leetcode.com/problems/gas-station/

Greedy - O(n)
-------------
If sum of cost > sum of gas: we do not have a solution,
otherwise there absolutely exists at least one solution.
We cannot have a configuration that will lead us to
a situation where the total sum of one array is greater
than the other and there isn't a position on the array
from which the total sum isn't always positive.

We are told in the problem that we have at most one solution.

Algo:
    - Create a diff array of gas - cost
    - Create a total = 0
    - Iterate over diff, updating total, if total is negative
        reset to zero and mark the next index as a potential
        start.
    - When we make it to the end of the list, we are done,
        we simply return the start. We don't have to go
        check from the beginning as we know the total diff is
        positive (sum(gas) > sum(cost))

Brute force - O(n^2)
-------------------
Start at every index. Move through the array, taking
the start gas and then moving to next position getting next gas
if we can make it back to the start array this result is valid.

def is_possible(gas, cost):
    n = len(gas)
    for i in range(n):
        if _is_possible_from(start=i, gas=gas, cost=cost):
            return i
    else:
        -1

g-c =   [-2 -2 -2  3 3]
pfx_sum [-2 -4 -6 -3 0]

    g = 3 5 4
    c = 3 4 5
    g-c=0 1 -1
    ps =0 1 0


g-c =       [-1 -1 1]
pfx_sum =   [-1 -2 -1]
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #return is_possible_n2(gas, cost)
        return is_possible_greedy(gas, cost)

############################################################################
# Greedy O(n)
############################################################################

def is_possible_greedy(gas, cost):
    n = len(gas)
    diff = [gas[i]-cost[i] for i in range(n)]
    if sum(gas) < sum(cost):
        # Solution doesn't exist
        return -1
    # Solution has to exist. There has to be some starting point
    # that let's you to be always net positive gas along the way
    total, start_ix = 0, 0
    for i in range(n):
        total += diff[i]
        if total < 0:
            total = 0
            start_ix = i+1
    return start_ix
    
############################################################################
# Simple O(n^2)
############################################################################

def is_possible_n2(gas, cost):
    n = len(gas)
    for i in range(n):
        if _is_possible_from(start=i, gas=gas, cost=cost):
            return i
    else:
        return -1

def _is_possible_from(start, gas, cost):
    """
    g=1 2 3 4 5
      0 1 2 3 4
    c=3 4 5 1 2


    s i ix c[ix] g[ix] tank
    ------------------------------
    3 3 3   1    4     

    """
    n = len(gas)
    tank = 0
    for i in range(start, start + n):
        ix = i % n
        # fill up gas and try to go to next pos
        tank += gas[ix] - cost[ix]
        if tank < 0:
            return False
    else:
        return True
Console

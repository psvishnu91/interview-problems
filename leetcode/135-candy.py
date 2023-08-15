"""135. Candy

Two pass solution
- start with 1 candy for each child
- iterate from left to right, whenever ratings[i] > ratings[i-1],
    then we make, candies[i] = candies[i-1] + 1
- iterate from right to left, whenever ratings[i] > ratings[i+1],
    then we make, candies[i] = max(candies[i], candies[i+1] +1).
    We do the max here because we could have arrived at a higher
    peak value from the left than right

r           1 2 3 4 5 4 2 1
lt_candies  1 2 3 4 5 1 1 1
rt_candies  1 1 1 1 4 3 2 1 
candies     1 2 3 4 5 3 2 1
"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        # forward pass
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        # backward pass
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)
        return sum(candies) # we could also compute it in backward pass


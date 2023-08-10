"""169. Majority Element

https://leetcode.com/problems/majority-element/

Algo: Boyer-Moore Voting Algorithm
----------------------------------
We maintain two variables, current num_maj and
cnt_maj.

We know that num_maj HAS TO appear more than half the time.
We will make the first number the major, and increment cnt it
everytime we see it and decrement everytime we see a different
number. The moment the cnt goes neg, we set the cur num as maj
and set cnt to 1. Because we are guaranteed that maj num
appears more than half the time, this will always be the maj
element.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_maj = nums[0]
        cnt_maj = 0
        for num in nums:
            if num == num_maj:
                cnt_maj += 1
            else:
                if cnt_maj > 0:
                    cnt_maj -= 1
                else:
                    num_maj = num
                    cnt_maj = 1
        return num_maj
                    

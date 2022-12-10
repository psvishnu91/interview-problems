"""43. Multiply Strings

https://leetcode.com/problems/multiply-strings/

Thinking
--------
- Convert strings to list of numbers

Reduce problem into two problems
- Multiply n digit number with a single digit
- Sum two list of ints representing a number

Test
====
123*5
615
123*4
4920
 615

num1 = "123", num2="45"
output = 5535

place digit2 num1   res
=======================
0       5     123   [6,1,5]
1       4     123

digit digit2 carry_over ans
===============================
3      5       1       [5]
2      5       1       [5,1]
1      5       0       [5,1,6]


digit digit2 carry_over ans
===============================
        4        0       [0]
3       4        1       [0,2]
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return _multiply(num1, num2)


def _multiply(num1, num2) -> str:
    if num1 == "0" or num2 == "0":
        return "0"
    num1, num2 = [int(c) for c in num1], [int(c) for c in num2]
    res = mult_with_single_digit(num1=num1, digit2=num2[-1], place=0)
    for place, digit2 in enumerate(reversed(num2)):
        if place == 0:
            continue
        res = sum_2_listed_nums(
            num1=res, num2=mult_with_single_digit(num1=num1, digit2=digit2, place=place)
        )
    # we include all the numbers after the first non zero number
    first_non_zero_ix = len(res) - 1
    for ix, digit in enumerate(res):
        if digit != 0:
            first_non_zero_ix = ix
            break
    return "".join(str(n) for n in res[first_non_zero_ix:])


def mult_with_single_digit(num1: int, digit2: int, place: int) -> List[int]:
    carry_over = 0
    ans = [0] * place
    digit2 = digit2
    for digit in reversed(num1):
        prod = (digit) * digit2 + carry_over
        carry_over = prod // 10
        ans.append(prod % 10)
    if carry_over:
        ans.append(carry_over)
    return list(reversed(ans))


def sum_2_listed_nums(num1: List[int], num2: List[int]) -> List[int]:
    sz1, sz2 = len(num1), len(num2)
    num1 = [0] * (sz2 - sz1) + num1
    num2 = [0] * (sz1 - sz2) + num2

    new_sz = max(sz1, sz2)
    res = [0] * new_sz
    carry_over = 0
    # n1 = '12', n2 = '34'
    # [0,1]
    # [(0,'2','4'), (1, '1', '3')]
    for i, digit1, digit2 in zip(range(new_sz), reversed(num1), reversed(num2)):
        sm = (digit1) + (digit2) + carry_over
        res[i] = sm % 10
        carry_over = sm // 10
    if carry_over:
        res.append(carry_over)
    return list(reversed(res))

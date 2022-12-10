"""
Multiply two n digit numbers using karatsuba multiplication.

Usage::

    python karatsuba.py 122211 321

Sample output::

    Multiplication karatsuba:       39,229,731
    Multiplication inbuilt:         39,229,731
"""
from typing import List
from typing import Tuple
import math
import sys


def _parse_input(argv: List[str]) -> Tuple[int, int]:
    return int(argv[1]), int(argv[2])


def _find_num_digits(num: int) -> int:
    if num == 0:
        return 1
    return int(math.log10(num)) + 1


def multiply(num1: int, num2: int) -> int:
    """Multiplies two numbers recursively using karatsuba algorithm.

    Please see https://youtu.be/JCbZayFr9RE for details.
    """
    ndigits = min(_find_num_digits(num1), _find_num_digits(num2))
    if ndigits == 1:
        return num1 * num2
    mid = 10 ** (ndigits // 2)
    mid_ndigits = ndigits // 2
    # a and c are the leading digits of the n1 and n2
    # b and d are the trailing digits
    a, c = num1 // mid, num2 // mid
    b, d = num1 % mid, num2 % mid
    ac = multiply(num1=a, num2=c)
    bd = multiply(num1=b, num2=d)
    ad_plus_bc = multiply(num1=(a + b), num2=(c + d)) - ac - bd
    # We will have to multiply ac by the total digits taken away from 2 numbers
    # which is twice mid_ndigits as we remove ndigits from both numbers
    return ac * (10 ** (mid_ndigits * 2)) + bd + ad_plus_bc * (10 ** (mid_ndigits))


if __name__ == "__main__":
    num1, num2 = _parse_input(sys.argv)
    print(f"Multiplication karatsuba: \t{multiply(num1, num2):,}")
    print(f"Multiplication inbuilt: \t{(num1*num2):,}")

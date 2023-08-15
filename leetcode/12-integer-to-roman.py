"""12. Integer to Roman

https://leetcode.com/problems/integer-to-roman

Algo:
1. We have a list of highest roman sym to val
2. Init roman = []
3. We do q=num//roman_val r=num%roman_val if
    q=0 we don't append anything to roman
    q<4 we append that many Sym to roman
    q==4: There are two cases
        Case 1: 4, 40, 400
        Case 2: 9, 90, 900
        In Case 2: the roman so far would have [...V], [...L], or [...D]
        and in Case 1, we won't. We check for this and in Case 1,
        we simply append [...IV], [...,XL], or [...,CD]; in Case 2,
        we replace the last char with [...IX], [...XC], [...CM] resply
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        symval = [("M", 1000), ("D", 500), ("C", 100), ("L", 50), ("X", 10), ("V", 5), ("I", 1)]
        roman = []
        for i, (sym, val) in enumerate(symval):
            q = num // val
            r = num % val
            if q == 0:
                continue
            if q != 4:
                roman.extend([sym] * q)
            else:
                # We need to contract as we have 4 of something
                grand_sym = symval[i-2][0]
                prev_sym = symval[i-1][0]
                if roman and roman[-1] == prev_sym:
                    # This is the scenario where we have something like
                    # 94
                    # sym=X, prev_sym=L, grand_sym=C
                    # roman=[L] new=XXXX -> convert to roman=[XC]
                    roman.pop()
                    roman.extend([sym, grand_sym])
                else:
                    # This is the scenario where we have something like
                    # 144 => [C]
                    # sym=X, prev_sym=L, grand_sym=C
                    # roman=[C] new = XXXX -> roman=[CXL]
                    roman.extend([sym, prev_sym])
            num = r
        return "".join(roman)


"""Rough work

84
LXXX I V

84// 50 = 1
84 % 50= 34

34 // 10 = 3
34 % 10 = 4

4 // 5 = 0
4%5 = 4

4 // 1 = 4
4%1 = 0

Option 1:
---------
Create the string and perform replaces in this order
DCCCC -> CM
CCCC -> CD

LXXXX -> XC
XXXX -> XL

VIIII -> IX
IIII -> IV

Option 2:
---------
If we ever get 4 as the quotient, then we append the 

9//5=1
9%4=4

[V] -> [IX]
4//1=4()
----

24
[XX]

4 // 5 = 0
4 % 5 = 4

4//1 = 4
4%4 = 0


Edge cases
----------
- 4
- 9
- 944
- 36

roman = []
i sym val   q   r   gs  ps  roman
---------------------------------
0 M   1000  0   944
1 D   500   1   444         [D]
2 C   100   4   44  M   D   [C,M]
3 L   50    0   44  
4 X   10    4   4   C   L   [C,M,X,L]


1994
roman = []
i sym val   q   r   gs  ps  roman
---------------------------------
0 M   1000  1   994         [M]
1 D   500   1   494         [M D]
2 C   100   4   94  M   D   [C,M]
3 L   50    0   44  
4 X   10    4   4   C   L   [C,M,X,L]

"""

"""151. Reverse Words in a String

https://leetcode.com/problems/reverse-words-in-a-string

Cases
-----
one word spaces each side
"  hi  "
 012345

i s[i] we res
5 " "  N   []
4 " "  N   []
3  i   4   []
2  h   4   []
1  " " N   ["hi"]

one word no leading spaces
"hi  "
 0123

i s[i] we res
3  "   N   []
2  2   N   []
1  i   2   []
0  h   2   []
            [hi]

2 words with trailing spaces
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        return interview_string_man(s)

def cheat_w_python(s):
    return " ".join(reversed(s.split()))

def interview_string_man(s):
    res = []
    n = len(s)
    w_end = None
    for i in range(n-1, -1, -1):
        if w_end is None and s[i] == " ":  # trailing spaces
            continue
        elif w_end is None and s[i] != " ":  # start of a word
            w_end = i+1
        elif w_end is not None and s[i] != " ":  # in a word
            continue
        elif w_end is not None and s[i] == " ":
            # end of a word
            res.append(s[i+1:w_end])
            w_end = None
        else:
            raise ValueError("Shouldn't happen")
    if w_end is not None:
        res.append(s[:w_end])
    return " ".join(res)

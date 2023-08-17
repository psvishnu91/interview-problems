"""71. Simplify Path

https://leetcode.com/problems/simplify-path/

Algorithm
- split '/'
- We have a second list result
- We iterate over the first list, if we encounter
    .., we pop, and at the end we join with /
- We skip empty spaces at the end


Edge cases
"/"
"///"
"/../"
"/hi/./boo/../goo"
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        for dirname in path.split("/"):
            if not dirname:
                continue
            elif dirname == ".":
                continue
            elif dirname == ".." and not stk:
                continue
            elif dirname == ".." and stk:
                stk.pop()
            else:
                stk.append(dirname)
        res = "/".join(stk)
        if not res:
            return "/"
        elif res[0] != "/":
            return "/" + res
        else:
            return res

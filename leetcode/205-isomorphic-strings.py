"""205. Isomorphic Strings

https://leetcode.com/problems/isomorphic-strings/

Algo: Dict and Set
-------------------

- Keep a dict mapping chars in s to chars in t.
- Keep a set of chars in t already assigned.
- Go through both strings, if char in s 

s "badc"
t  baba

cs ct mapping
      {}
b  b  {b:b}
a  a  {b:b, a:a}
d  b  

"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if s == t == "":
            return True
        if len(s) != len(t):
            return False
        # mapping[char_in_s)] -> char_in_t
        mapping = {}
        # char_in_t already assigned in the mapping above
        assigned = set()
        for cs, ct in zip(s, t):
            if cs in mapping and mapping[cs] == ct:
                # mapping exists and matches
                continue
            if cs in mapping and mapping[cs] != ct:
                # we already had to map this character but not it doesn't match
                return False
            # cs not in mapping
            if ct in assigned:
                # we have already mapped this value in to a different char in s
                return False
            mapping[cs] = ct
            assigned.add(ct)
        else:
            return True

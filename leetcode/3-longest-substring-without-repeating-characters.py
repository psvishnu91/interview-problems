"""3. Longest Substring Without Repeating Characters

https://leetcode.com/problems/longest-substring-without-repeating-characters

Idea
----
Two pointers.
- iterate over string for rt
- keep adding entries of s[rt] to a seen set
- as long as we are valid we keep updating a global maxlen var
- the moment we find a duplicate we move the lt pointer forward
    and delete from the seen set, until we crossover till we
    saw the last s[rt].

Test case
---------
pwwkew
012345

lt cl rt cr ml seen
0   p  0  p 1   {p}
0   p  1  w 2   {pw}
0   p  2  w 
1   w  2  w     {w}
2   w  2  w 2   {w}
2   w  3  k 2   {wk}
2   w  4  e 3   {wke}
2   w  5  w     
3   k  5  w 3   {kew}

Edge cases
---------
empty string
same char
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        lt = 0
        max_len = 0
        for rt in range(n):
            while s[rt] in seen:
                seen.discard(s[lt])
                lt += 1
            seen.add(s[rt])
            max_len = max(max_len, rt - lt + 1)
        return max_len

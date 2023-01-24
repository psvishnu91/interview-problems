"""1143. Longest Common Subsequence

https://leetcode.com/problems/longest-common-subsequence/

Recursive DP
Move both pointers forward until you find a character that doesn't match, recurse by 
increasing pointer of left word and pointer of right word. Cache would be of size 
len(s1)*len(s2). And cached on the position of the two pointers of the word.

Try to write the recursion in terms of pointers. 
length = is_match(i, j) + max(  (i+1, j), (i, j+1) 

Bottoms up DP
n, m = len(s1), len(s2)
We can also solve this with bottoms up DP. Here we create a matrix of dimension 
(n+1, m+1). M[0,0] contains the length of the lcs of the two entire strings. 
Whereas M[n-1, m-1] contain lcs of the last character of both. The row n+1 and col m+1 
are all 0s, because the longest common substr for an empty string and the rest of the 
other string M[n,m] is lcs of empty str and empty str.

Now we can move through the string in two ways
if s1[i] == s2[j]: 
    # (1 for this character and the longest subsequence by moving both pointers forward)
    then M[i,j] = 1+M[i+1, j+1] 
else:
    # moving one character on either string and finding the max substring for that.
    # We for loop from the bottom right, to top-left
    M[i,j] = max(M[i+1, j], M[i, j+1]) 

Test recursion
---------------
a c e
0 1 2
a d c e
0 1 2 3
(0,0)
p1 p2 
0  0 

            1 + val
            |
           p1=1, p2=1
            /        \
        (2,1) 1      (1,2)
        /   \           \   
      0(3,1) (2,2) 1    1+(2,3)
              /     \        \ 
             (3,2)  (2,3) 1  1
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return lcs(text1, text2)
    

def lcs(t1, t2) -> int:
    n1, n2= len(t1), len(t2)
    cache = [[None]*n2  for _ in range(n1)]
    length = lcs_rec(
        t1=t1, t2=t2, p1=0, p2=0,
        cache=cache,
    )
    pprint(cache)
    return length


def lcs_rec(t1, t2, p1, p2, cache) -> int:
    n1, n2 = len(t1), len(t2)
    if p1 >= n1 or p2 >= n2:
        return 0
    if cache[p1][p2] is not None:
        return cache[p1][p2]
    cs = 0
    i1, i2 = p1, p2
    while i1 < n1 and i2 < n2 and t1[i1] == t2[i2]:
        cs += 1
        i1 += 1
        i2 += 1
    longest_cs = cs + max(
        lcs_rec(t1=t1, t2=t2, p1=i1+1, p2=i2, cache=cache),
        lcs_rec(t1=t1, t2=t2, p1=i1, p2=i2+1, cache=cache),
    )
    cache[p1][p2] = longest_cs
    return longest_cs


def lcs_botup(t1, t2) -> int:
    n1, n2 = len(t1), len(t2)
    # lcs[i][j] matrix contains the longest common subsequence of
    # of t1[i:] and t2[j:].
    lcs = [[0]*(n2+1) for _ in range(n1+1)]
    # bottom up, go in reverse
    for i in range(n1-1, -1, -1):
        for j in range(n2-1, -1, -1):
            if t1[i] == t2[j]:
                # if both are equal, max length is 1 plus 
                # longest common subsequence of t1[i+1:] and
                # t2[j+1:].
                lcs[i][j] = 1 + lcs[i+1][j+1]
            else:
                # If the characters are not equal, it is the
                # lcs of the string t1[i+1:] and t2[j:] or
                # t1[i:] and t2[j+1:]. Delete a char from either str.
                lcs[i][j] = max(lcs[i+1][j], lcs[i][j+1])
    return lcs[0][0]
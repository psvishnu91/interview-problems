"""763. Partition Labels

https://leetcode.com/problems/partition-labels/

Solution 1
==========
1. Build hashmap of char to end
2. Iterate over string and keep seen characters. beg=0
Check if index is end, if so discard from seen set.
If seen set is empty add index-beg+1 to output list
set beg=index+1.

bdddbcaca -> [bddb] [caca]
0123456789
hashmap = char->(end)

seen={bd}
i=4
discard b, if seen empty add to output

Solution 2
==========
Build hashmap/list of list with char to start, end ix
Iterate over characters, check if index is start or end of a character
keep track of new_seen characters. If start_index incremenet new_seen
if end character decrement. if new_seen is 0, add index-beg+1 and set
beg=index+1.


Edge cases
1. single char str
2. a char appearing only once
3. entire string

Test
====
ababdefef
012345678
{a:2, b:3, d:4, e:7, f:8}

i   c   seen    beg    output
=============================
0   a    {a}     0     []
1   b    {a,b}   0     []
2   a    {b}     0     []
3   b    {}      4     [4,]
4   d    {}      5     [4,1]
"""


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        return partition_labels(s)


def partition_labels(s):
    # List of start and end ix for each char
    ch_st_end_ix_map = [[None, None] for _ in range(26)]
    for i, c in enumerate(s):
        c_ix = to_ix(c)
        if ch_st_end_ix_map[c_ix][0] is None:
            ch_st_end_ix_map[c_ix][0] = i
        ch_st_end_ix_map[c_ix][1] = i
    new_seen = 0
    beg = 0
    sizes = []
    for i, c in enumerate(s):
        c_ix = to_ix(c)
        new_seen += i == ch_st_end_ix_map[c_ix][0]
        new_seen -= i == ch_st_end_ix_map[c_ix][1]
        if not new_seen:
            sizes.append(i - beg + 1)
            beg = i + 1
    return sizes


def to_ix(char):
    return ord(char) - ord("a")

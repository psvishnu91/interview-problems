"""49. Group Anagrams

https://leetcode.com/problems/group-anagrams/

Ask questions
=============
1. Can we have empty strings? => empty strings - consider anagrams?
2. What is the max size of the string
3. What is the min and max length of the array?

Brute force
===========
Create a list of counter classes (dict(char-> cnt)) for all the words
We also keep a Flag list included of all false
We double for loop, we compare the first word counter with the rest of the
words, if we equal we add it to an output list for this word. We mark the
corresponding flag of the new word as True (seen). When we iterate we only
include words that are not seen, both in the inner loop and in the outer loop.

O(N^2) and O(N) space both for flag, counter and output

Solution 2: Sorting
===================
N - num words
K - max word len

We sort each word. For each word O(100log100) => O(1). Sorting all words O(N)
or precisely O(N k log k).

Sort the entire array, with the indices - O(N log N)

Iterate over the array, keep track of curword, create an output list with
index and with same curword.

T - O(N log N + N k log k) 
S - O(N)


Optimal solution
================
Keep a map, mapping sorted word to word.

Testing
=======
Nominal
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sorted_strs = ["aet", "aet", "ant", "aet", "ant", "abt"]
                0       1      2      3      4      5
sorted_strs_ixes = [("abt", 5), ("aet", 0), ("aet", 1), ("aet", 3), ("ant", 2), ("ant", 4)]

ix     word cur_word     anagrams   anagrams_list        
===================================================
5      abt    abt         [bat]       []
0      aet    aet         [eat]       [[bat]]
1      aet    aet      [eat,  tea]
3      aet    aet  [eat, tea, ate]
2      ant    ant        [tan]          [[bat],[eat, tea, ate]]

Edge cases
==========
Multiple empty strings - consider anagrams?
No anagrams
All anagrams
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return group_anagrams_sorting(strs)


def group_anagrams_sorting(strs: list[str]) -> list[list[str]]:
    n = len(strs)
    # sort the sorted words with their original indices
    sorted_words_ixes = sorted(
        # sort each word
        zip(["".join(sorted(s)) for s in strs], range(n)),
    )
    anagrams_list = []
    cur_word, _ = sorted_words_ixes[0]
    anagrams = []
    for word, ix in sorted_words_ixes:
        orig_word = strs[ix]
        if word == cur_word:
            anagrams.append(orig_word)
        else:
            cur_word = word
            anagrams_list.append(anagrams)
            anagrams = [orig_word]
    anagrams_list.append(anagrams)
    return anagrams_list


def group_anagrams_sortmap(strs):
    sorted_to_words = collections.defaultdict(list)
    for w in strs:
        sorted_to_words[tuple(sorted(w))].append(w)
    return sorted_to_words.values()
    
    
    

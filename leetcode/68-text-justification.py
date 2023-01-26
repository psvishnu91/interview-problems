"""68. Text Justification

https://leetcode.com/problems/text-justification

we look at words one at a time, and len(word) + 1 for space
when this becomes larger than max_width, we construct the line
with these words.

First simplification don't do left justify for the last line.

When full justification, we compute
numspaces = max_width - sum(len(w) in words)
space_aft_word_avg = 

hi  bye bo
0123456789

wmin1 num_words-1
space_per_word =15//6 = 2 
spaces//wmin1
spaces%wmin1
for these words we add equal extra spaces at front
"""
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        word_groups = group_words(words=words, max_width=maxWidth)
        output = [
            justify(word_group=wg, max_width=maxWidth)
            for wg in word_groups[:-1]
        ] + [left_justify(word_group=word_groups[-1], max_width=maxWidth)]
        return output


def group_words(words, max_width):
    """
    ["aa", "bb", "ccc"] = 6
    """
    lines, line, cur_len = [], [], 0
    for word in words:
        new_len = cur_len + len(word)
        if new_len > max_width:
            lines.append(line)
            line = [word]
            cur_len = len(word) + 1
        else:
            # plus one for space
            cur_len = new_len + 1
            line.append(word)
    lines.append(line)
    return lines


def justify(word_group, max_width):
    """
    ["aa", "bb", "ccc"] = 14
    num_words = 3
    word_len = 7
    num_spaces = 7
    wlen_min1 = 2
    space_per_word = 3
    extra_spaces = 1
    i word tmp_line
    ===============
    0  aa  ["aa", 4" "]
    1  bb  ["aa", 4" ", "bb", 3" "]
    """
    num_words = len(word_group)
    if num_words == 1:
        return left_justify(word_group=word_group, max_width=max_width)
    words_len = sum(len(word) for word in word_group)
    num_spaces = max_width - words_len
    wlen_min1 = num_words - 1
    space_per_word = num_spaces // wlen_min1
    # these many words will get an extra space after the text
    extra_spaces = num_spaces % wlen_min1
    tmp_line = []
    for i, word in enumerate(word_group):
        tmp_line.append(word)
        if i != num_words - 1:
            tmp_line.append(" " * (space_per_word + int(i < extra_spaces)))
    return "".join(tmp_line)

        
def left_justify(word_group, max_width):
    unpadded_words = " ".join(word_group)
    return unpadded_words + " " * (max_width - len(unpadded_words))

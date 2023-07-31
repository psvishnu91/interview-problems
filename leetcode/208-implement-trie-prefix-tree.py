"""208. Implement Trie (Prefix Tree)

https://leetcode.com/problems/implement-trie-prefix-tree/

Logic
-----
Use a dict of child_char -> children_dict. Add characters iteratively
and find iteratively. Start with a sentinel root node.

words: apple, app, be

Root node   {'a':  , 'b':}
              /        \
          {'p':}        {'e': }
           /                \
         {'p':}             {'E': {}}
         /
        {'l': , 'E': {}}
        /
      {'e':}
      /
      {'E': {}}
The trie is maintained by a dict where each key is
a child character which contains a dict of it's child_char -> children_dict.

Every time we get a new a word gets added
1. We add `E` to the end.
2. We iterate over children of root node and keep moving until we
    have matching children. The moment we run out of matching children
    we add new nodes.

`Search` we add `E` to the word. We iterate over node until
    both match if they stop matching we return False.
"""


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        """
        R - a - p - p - l - e - E
                \
                 l - e - E
        Tests
        =====
        1. appE, wlen = 4
           0123
        node    ix  c
        {S}     0   a
        {a}     1   p
        {p}     2   p
        {p }    3   E
        {E}     4

        2. apleE, wlen = 5
           01234
        node    ix  c
        {S}     0   a
        {a}     1   p
        {p}     2   l
        {l}
        """
        word = word + "E"
        ix, node, wlen = 0, self.root, len(word)
        # Walk through existing nodes
        while ix < wlen:
            c = word[ix]
            if c not in node:
                break
            node = node[c]
            ix += 1
        # Create missing nodes
        while ix < wlen:
            c = word[ix]
            node[c] = {}
            node = node[c]
            ix += 1

    def search(self, word: str) -> bool:
        return self.startsWith(prefix=word + "E")

    def startsWith(self, prefix: str) -> bool:
        """
        Tests
        =====
        1. app: plen = 3
        012
        node    ix  c
        {S}     0   a
        {a}     1   p
        {p}     2   p
        {p}     3

        2. al: plen = 2
        01
        node    ix  c
        {S}     0   a
        {a}     1   l
        {l}
        """
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        else:
            # We iterated through the entire word and found no
            # missing character
            return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

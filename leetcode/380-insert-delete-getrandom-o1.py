"""380. Insert Delete GetRandom O(1)

https://leetcode.com/problems/insert-delete-getrandom-o1

Trick to get O(1) deletes from a list swap with the last element of the list. 

Have a list and hashmap.

Append values to the list as you recieve them and keep track of the
indices in a hashmap. While delete a value swap it with the last value
of the list and pop from the back of the list O(1),
updating the hashmap accordingly.
"""

class RandomizedSet:

    SZ = 100_000

    def __init__(self):
        self.vals = []
        self.val2ix = {}

    def insert(self, val: int) -> bool:
        if val in self.val2ix:
            return False
        self.vals.append(val)
        self.val2ix[val] = len(self.vals) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val2ix:
            return False
        if val == self.vals[-1]:
            # Handle edge case number to be deleted is the last
            # number
            self.vals.pop()
            del self.val2ix[val]
            return True
        else:
            # pop last element and swap with the number to be
            # deleted
            last_val = self.vals.pop()
            ix = self.val2ix.pop(val)
            self.vals[ix] = last_val
            self.val2ix[last_val] = ix
            return True

    def getRandom(self) -> int:
        # If more than half of the saved ixes are marked as deleted
        # Reset and create a new saved_ixes also update bkt_ix2saved_ix
        return self.vals[random.randint(0, len(self.vals)-1)]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""

# Iteration: have to keep a head and tail. Initialise both to an empty likedlist node.
def merge(h1, h2):
    head = Node()
    tail = head
    while h1 and h2:
        if h1.val <= h2.val:
            tail = h1
            h1 = h1.next
        else:
            tail = h2
            h2 = h2.next
        tail = tail.next
    # add rem elements
    tail.next = h1 if h2 is None else h2
    # return head.next as head is empty node
    return head.next


# Merge recursive
def merge_ll_rec(h1, h2):
    if h1 is None:
        return h2
    if h2 is None:
        return h1
    if h1.val <= h2.val:
        head = h1
        head.next = merge_ll_rec(h1=h1.next, h2=h2)
    else:
        head = h2
        head.next = merge_ll_rec(h1=h1, h2=h2.next)
    return head

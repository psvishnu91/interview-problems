"""
Given an array A with n distinct numbers and k, return the kth order statistic. The
k-th order statistic is the kth smallest number.

10, 8, 2, 4 -> 3rd order statistic is 8. First order statistic is 2.

Using reduction, we can sort the array in O(n log n) by sorting
and returning the (k+1)th element. However this algorithm is O(n).

Sample usage::

    # The fist number is taken as the k in the k-th order statistic interested
    python -m chapter_5_quicksort.selection_randomised 3 4 1 5 0 6

Sample output::

    INFO:Selection:Input list:	4 1 5 0 6 2 3 8 4 4 4
    INFO:Selection:Sorted list:	0 1 2 3 4 4 4 4 5 6 8
"""
import random

import utils


def selection(lst, beg, end, k):
    # Return the 0-indexed order statistic
    return _selection(lst=lst, beg=beg, end=end, k=k - 1)


def _selection(lst, beg, end, k):
    if not beg == end:
        _swap_pvt_to_beg(lst=lst, beg=beg, end=end)
    pivot_ix = _partition(lst=lst, beg=beg, end=end)
    if pivot_ix == k:
        return lst[pivot_ix]
    elif pivot_ix > k:
        return _selection(lst=lst, beg=beg, end=pivot_ix - 1, k=k)
    else:
        # pivot_ix < k
        return _selection(lst=lst, beg=pivot_ix + 1, end=end, k=k)


def _swap_pvt_to_beg(lst, beg, end):
    pivot_ix = random.randrange(beg, end)
    lst[beg], lst[pivot_ix] = lst[pivot_ix], lst[beg]


def _partition(lst, beg, end):
    if beg == end:
        return beg
    pvt_val = lst[beg]
    edge = beg
    for i in range(beg + 1, end + 1):
        if lst[i] <= pvt_val:
            edge += 1
            lst[edge], lst[i] = lst[i], lst[edge]
    lst[edge], lst[beg] = lst[beg], lst[edge]
    return edge


if __name__ == "__main__":
    # Sample inputs:
    # 4 1 5 0 6 2 3 8
    # 4 1 2 3
    # 4 5 6 7 8 9
    #  4 1 2 5 0 3 9 -1 -2
    input_list = utils.parse_input_array()
    k = input_list[0]
    lst = input_list[1:]
    if k > len(lst):
        raise RuntimeError(
            f"The {k} is larger than the length of the array {len(lst)=}."
        )
    kth_stat = selection(lst=lst, beg=0, end=len(lst) - 1, k=k)
    log = utils.get_logger("Selection")
    log.info("Input k={}, list:\t{}".format(k, " ".join(map(str, input_list))))
    log.info(f"{k}th-order statistic list:\t{kth_stat}")

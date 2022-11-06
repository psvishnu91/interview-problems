"""Sorts an input array with randomised quicksort.

Sample usage::

    python -m chapter_5_quicksort.quicksort 4 1 5 0 6 2 3 8 4 4 4

Sample output::

    INFO:Quicksort:Input list:	4 1 5 0 6 2 3 8 4 4 4
    INFO:Quicksort:Sorted list:	0 1 2 3 4 4 4 4 5 6 8
"""
import random

import utils
from chapter_5_quicksort import partition


def quicksort_inplace(lst, beg=0, end=None) -> None:
    if end is None:
        end = len(lst) - 1
    if beg >= end:
        return
    swap_random_pivot_to_beg(lst, beg, end)
    pivot_ix = partition.partition_inplace(lst=lst, beg=beg, end=end)
    quicksort_inplace(lst, beg=beg, end=pivot_ix-1)
    quicksort_inplace(lst, beg=pivot_ix+1, end=end)



def swap_random_pivot_to_beg(lst, beg, end):
    # Select a random pivot and swap it to the beginning of the array
    # Partition function assumes the pivot is at the beginning of the array
    pivot_ix = random.randrange(beg, end)
    lst[beg], lst[pivot_ix] = lst[pivot_ix], lst[beg]


if __name__ == "__main__":
    # Sample inputs: 
    # 4 1 5 0 6 2 3 8
    # 4 1 2 3
    # 4 5 6 7 8 9
    #  4 1 2 5 0 3 9 -1 -2
    input_list  = utils.parse_input_array()
    output_list = input_list.copy()
    quicksort_inplace(lst=output_list)
    log = utils.get_logger("Quicksort")
    log.info("Input list:\t{}".format(" ".join(map(str, input_list))))
    log.info("Sorted list:\t{}".format(" ".join(map(str, output_list))))

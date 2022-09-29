"""
Sort an array with merge sort.

Usage::

    python mergesort.py 8 2 1 3 5 9 8

Sample output::

    Input list:                     8 2 1 3 5 9 8
    Sorted list:                    1 2 3 5 8 8 9
"""
from operator import ilshift
from typing import List
from typing import Tuple
import math
import sys
import logging


# Uncomment if you want debug info
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("merge_sort")


def _parse_input(argv: List[str]) -> List[int]:
    return [int(n) for n in argv[1:]]


def merge_sort(unsorted: List[int]) -> List[int]:
    """Wrapper which returns a sorted copy.
    """
    # Create a copy of the list which will be sorted inplace
    tosort_copy = unsorted.copy()
    n = len(tosort_copy)
    if n <=1:
        return tosort_copy
    # For merge sort we need second list to perform the merge
    # Create one list ahead of time and reuse in recursion
    tmp_list = [None] * n
    _merge_sort_inplace(lst=tosort_copy, start=0, end=n, tmp_list=tmp_list)
    return tosort_copy


def _merge_sort_inplace(lst, start, end, tmp_list) -> None:
    """Sorts `lst` recursively inplace using merge sort.

    :param lst: List to be sorted.
    :param start: Index on the left of the list to sort from.
    :param end: Index on the right on the list up to which
        we should sort in this recursion level.
    :param tmp_list: A dummy shared list which will be used to
        copy over elements during the sort.
    """
    n = end - start
    if n == 0:
        raise RuntimeError("Should never occur")
    if n == 1:
        return
    mid = start + (n // 2)
    _merge_sort_inplace(lst=lst, start=start, end=mid, tmp_list=tmp_list)
    _merge_sort_inplace(lst=lst, start=mid, end=end, tmp_list=tmp_list)
    _merge_subroutine(lst=lst, start=start, mid=mid, end=end, tmp_list=tmp_list)


def _merge_subroutine(lst, start, mid, end, tmp_list):
    log.debug(f"\n\nMerge subroutine st, mid, end: \t{[start, mid, end]}")
    log.debug(f"Merge subroutine lft: \t{lst[start:mid]}")
    log.debug(f"Merge subroutine rt: \t{lst[mid:end]}")
    i = start
    j = mid
    k = start
    while i < mid and j < end:
        if lst[i] <= lst[j]:
            tmp_list[k] = lst[i]
            i += 1
            k += 1
        else:
            tmp_list[k] = lst[j]
            j += 1
            k += 1
    while i < mid:
        tmp_list[k] = lst[i]
        i += 1; k += 1
    while j < end:
        tmp_list[j] = lst[j]
        j += 1; k += 1
    for i in range(start, end):
        lst[i] = tmp_list[i]
    log.debug(f"Merge subroutine done: \t{lst[start:end]}")
    


if __name__ == "__main__":
    input_list  = _parse_input(sys.argv)
    sorted_list = merge_sort(input_list)
    log.info("Input list:\t{}".format(" ".join(map(str, input_list))))
    log.info("Sorted list:\t{}".format(" ".join(map(str, sorted_list))))

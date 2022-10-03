"""
Implement partition function used by quicksort

We assume the first element of the array is the pivot element.

Sample input::

    python partition.py 4 1 5 0 6 2 3 8

The output can be any result with the 4 in it's rightful place. Some valid outputs

Sample valid output 1::

    1 0 3 2 4 5 6 8

Sample valid output 2::

    3 1 2 0 4 8 6 5
"""
from typing import List
from typing import Optional
import math
import sys
import logging


# Uncomment if you want debug info
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("partition")



def _parse_int_array(lst: List[str]) -> List[int]:
    return [int(n) for n in lst[1:]]


def partition_inplace(lst: List[int], beg: int = 0, end: Optional[int] = None) -> None:
    if end is None:
        end = len(lst) - 1
    if beg == end:
        return
    pvt = lst[beg]
    edge = beg
    i = beg + 1
    for i in range(beg+1, end+1):
        if lst[i] <= pvt:
            edge += 1
            swap(lst, edge, i)
    swap(lst, beg, edge)
            

def swap(lst: List[int], i: int, j: int) -> None:
    t = lst[i]
    lst[i] = lst[j]
    lst[j] = t


if __name__ == "__main__":
    # Sample inputs: 
    # 4 1 5 0 6 2 3 8
    # 4 1 2 3
    # 4 5 6 7 8 9
    #  4 1 2 5 0 3 9 -1 -2
    input_list  = _parse_int_array(lst=sys.argv)
    output_list = input_list.copy()
    partition_inplace(output_list)
    log.info("Input list:\t{}".format(" ".join(map(str, input_list))))
    log.info("Partitioned list:\t{}".format(" ".join(map(str, output_list))))

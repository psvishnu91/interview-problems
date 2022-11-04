import logging
import sys
from typing import List


def get_logger(name=None) -> logging.Logger:
    # Uncomment if you want debug info
    # logging.basicConfig(level=logging.DEBUG)
    logging.basicConfig(level=logging.INFO)
    name = name or __name__
    return logging.getLogger(name)


def parse_input_array() -> List[int]:
    return parse_int_array(lst=sys.argv)


def parse_int_array(lst: List[str]) -> List[int]:
    """Parse sys.argv to a list of int.

    Sample input::
        
        python x.py 1 2 3 4

        import sys
        parse_int_array(sys.argv)

    Sample output::

        [1 2 3 4]
    """
    return [int(n) for n in lst[1:]]
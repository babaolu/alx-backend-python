#!/usr/bin/env python3
""" Implements function that sums up a list of numbers """
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ sums up the list """
    accum = 0
    for it in mxd_list:
        accum += it
    return accum

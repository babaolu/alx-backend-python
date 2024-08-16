#!/usr/bin/env python3
""" Implements function that sums up a list of floats """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ sums up the list """
    accum = 0
    for it in input_list:
        accum += it
    return accum

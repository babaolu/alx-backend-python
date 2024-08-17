#!/usr/bin/env python3
""" Implements function that creates a tuple """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a Tuple """
    def d_mult(val: float) -> float:
        return val * multiplier
    return d_mult

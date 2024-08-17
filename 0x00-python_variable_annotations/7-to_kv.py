#!/usr/bin/env python3
""" Implements function that creates a tuple """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a Tuple """
    return k, v ** 2

#!/usr/bin/env python3
""" Implements functions that returns the length of each sequence element """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Makes Tuple elements out of Sequence elements """
    return [(i, len(i)) for i in lst]

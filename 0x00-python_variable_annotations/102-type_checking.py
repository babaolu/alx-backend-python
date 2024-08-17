#!/usr/bin/env python3
""" Implements functions that factors a list of numbers """
from typing import Any, List, Union, Sequence


def zoom_array(lst: Sequence, factor: Union[int, float] = 2
               ) -> List[Union[int, float]]:
    """ Factors list of numbers """
    factor = int(factor) if isinstance(factor, float) else factor
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)

#!/usr/bin/env python3
""" Implements functions that returns the length of each sequence element """
from typing import Any, Sequence, Union


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Makes Tuple elements out of Sequence elements """
    if lst:
        return lst[0]
    else:
        return None

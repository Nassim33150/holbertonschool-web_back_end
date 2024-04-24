#!/usr/bin/env python3
from typing import Iterable, List, Tuple


""" Annotate the below function’s
parameters and return values with
the appropriate types """


def element_length(lst: Iterable[str]) -> List[Tuple[str, int]]:
    """ return values with the appropriate types """
    return [(i, len(i)) for i in lst]

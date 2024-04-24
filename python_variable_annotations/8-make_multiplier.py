#!/usr/bin/env python3
"""Type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Function that make a multiplier """

    def multiplier_function(x: float) -> float:
        """ Return x * multiplier """
        return x * multiplier
    """ Return multiplier_function """
    return multiplier_function

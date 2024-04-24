#!/usr/bin/env python3
from typing import Callable


"""Return a function that multiplies a float by a given multiplier."""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Function that make a multiplier """

    def multiplier_function(x: float) -> float:
        """ Return x * multiplier """
        return x * multiplier
    """ Return multiplier_function """
    return multiplier_function

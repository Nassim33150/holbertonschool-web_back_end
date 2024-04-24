#!/usr/bin/python3
from typing import Callable


"""Return a function that multiplies a float by a given multiplier."""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
 
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function

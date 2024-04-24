#!/usr/bin/env python3
from typing import List, Union


"""Calculate the sum of a list of integers and floats."""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of mxd_lst"""
    return sum(mxd_lst)

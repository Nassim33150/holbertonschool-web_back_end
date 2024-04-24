#!/usr/bin/python3
from typing import Union, Tuple


"""Convert a string and an int or float to a tuple."""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, v ** 2)

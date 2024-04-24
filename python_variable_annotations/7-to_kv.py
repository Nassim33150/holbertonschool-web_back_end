#!/usr/bin/env python3
from typing import Union, Tuple


""" Type-annotated function to_kv
that takes a string k and an int
OR float v as arguments and returns a tuple."""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple """
    return (k, v ** 2)

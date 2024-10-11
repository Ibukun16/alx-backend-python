#!/usr/bin/env python3
"""
A type-annotated function that takes a string k
and an int OR float v as arguments and returns a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a key value pair to a tuple of of the keys and
    square of the values.
    """
    return(k, float(v**2))

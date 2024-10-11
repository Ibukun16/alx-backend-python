#!/usr/bin/env python3
"""
Module that annotate the function’s parameters
and return values with the appropriate types.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Compute the length of a list of sequences."""
    return [(n, len(n)) for n in lst]

#!/usr/bin/env python3
"""
A module that augment code with the correct
duck-typed annotations.
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Retrieves the first element of the sequence if it exists"""
    if lst:
        return [0]
    else:
        return None

#!/usr/bin/env python3
"""
A type-annotated function that takes a list of
floats as argument and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Computes the sum of a list of floating-point numbers"""
    return(float(sum(input_list))

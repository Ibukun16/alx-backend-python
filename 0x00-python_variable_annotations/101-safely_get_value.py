#!/usr/bin/env python3
"""
A module that add type annotations to the function,
given the parameters and the return values
"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """ Retrieves a value from the dictionaryusing a particular key"""
    if key in dct:
        return dct[key]
    return default

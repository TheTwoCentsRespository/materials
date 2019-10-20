"""
The linear search algorithm.
"""

from typing import Callable, Optional, Sequence, Union

from search import T, S, identity


def find_index(elements: Sequence[T],
               value: S,
               key: Callable[[T], Union[T, S]] = identity) -> Optional[int]:
    """Return the index of value in elements or None."""
    for i, element in enumerate(elements):
        if key(element) == value:
            return i
    return None


def find(elements: Sequence[T],
         value: S,
         key: Callable[[T], Union[T, S]] = identity) -> Optional[T]:
    """Return an element with matching key or None."""
    index = find_index(elements, value, key)
    return None if index is None else elements[index]


def contains(elements: Sequence[T],
             value: S,
             key: Callable[[T], Union[T, S]] = identity) -> bool:
    """Return True if value is present in elements."""
    return find_index(elements, value, key) is not None
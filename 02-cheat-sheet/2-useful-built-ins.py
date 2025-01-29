#!/usr/bin/env python

# obsolete
# from typing import Dict, List, Set, Tuple, Union, Optional

if __name__ == "__main__":
    x_1: int = 1
    x_2: float = 1.0
    x_3: bool = True
    x_4: str = "test"
    x_5: bytes = b"test"

    # For collections on Python 3.9+, the type of the collection item is in brackets
    x_6: list[int] = [1]
    x_7: set[int] = {6, 7}

    # For mappings, we need the types of both keys and values
    x_8: dict[str, float] = {"field": 2.0}

    # For tuples of fixed size, we specify the types of all the elements
    x_9: tuple[int, str, float] = (3, "yes", 7.5)

    # For tuples of variable size, we use one type and ellipsis
    x_10: tuple[int, ...] = (1, 2, 3)

    # On Python 3.8 and earlier, the name of the collection type is
    # capitalized, and the type is imported from the 'typing' module
    # Obsolete:
    # x_11: List[int] = [1]
    # x_12: Set[int] = {6, 7}
    # x_13: Dict[str, float] = {"field": 2.0}
    # x_14: Tuple[int, str, float] = (3, "yes", 7.5)
    # x_15: Tuple[int, ...] = (1, 2, 3)

    # Use the | operator when something could be one of a few types
    x_16: list[int | str] = [3, 5, "test", "fun"]  # Python 3.10+

    # Union is obsolete
    # x_17: list[Union[int, str]] = [3, 5, "test", "fun"]

    # Use 'X | None' for a value that could be None.
    # Optional[X] is the same as 'X | None' (obsolete).
    x_18: str | None = "something" if True else None

    if x_18:
        # Mypy understands x won't be None here because of the if-statement
        print(x_18.upper())

    # If you know a value can never be None due to some logic that mypy doesn't understand, use an assert!
    assert x_18 is not None
    print(x_18.upper())

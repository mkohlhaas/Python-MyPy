#!/usr/bin/env python

import sys
from collections.abc import Iterable, Mapping, MutableMapping
from typing import IO


# Use Iterable for generic iterables (anything usable in "for"), and
# Sequence where a sequence (supporting "len" and "__getitem__") is required.
def f_1(ints: Iterable[int]) -> list[str]:
    return [str(x) for x in ints]


# Mapping describes a dict-like object (with "__getitem__") that we won't
# mutate, and MutableMapping one (with "__setitem__") that we might
def f_2(my_mapping: Mapping[int, str]) -> list[int]:
    my_mapping[5] = "maybe"  # mypy will complain about this line...
    return list(my_mapping.keys())


def f_3(my_mapping: MutableMapping[int, str]) -> set[int]:
    my_mapping[5] = "maybe"  # ...but mypy is OK with this.
    return set(my_mapping.keys())


# Use IO[str] or IO[bytes] for functions that should accept or return
# objects that come from an open() call (note that IO does not
# distinguish between reading, writing or other modes)
def get_sys_IO(mode: str = "w") -> IO[str]:
    match mode:
        case "w":
            return sys.stdout
        case "r":
            return sys.stdin
        case _:
            return sys.stdout


if __name__ == "__main__":
    f_1(range(1, 3))
    f_2({3: "yes", 4: "no"})
    f_3({3: "yes", 4: "no"})

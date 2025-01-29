#!/usr/bin/env python

# https://mypy.readthedocs.io/en/stable/getting_started.html#more-complex-types

# obsolete:
# from typing import Iterable
from collections.abc import Iterable


def greet_all(names: list[str]) -> None:
    for name in names:
        print("Hello " + name)


def greet_all_1(names: Iterable[str]) -> None:
    for name in names:
        print("Hello " + name)


# union type
def normalize_id(user_id: int | str) -> str:
    if isinstance(user_id, int):
        return f"user-{100_000 + user_id}"
    else:
        return user_id


if __name__ == "__main__":
    names = ["Alice", "Bob", "Charlie"]
    ages = [10, 20, 30]

    greet_all(names)
    greet_all(ages)

    greet_all_1(names)
    greet_all_1(ages)

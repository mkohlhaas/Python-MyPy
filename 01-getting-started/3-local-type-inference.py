#!/usr/bin/env python

# https://mypy.readthedocs.io/en/stable/getting_started.html#local-type-inference

from collections.abc import Iterable


def nums_below(numbers: Iterable[float], limit: float) -> list[float]:
    output: list[float] = []
    for num in numbers:
        if num < limit:
            output.append(num)
    return output


if __name__ == "__main__":
    _ = nums_below([1, 2, 3, 4, 5, 6, 7], 3)

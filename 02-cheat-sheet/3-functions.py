#!/usr/bin/env python

from collections.abc import Iterator, Callable
from typing import reveal_type


def stringify(num: int) -> str:
    return str(num)


def plus(num1: int, num2: int) -> int:
    return num1 + num2


def show(value: str, excitement: int = 10) -> None:
    print(value + "!" * excitement)


# NOTE: Arguments without a type are dynamically typed (treated as Any)
# and that functions without any annotations are not checked
def untyped(x):
    _ = x.anything() + 1 + "string"


# callable value / function
# x takes an int and a float and returns a float.
x: Callable[[int, float], float]


def register(_callback: Callable[[str], int]) -> None: ...


# A generator function that yields ints is secretly just a function that
# returns an iterator of ints, so that's how we annotate it
def gen(n: int) -> Iterator[int]:
    i = 0
    while i < n:
        yield i
        i += 1


def send_email(
    _address: str | list[str],
    _sender: str,
    _cc: list[str] | None,
    _bcc: list[str] | None,
    _subject: str = "",
    _body: list[str] | None = None,
) -> None: ...


# Positional-only arguments can also be marked by using a name starting with `__` (not demonstrated).
def quux(x: int, /, *, y: int) -> None:
    print(x + y)


quux(3, y=5)
quux(3, 5)
quux(x=3, y=5)


def do_api_query(req: str) -> None: ...


def call_someone(*_args: str, **_kwargs: int) -> str:
    return "dummy call"


def call(*args: str, **kwargs: int) -> None:
    reveal_type(args)
    reveal_type(kwargs)
    request = call_someone(*args, **kwargs)
    do_api_query(request)

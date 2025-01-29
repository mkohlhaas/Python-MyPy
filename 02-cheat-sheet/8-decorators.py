#!/usr/bin/env python

from collections.abc import Callable
from typing import Any


# decorator without args
def bare_decorator[F: Callable[..., Any]](_func: F) -> F: ...


# decorator with args
def decorator_args[F: Callable[..., Any]](_url: str) -> Callable[[F], F]: ...


if __name__ == "__main__":
    ...

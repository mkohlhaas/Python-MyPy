#!/usr/bin/env python

# https://mypy.readthedocs.io/en/stable/getting_started.html#dynamic-vs-static-typing


def greeting_1(name):
    return "Hello " + name


def greeting_2(name: str) -> str:
    return "Hello " + name


def bad_greeting(name: str) -> str:
    return "Hello " * name


if __name__ == "__main__":
    # These calls will fail when the program runs, but mypy does not report an error
    # because "greeting" does not have type annotations.
    greeting_1(123)
    greeting_1(b"Alice")

    greeting_2(123)
    greeting_2(b"Alice")
    _ = greeting_2("Michael")

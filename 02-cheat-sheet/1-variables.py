#!/usr/bin/env python


if __name__ == "__main__":
    # no value at runtime until assigned
    a: int

    age: int = 1

    child: bool
    if age < 18:
        child = True
    else:
        child = False

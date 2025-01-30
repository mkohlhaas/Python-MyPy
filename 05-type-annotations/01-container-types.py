#!/usr/bin/env python


# not allowed ...
def f_1(objects: list[object], ints: list[int]) -> None:
    objects = ints
    print(objects)


# ... because you could write a non-int into a list of int:
def f_2(objects: list[object], ints: list[int]) -> None:
    objects = ints
    objects.append("x")
    print(ints[-1])  # Ouch; a string in list[int]


if __name__ == "__main__":
    ...

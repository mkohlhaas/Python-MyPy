#!/usr/bin/env python

# If you add the following special import you can use forward references!
from __future__ import annotations


# You may want to reference a class before it is defined.
# This is known as a "forward reference".
def f_1(_foo: A) -> int:
    return 42


# It will work at runtime and type checking will succeed as long as there
# is a class of that name later on in the file
def f_2(_foo: A) -> int:
    return 42


# Another option is to just put the type in quotes
def f(_foo: "A") -> int:
    return 42


# This can also come up if you need to reference a class in a type
# annotation inside the definition of that class.
class A:
    @classmethod
    def create(cls) -> A:
        return A()


if __name__ == "__main__":
    ...

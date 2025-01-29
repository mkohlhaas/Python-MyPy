#!/usr/bin/env python

from typing import Any, TYPE_CHECKING, cast, reveal_type

# To find out what type mypy infers for an expression anywhere in
# your program, wrap it in reveal_type().  Mypy will print an error
# message with the type.
# Remove it again before running the code!!!
reveal_type(1)

# If you initialize a variable with an empty container or "None"
# you may have to help mypy a bit by providing an explicit type annotation
x_1: list[str] = []
x_2: str | None = None


def mystery_function(): ...


# Use Any if you don't know the type of something or it's too dynamic to write a type for.
x_3: Any = mystery_function()

# Mypy will let you do anything with x!
_ = x_3.whatever() * x_3["you"] + x_3("want") - any(x_3) and all(x_3) is super


def confusing_function() -> str | int | float | None: ...


# Use a "type: ignore" comment to suppress errors on a given line,
# when your code confuses mypy or runs into an outright bug in mypy.
# Good practice is to add a comment explaining the issue.
x = confusing_function()  # type: ignore  # confusing_function won't return None here because ...

# "cast" is a helper function that lets you override the inferred type of an expression.
# It's only for mypy -- there's no runtime check.
a = [4]
b = cast(list[int], a)  # Passes fine
c = cast(list[str], a)  # Passes fine despite being a lie (no runtime check)
reveal_type(c)  # Revealed type is "builtins.list[builtins.str]"
print(c)  # Still prints [4] ... the object is not changed or casted at runtime

# Use "TYPE_CHECKING" if you want to have code that mypy can see but will not
# be executed at runtime (or to have code that mypy can't see)
if TYPE_CHECKING:
    pass
else:
    pass  # mypy is unaware of this

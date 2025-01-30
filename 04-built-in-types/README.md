## Built-in types 

- [Built-in types](https://mypy.readthedocs.io/en/stable/builtin_types.html)

- ### Simple Types

Type| Description
---|---
int |integer
float| floating point number
bool |boolean value (subclass of int)
str |text, sequence of unicode codepoints
bytes| 8-bit string, sequence of byte values
object| an arbitrary object (object is the common base class)

- ### Generic Types

Type| Description
---|---
list[str]| list of str objects
tuple[int, int]| tuple of two int objects (tuple[()] is the empty tuple)
tuple[int, ...]| tuple of an arbitrary number of int objects
dict[str, int]| dictionary from str keys to int values
Iterable[int]| iterable object containing ints
Sequence[bool]| sequence of booleans (read-only)
Mapping[str, int]| mapping from str keys to int values (read-only)
type[C]| **type object of C** (C is a class/type variable/union of types)

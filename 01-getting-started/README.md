### Getting started

- [Getting started](https://mypy.readthedocs.io/en/stable/getting_started.html)

### Installation

```shell
sudo pacman -S mypy
```

### Command Line Flags

- --strict
- --disallow-untyped-defs 
- --check-untyped-defs
- --ignore-missing-imports

### Notes

- When adding types, the convention is to import types using the form `from typing import <name>` as opposed to doing just import typing or `import typing as t` or `from typing import *`.
- In some examples we use capitalized variants of types, such as `List`, and sometimes we use plain `list`. They are equivalent, but the prior variant is needed if you are using Python 3.8 or earlier.

- [Typeshed: Typing Stubs for mypy](https://github.com/python/typeshed/)

- basedpyright: Config param: `typeshedPath` [path, optional]: Path to a directory that contains typeshed type stub files. `Pyright ships with a bundled copy of typeshed type stubs.` If you want to use a different version of typeshed stubs, you can clone the typeshed github repo to a local directory and reference the location with this path. This option is useful if you’re actively contributing updates to typeshed.

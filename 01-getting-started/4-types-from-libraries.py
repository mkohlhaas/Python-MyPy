#!/usr/bin/env python

# https://mypy.readthedocs.io/en/stable/getting_started.html#types-from-libraries

from pathlib import Path


def load_template(template_path: Path, name: str) -> str:
    template = template_path.read_text()
    return template.replace("USERNAME", name)


if __name__ == "__main__":
    _ = load_template(Path("4-types-from-libraries.py"), "Michael")

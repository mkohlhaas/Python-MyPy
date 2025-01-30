[Using mypy with an existing codebase](https://mypy.readthedocs.io/en/stable/existing_code.html)

### Automatic Stub Generation
- [MonkeyType](https://github.com/instagram/MonkeyType)
- [autotyping](https://github.com/JelleZijlstra/autotyping)

### Test Automation#

- [nox](https://github.com/wntrblm/nox)
- [tox](https://tox.wiki/)

An excellent goal to aim for is to have your codebase pass when run against
`mypy --strict`. This basically ensures that you will never have a type related
error without an explicit circumvention somewhere (such as a `# type: ignore`
comment).

- [Mypy Daemon](https://mypy.readthedocs.io/en/stable/mypy_daemon.html#mypy-daemon)

# Template for Python Package

This repository provides a template for python package.

This repository uses [uv](https://github.com/astral-sh/uv) for project management.

## Prepare

1. Install [uv](https://github.com/astral-sh/uv).
1. Replace the keyword in the `pyproject.toml`.
   - `PACKAGE_NAME`: package's name
   - `PACKAGE_DESCRIPTION`: package's description
   - `USERNAME`: package's author
1. Update other content in the `pyproject.toml`.
1. Implement `src` and `test` directories.

## Development

Install require libraries.

```sh
uv sync --group dev
```

## Testing

Install require libraries.

```sh
uv sync --group test
```

Execute test code.

```sh
uv run tox
```

## Documentation

Install require libraries.

```sh
uv sync --group doc
```

Generate API document.

```sh
uv run sphinx-apidoc -F -f -a -H PROJECT -A AUTHOR -V VERSION -o doc src
cd doc
uv run make html
```

## Building package

Build `sdist` and `bdist`.

```sh
uv build
```

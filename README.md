# Redfish Service for Python

This repository provides Redfish service library and entry script.

## Install

Intall library and entry script.

```sh
pip install git+https://github.com/9506hqwy/redfish-service-py.git
```

## Execute

Start up service.

```sh
redfish-service
```

## Development

Install dependencies libraries.

```sh
uv sync --all-groups
```

Run test.

```sh
uv run tox
```

Start up service.

```sh
uv run redfish-service
```

Validate protocol after running service.

```sh
uv run rf_protocol_validator -u admin -p admin -r http://127.0.0.1:8000
```

Validate service after running service.

```sh
uv run rf_service_validator -u admin -p admin -r http://127.0.0.1:8000
```

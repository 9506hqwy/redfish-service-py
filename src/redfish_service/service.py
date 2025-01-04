from __future__ import annotations  # PEP563 Forward References

from typing import Any, Protocol

from .exception import OperationNotAllowedError
from .model import RedfishModel

services: list[Service] = []


def find_service[T: RedfishModel](ty: type[T]) -> Service:
    for s in services:
        if s.respond(ty):
            return s

    raise OperationNotAllowedError


def registry_service(s: Service) -> None:
    services.append(s)


class Service[T: RedfishModel](Protocol):
    def respond(self, ty: type[RedfishModel]) -> bool: ...

    def delete(self, **kwargs: dict[str, Any]) -> T:
        raise OperationNotAllowedError

    def get(self, **kwargs: dict[str, Any]) -> T:
        raise OperationNotAllowedError

    def insert(self, **kwargs: dict[str, Any]) -> T:
        raise OperationNotAllowedError

    def list(self, **kwargs: dict[str, Any]) -> list[T]:
        raise OperationNotAllowedError

    def update(self, **kwargs: dict[str, Any]) -> T:
        raise OperationNotAllowedError

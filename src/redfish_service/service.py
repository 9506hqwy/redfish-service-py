from __future__ import annotations  # PEP563 Forward References

from typing import Any, Protocol, cast

from .exception import OperationNotAllowedError
from .model import RedfishModel

services: list[Service] = []


def find_service[T: RedfishModel](ty: type[T]) -> Service:
    for s in services:
        if s.respond(ty):
            return s

    raise OperationNotAllowedError


def find_service_collection[T: RedfishModel](ty: type[T]) -> ServiceCollection:
    for s in services:
        if s.respond(ty):
            return cast(ServiceCollection, s)

    raise OperationNotAllowedError


def registry_service(s: Service) -> None:
    services.append(s)


class Service[T: RedfishModel](Protocol):
    def respond(self, ty: type[RedfishModel]) -> bool: ...

    def delete(self, **kwargs: dict[str, Any]) -> None:
        raise OperationNotAllowedError

    def get(self, **kwargs: dict[str, Any]) -> T:
        raise OperationNotAllowedError

    def patch(self, **kwargs: dict[str, Any]) -> T:
        raise OperationNotAllowedError


class ServiceCollection[T: RedfishModel, I: RedfishModel](Service[T], Protocol):
    def post(self, **kwargs: dict[str, Any]) -> I:
        raise OperationNotAllowedError

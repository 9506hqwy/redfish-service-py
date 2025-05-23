from __future__ import annotations  # PEP563 Forward References

from typing import Any, Protocol, cast

from .exception import OperationNotAllowedError
from .model import RedfishModel
from .model.redfish_error import RedfishError

services: list[Service] = []


def find_service[T: RedfishModel](ty: type[T]) -> Service | None:
    for s in services:
        if s.respond(ty):
            return s

    return None


def find_service_collection[T: RedfishModel](ty: type[T]) -> ServiceCollection | None:
    for s in services:
        if s.respond(ty):
            return cast(ServiceCollection, s)

    return None


def registry_service(s: Service) -> None:
    services.append(s)


class Service[T: RedfishModel](Protocol):
    def respond(self, ty: type[RedfishModel]) -> bool: ...

    def delete(self, **kwargs: dict[str, Any]) -> None:
        raise OperationNotAllowedError(self)

    def get(self, **kwargs: dict[str, Any]) -> T:
        raise OperationNotAllowedError(self)

    def patch(self, **kwargs: dict[str, Any]) -> T:
        raise OperationNotAllowedError(self)

    def action(self, **kwargs: dict[str, Any]) -> RedfishError:
        raise OperationNotAllowedError(self)


class ServiceCollection[T: RedfishModel, I: RedfishModel](Service[T], Protocol):
    def post(self, **kwargs: dict[str, Any]) -> I:
        raise OperationNotAllowedError(self)

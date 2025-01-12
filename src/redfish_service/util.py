from __future__ import annotations  # PEP563 Forward References

from fastapi import Request

from .exception import InvalidURIError
from .model import RedfishModel
from .service import Service, ServiceCollection, find_service, find_service_collection


def get_service[T: RedfishModel](ty: type[T], req: Request) -> Service:
    if s := find_service(ty):
        return s

    raise InvalidURIError(req.url.path)


def get_service_collection[T: RedfishModel](ty: type[T], req: Request) -> ServiceCollection:
    if s := find_service_collection(ty):
        return s

    raise InvalidURIError(req.url.path)

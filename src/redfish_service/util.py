from __future__ import annotations  # PEP563 Forward References

from datetime import datetime
from typing import cast

from fastapi import Request, Response

from .exception import InvalidURIError
from .model import RedfishModel
from .service import Service, ServiceCollection, find_service, find_service_collection


def create_etag() -> str:
    return f"{datetime.now().timestamp()!s}"


def get_service[T: RedfishModel](ty: type[T], req: Request) -> Service:
    if s := find_service(ty):
        return s

    raise InvalidURIError(req.url.path)


def get_service_collection[T: RedfishModel](ty: type[T], req: Request) -> ServiceCollection:
    if s := find_service_collection(ty):
        return s

    raise InvalidURIError(req.url.path)


def set_link_header[T: RedfishModel](model: T, res: Response) -> None:
    if ty := getattr(model, "odata_type", None):
        name = cast(str, ty)[1:]
        res.headers.append("Link", f"</redfish/v1/JsonSchemas/{name}.json>; rel=describedby")

from typing import Any, cast

from fastapi import Request

from ..exception import ResourceNotFoundError
from ..model.service_root import ServiceRoot
from ..repository import instances
from ..service import Service


class ServiceRootService(Service[ServiceRoot]):
    def respond(self, ty: type) -> bool:
        return ty == ServiceRoot

    def get(self, **kwargs: dict[str, Any]) -> ServiceRoot:
        i = instances.find_by_type(ServiceRoot)
        if i is None:
            raise ResourceNotFoundError("ServiceRoot", "ServiceRoot")

        req: Request = cast(Request, kwargs["request"])
        i.odata_id = req.url.path

        return i

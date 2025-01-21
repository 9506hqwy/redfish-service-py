from typing import Any, cast

from fastapi import Request, Response

from ..exception import ResourceNotFoundError
from ..model.account_service import AccountService
from ..model.odata_v4 import IdRef
from ..model.service_root import ServiceRoot
from ..repository import instances
from ..service import Service


class ServiceRootService(Service[ServiceRoot]):
    def respond(self, ty: type) -> bool:
        return ty == ServiceRoot

    def get(self, **kwargs: dict[str, Any]) -> ServiceRoot:
        account_service = instances.find_by_type(AccountService)

        i = instances.find_by_type(ServiceRoot)
        if i is None:
            raise ResourceNotFoundError("ServiceRoot", "ServiceRoot")

        if account_service:
            i.account_service = IdRef(odata_id=account_service.odata_id)

        req = cast(Request, kwargs["request"])
        i.odata_id = req.url.path

        res = cast(Response, kwargs["response"])
        res.headers["ETag"] = f'"{i.odata_etag}"'

        return i

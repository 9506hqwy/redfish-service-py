from typing import Any, cast

from fastapi import Response

from ..exception import ResourceNotFoundError
from ..model.account_service import AccountService
from ..repository import instances
from ..service import Service


class AccountServiceService(Service[AccountService]):
    def respond(self, ty: type) -> bool:
        return ty == AccountService

    def get(self, **kwargs: dict[str, Any]) -> AccountService:
        res = cast(Response, kwargs["response"])

        i = instances.find_by_type(AccountService)
        if i is None:
            raise ResourceNotFoundError("ServiceRoot", "ServiceRoot")

        res.headers["ETag"] = f'"{i.odata_etag}"'

        return i

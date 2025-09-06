from typing import Any, cast

from fastapi import Response

from ..exception import ResourceNotFoundError
from ..model.manager_account import ManagerAccount
from ..repository import instances
from ..service import Service


class ManagerAccountService(Service[ManagerAccount]):
    def respond(self, ty: type) -> bool:
        return ty == ManagerAccount

    def get(self, **kwargs: dict[str, Any]) -> ManagerAccount:
        res = cast(Response, kwargs["response"])

        manager_coount_id = cast(str, kwargs.get("manager_account_id"))
        a = self._get_by_id(manager_coount_id)

        res.headers["ETag"] = f'"{a.odata_etag}"'

        return a

    def _get_by_id(self, account_id: str) -> ManagerAccount:
        a = next((a for a in instances.enum_by_type(ManagerAccount) if a.id == account_id), None)
        if a is None:
            raise ResourceNotFoundError("ManagerAccount", account_id)

        return a

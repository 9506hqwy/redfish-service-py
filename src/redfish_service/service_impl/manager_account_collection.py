from typing import Any, cast

from fastapi import Request, Response

from ..exception import ResourceNotFoundError
from ..model.manager_account import ManagerAccount
from ..model.manager_account_collection import ManagerAccountCollection
from ..model.odata_v4 import IdRef
from ..repository import instances
from ..service import ServiceCollection


class ManagerAccountCollectionService(ServiceCollection[ManagerAccountCollection, ManagerAccount]):
    def respond(self, ty: type) -> bool:
        return ty == ManagerAccountCollection

    def get(self, **kwargs: dict[str, Any]) -> ManagerAccountCollection:
        req = cast(Request, kwargs["request"])
        res = cast(Response, kwargs["response"])

        i = self._get_by_type()
        i.members = [IdRef(odata_id=s.odata_id) for s in instances.enum_by_type(ManagerAccount)]
        i.members_odata_count = len(i.members)
        i.odata_id = req.url.path

        res.headers["ETag"] = f'"{i.odata_etag}"'

        return i

    def _get_by_type(self) -> ManagerAccountCollection:
        i = instances.find_by_type(ManagerAccountCollection)
        if i is None:
            raise ResourceNotFoundError("ManagerAccountCollection", "ManagerAccountCollection")

        return i

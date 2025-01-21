from http import HTTPStatus
from typing import Any, cast

from fastapi import Request, Response

from ..exception import ResourceNotFoundError
from ..model.odata_v4 import IdRef
from ..model.role import Role, RoleOnCreate
from ..model.role_collection import RoleCollection
from ..repository import instances
from ..service import ServiceCollection
from ..util import create_etag


class RoleCollectionService(ServiceCollection[RoleCollection, Role]):
    def respond(self, ty: type) -> bool:
        return ty == RoleCollection

    def get(self, **kwargs: dict[str, Any]) -> RoleCollection:
        res = cast(Response, kwargs["response"])

        i = self._get_by_type()
        i.members = [IdRef(odata_id=s.odata_id) for s in instances.enum_by_type(Role)]
        i.members_odata_count = len(i.members)

        req = cast(Request, kwargs["request"])
        i.odata_id = req.url.path

        res.headers["ETag"] = f'"{i.odata_etag}"'

        return i

    def post(self, **kwargs: dict[str, Any]) -> Role:
        body = cast(RoleOnCreate, kwargs.get("body"))
        req = cast(Request, kwargs["request"])
        res = cast(Response, kwargs["response"])

        collection = self._get_by_type()

        etag = create_etag()
        id = body.role_id
        role = Role(odata_etag=etag, odata_id=f"{req.url.path}/{id}", id=id, name=id, role_id=id)

        instances.add(role)
        collection.odata_etag = etag

        res.headers["ETag"] = f'"{etag}"'
        res.headers["Location"] = role.odata_id
        res.status_code = HTTPStatus.CREATED

        return role

    def _get_by_type(self) -> RoleCollection:
        i = instances.find_by_type(RoleCollection)
        if i is None:
            raise ResourceNotFoundError("RoleCollection", "RoleCollection")

        return i

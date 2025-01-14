from http import HTTPStatus
from typing import Any, cast

from fastapi import Request, Response

from ..exception import ResourceNotFoundError
from ..model.odata_v4 import IdRef
from ..model.role import Role, RoleOnCreate
from ..model.role_collection import RoleCollection
from ..repository import instances
from ..service import ServiceCollection


class RoleCollectionService(ServiceCollection[RoleCollection, Role]):
    def respond(self, ty: type) -> bool:
        return ty == RoleCollection

    def get(self, **kwargs: dict[str, Any]) -> RoleCollection:
        i = instances.find_by_type(RoleCollection)
        if i is None:
            raise ResourceNotFoundError("RoleCollection", "RoleCollection")

        i.members = [IdRef(odata_id=s.odata_id) for s in instances.enum_by_type(Role)]
        i.members_odata_count = len(i.members)

        req: Request = cast(Request, kwargs["request"])
        i.odata_id = req.url.path

        return i

    def post(self, **kwargs: dict[str, Any]) -> Role:
        body: RoleOnCreate = cast(RoleOnCreate, kwargs.get("body"))
        req: Request = cast(Request, kwargs["request"])
        res: Response = cast(Response, kwargs["response"])

        role = Role(odata_id=f"{req.url.path}/{body.role_id}", id=body.role_id, name=body.role_id)
        instances.add(role)

        res.headers["Location"] = role.odata_id
        res.status_code = HTTPStatus.CREATED

        return role

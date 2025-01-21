from http import HTTPStatus
from typing import Any, cast

from fastapi import Response

from ..exception import ResourceNotFoundError
from ..model.role import Role, RoleOnUpdate
from ..model.role_collection import RoleCollection
from ..repository import instances
from ..service import Service
from ..util import create_etag


class RoleService(Service[Role]):
    def respond(self, ty: type) -> bool:
        return ty == Role

    def delete(self, **kwargs: dict[str, Any]) -> None:
        role_id = cast(str, kwargs.get("role_id"))
        res = cast(Response, kwargs["response"])

        collection = self._get_collection()

        etag = create_etag()
        r = self._get_by_id(role_id)

        instances.remove(r)
        collection.odata_etag = etag

        res.status_code = HTTPStatus.NO_CONTENT

    def get(self, **kwargs: dict[str, Any]) -> Role:
        res = cast(Response, kwargs["response"])

        role_id = cast(str, kwargs.get("role_id"))
        r = self._get_by_id(role_id)

        res.headers["ETag"] = f'"{r.odata_etag}"'

        return r

    def patch(self, **kwargs: dict[str, Any]) -> Role:
        res = cast(Response, kwargs["response"])

        role_id = cast(str, kwargs.get("role_id"))
        updated = cast(RoleOnUpdate, kwargs.get("body"))

        r = self._get_by_id(role_id)

        # TODO: check
        etag = create_etag()
        r.odata_etag = etag
        r.assigned_privileges = updated.assigned_privileges
        r.oem_privileges = updated.oem_privileges

        res.headers["ETag"] = f'"{etag}"'

        return r

    def _get_by_id(self, id: str) -> Role:
        r = next((r for r in instances.enum_by_type(Role) if r.id == id), None)
        if r is None:
            raise ResourceNotFoundError("Role", id)

        return r

    def _get_collection(self) -> RoleCollection:
        i = instances.find_by_type(RoleCollection)
        if i is None:
            raise ResourceNotFoundError("RoleCollection", "RoleCollection")

        return i

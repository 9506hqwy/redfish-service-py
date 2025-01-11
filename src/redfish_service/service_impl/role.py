from http import HTTPStatus
from typing import Any, cast

from fastapi import Response

from ..exception import ResourceNotFoundError
from ..model.role import Role, RoleOnUpdate
from ..repository import instances
from ..service import Service


class RoleService(Service[Role]):
    def respond(self, ty: type) -> bool:
        return ty == Role

    def delete(self, **kwargs: dict[str, Any]) -> None:
        role_id = cast(str, kwargs.get("role_id"))
        res: Response = cast(Response, kwargs["response"])

        r = self._get_by_id(role_id)
        instances.remove(r)

        res.status_code = HTTPStatus.NO_CONTENT

    def get(self, **kwargs: dict[str, Any]) -> Role:
        role_id = cast(str, kwargs.get("role_id"))
        return self._get_by_id(role_id)

    def patch(self, **kwargs: dict[str, Any]) -> Role:
        role_id = cast(str, kwargs.get("role_id"))
        updated = cast(RoleOnUpdate, kwargs.get("body"))

        r = self._get_by_id(role_id)

        # TODO: check
        r.assigned_privileges = updated.assigned_privileges
        r.oem_privileges = updated.oem_privileges

        return r

    def _get_by_id(self, id: str) -> Role:
        r = next((r for r in instances.enum_by_type(Role) if r.id == id), None)
        if r is None:
            raise ResourceNotFoundError("Role", id)

        return r

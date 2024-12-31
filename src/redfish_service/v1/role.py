from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .privileges import PrivilegeType


class Actions(RedfishResource):
    oem: OemActions | None = None


class OemActions(RedfishResource):
    pass


class Role(RedfishResource):
    actions: Actions | None = None
    alternate_role_id: str | None = None
    assigned_privileges: list[PrivilegeType] | None = None
    description: str | None = None
    is_predefined: bool | None = None
    oem: dict[str, Any] | None = None
    oem_privileges: list[str] | None = None
    restricted: bool | None = None
    role_id: str | None = None

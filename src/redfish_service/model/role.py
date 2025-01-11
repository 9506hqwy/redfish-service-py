from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .privileges import PrivilegeType


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Role(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#Role.v1_3_2.Role")
    actions: Actions | None = None
    alternate_role_id: str | None = None
    assigned_privileges: list[PrivilegeType] | None = None
    description: str | None = None
    id: str
    is_predefined: bool | None = None
    name: str
    oem: dict[str, Any] | None = None
    oem_privileges: list[str] | None = None
    restricted: bool | None = None
    role_id: str | None = None


class RoleOnCreate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(alias="@odata.type", default="#Role.v1_3_2.Role")
    actions: Actions | None = None
    alternate_role_id: str | None = None
    assigned_privileges: list[PrivilegeType] | None = None
    description: str | None = None
    id: str | None = None
    is_predefined: bool | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    oem_privileges: list[str] | None = None
    restricted: bool | None = None
    role_id: str | None = None


class RoleOnUpdate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(alias="@odata.type", default="#Role.v1_3_2.Role")
    actions: Actions | None = None
    alternate_role_id: str | None = None
    assigned_privileges: list[PrivilegeType] | None = None
    description: str | None = None
    id: str | None = None
    is_predefined: bool | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    oem_privileges: list[str] | None = None
    restricted: bool | None = None
    role_id: str | None = None

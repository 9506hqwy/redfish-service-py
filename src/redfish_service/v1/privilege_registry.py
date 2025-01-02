from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
)
from .privileges import PrivilegeType


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Mapping(RedfishModel):
    entity: str | None = None
    operation_map: OperationMap | None = None
    property_overrides: list[TargetPrivilegeMap] | None = None
    resource_uri_overrides: list[TargetPrivilegeMap] | None = Field(
        alias="ResourceURIOverrides", default=None
    )
    subordinate_overrides: list[TargetPrivilegeMap] | None = None


class OperationMap(RedfishModel):
    delete: list[OperationPrivilege] | None = Field(alias="DELETE", default=None)
    get: list[OperationPrivilege] | None = Field(alias="GET", default=None)
    head: list[OperationPrivilege] | None = Field(alias="HEAD", default=None)
    patch: list[OperationPrivilege] | None = Field(alias="PATCH", default=None)
    post: list[OperationPrivilege] | None = Field(alias="POST", default=None)
    put: list[OperationPrivilege] | None = Field(alias="PUT", default=None)


class OperationPrivilege(RedfishModel):
    privilege: list[str] | None = None


class PrivilegeRegistry(RedfishModel):
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    description: str | None = None
    id: str
    mappings: list[Mapping] | None = None
    name: str
    oem_privileges_used: list[str] | None = Field(alias="OEMPrivilegesUsed", default=None)
    oem: dict[str, Any] | None = None
    privileges_used: list[PrivilegeType] | None = None


class TargetPrivilegeMap(RedfishModel):
    operation_map: OperationMap | None = None
    targets: list[str] | None = None

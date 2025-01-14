from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .privileges import PrivilegeType


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Mapping(RedfishModel):
    entity: str | None = None
    operation_map: OperationMap | None = None
    property_overrides: list[TargetPrivilegeMap] | None = None
    resource_uri_overrides: list[TargetPrivilegeMap] | None = Field(
        serialization_alias="ResourceURIOverrides", default=None
    )
    subordinate_overrides: list[TargetPrivilegeMap] | None = None


class OperationMap(RedfishModel):
    delete: list[OperationPrivilege] | None = Field(serialization_alias="DELETE", default=None)
    get: list[OperationPrivilege] | None = Field(serialization_alias="GET", default=None)
    head: list[OperationPrivilege] | None = Field(serialization_alias="HEAD", default=None)
    patch: list[OperationPrivilege] | None = Field(serialization_alias="PATCH", default=None)
    post: list[OperationPrivilege] | None = Field(serialization_alias="POST", default=None)
    put: list[OperationPrivilege] | None = Field(serialization_alias="PUT", default=None)


class OperationPrivilege(RedfishModel):
    privilege: list[str] | None = None


class PrivilegeRegistry(RedfishModel):
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#PrivilegeRegistry.v1_1_5.PrivilegeRegistry"
    )
    actions: Actions | None = None
    description: str | None = None
    id: str
    mappings: list[Mapping] | None = None
    name: str
    oem_privileges_used: list[str] | None = Field(
        serialization_alias="OEMPrivilegesUsed", default=None
    )
    oem: dict[str, Any] | None = None
    privileges_used: list[PrivilegeType] | None = None


class TargetPrivilegeMap(RedfishModel):
    operation_map: OperationMap | None = None
    targets: list[str] | None = None

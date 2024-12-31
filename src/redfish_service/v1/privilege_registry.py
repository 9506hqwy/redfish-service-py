from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
)
from .privileges import PrivilegeType


class Actions(RedfishModel):
    oem: OemActions | None = None


class Mapping(RedfishModel):
    entity: str | None = None
    operation_map: OperationMap | None = None
    property_overrides: list[TargetPrivilegeMap] | None = None
    resource_urioverrides: list[TargetPrivilegeMap] | None = None
    subordinate_overrides: list[TargetPrivilegeMap] | None = None


class OemActions(RedfishModel):
    pass


class OperationMap(RedfishModel):
    delete: list[OperationPrivilege] | None = None
    get: list[OperationPrivilege] | None = None
    head: list[OperationPrivilege] | None = None
    patch: list[OperationPrivilege] | None = None
    post: list[OperationPrivilege] | None = None
    put: list[OperationPrivilege] | None = None


class OperationPrivilege(RedfishModel):
    privilege: list[str] | None = None


class PrivilegeRegistry(RedfishModel):
    actions: Actions | None = None
    description: str | None = None
    id: str
    mappings: list[Mapping] | None = None
    name: str
    oemprivileges_used: list[str] | None = None
    oem: dict[str, Any] | None = None
    privileges_used: list[PrivilegeType] | None = None


class TargetPrivilegeMap(RedfishModel):
    operation_map: OperationMap | None = None
    targets: list[str] | None = None

from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .privileges import PrivilegeType


class Actions(RedfishResource):
    oem: OemActions | None = None


class Mapping(RedfishResource):
    entity: str | None = None
    operation_map: OperationMap | None = None
    property_overrides: list[TargetPrivilegeMap] | None = None
    resource_urioverrides: list[TargetPrivilegeMap] | None = None
    subordinate_overrides: list[TargetPrivilegeMap] | None = None


class OemActions(RedfishResource):
    pass


class OperationMap(RedfishResource):
    delete: list[OperationPrivilege] | None = None
    get: list[OperationPrivilege] | None = None
    head: list[OperationPrivilege] | None = None
    patch: list[OperationPrivilege] | None = None
    post: list[OperationPrivilege] | None = None
    put: list[OperationPrivilege] | None = None


class OperationPrivilege(RedfishResource):
    privilege: list[str] | None = None


class PrivilegeRegistry(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    mappings: list[Mapping] | None = None
    oemprivileges_used: list[str] | None = None
    oem: dict[str, Any] | None = None
    privileges_used: list[PrivilegeType] | None = None


class TargetPrivilegeMap(RedfishResource):
    operation_map: OperationMap | None = None
    targets: list[str] | None = None

from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..odata_v4 import IdRef
from ..resource import Identifier, Status
from ..swordfish.storage_replica_info import ReplicaInfo


class AccessCapability(StrEnum):
    READ = "Read"
    READ_WRITE = "ReadWrite"


class Actions(RedfishModel):
    oem: OemActions | None = None


class ExposeVolumes(RedfishModel):
    target: str | None = None
    title: str | None = None


class HideVolumes(RedfishModel):
    target: str | None = None
    title: str | None = None


class Links(RedfishModel):
    child_storage_groups: list[StorageGroup] | None = None
    class_of_service: IdRef | None = None
    oem: dict[str, Any] | None = None
    parent_storage_groups: list[StorageGroup] | None = None


class MappedVolume(RedfishModel):
    access_capability: str | None = None
    logical_unit_number: str | None = None
    volume: IdRef | None = None


class OemActions(RedfishModel):
    pass


class StorageGroup(RedfishResource):
    access_state: str | None = None
    actions: Actions | None = None
    authentication_method: str | None = None
    chap_info: list[str] | None = None
    client_endpoint_groups: list[IdRef] | None = None
    dhchap_info: list[str] | None = None
    description: str | None = None
    identifier: Identifier | None = None
    links: Links | None = None
    mapped_volumes: list[str] | None = None
    members_are_consistent: str | None = None
    oem: dict[str, Any] | None = None
    replica_info: ReplicaInfo | None = None
    replica_targets: list[IdRef] | None = None
    server_endpoint_groups: list[IdRef] | None = None
    status: Status | None = None
    volumes: list[IdRef] | None = None
    volumes_are_exposed: str | None = None

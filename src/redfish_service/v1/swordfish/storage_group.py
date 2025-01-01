from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

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
    expose_volumes: ExposeVolumes | None = Field(alias="#StorageGroup.ExposeVolumes", default=None)
    hide_volumes: HideVolumes | None = Field(alias="#StorageGroup.HideVolumes", default=None)
    oem: dict[str, Any] | None = None


class ExposeVolumes(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class HideVolumes(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Links(RedfishModel):
    child_storage_groups: list[StorageGroup] | None = None
    child_storage_groups_odata_count: int | None = Field(
        alias="ChildStorageGroups@odata.count", default=None
    )
    class_of_service: IdRef | None = None
    oem: dict[str, Any] | None = None
    parent_storage_groups: list[StorageGroup] | None = None
    parent_storage_groups_odata_count: int | None = Field(
        alias="ParentStorageGroups@odata.count", default=None
    )


class MappedVolume(RedfishModel):
    access_capability: str | None = None
    logical_unit_number: str | None = None
    volume: IdRef | None = None


class StorageGroup(RedfishResource):
    access_state: str | None = None
    actions: Actions | None = None
    authentication_method: str | None = None
    chap_info: list[str] | None = None
    client_endpoint_groups: list[IdRef] | None = None
    client_endpoint_groups_odata_count: int | None = Field(
        alias="ClientEndpointGroups@odata.count", default=None
    )
    dhchap_info: list[str] | None = Field(alias="DHChapInfo", default=None)
    description: str | None = None
    identifier: Identifier | None = None
    links: Links | None = None
    mapped_volumes: list[str] | None = None
    members_are_consistent: str | None = None
    oem: dict[str, Any] | None = None
    replica_info: ReplicaInfo | None = None
    replica_targets: list[IdRef] | None = None
    replica_targets_odata_count: int | None = Field(
        alias="ReplicaTargets@odata.count", default=None
    )
    server_endpoint_groups: list[IdRef] | None = None
    server_endpoint_groups_odata_count: int | None = Field(
        alias="ServerEndpointGroups@odata.count", default=None
    )
    status: Status | None = None
    volumes: list[IdRef] | None = None
    volumes_odata_count: int | None = Field(alias="Volumes@odata.count", default=None)
    volumes_are_exposed: str | None = None

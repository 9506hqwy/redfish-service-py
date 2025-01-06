from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .. import RedfishModel
from ..endpoint_group import AccessState
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


class AuthenticationMethod(StrEnum):
    NONE = "None"
    CHAP = "CHAP"
    MUTUAL_CHAP = "MutualCHAP"
    DHCHAP = "DHCHAP"


class ChapInformation(RedfishModel):
    chap_password: str | None = Field(alias="CHAPPassword", default=None)
    chap_user: str | None = Field(alias="CHAPUser", default=None)
    initiator_chap_password: str | None = Field(alias="InitiatorCHAPPassword", default=None)
    initiator_chap_user: str | None = Field(alias="InitiatorCHAPUser", default=None)
    target_chap_password: str | None = Field(alias="TargetCHAPPassword", default=None)
    target_chap_user: str | None = Field(alias="TargetCHAPUser", default=None)
    target_password: str | None = None


class DhchapInformation(RedfishModel):
    local_dhchap_auth_secret: str | None = Field(alias="LocalDHCHAPAuthSecret", default=None)
    peer_dhchap_auth_secret: str | None = Field(alias="PeerDHCHAPAuthSecret", default=None)


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
    access_capability: AccessCapability | None = None
    logical_unit_number: str | None = None
    volume: IdRef | None = None


class StorageGroup(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#StorageGroup.v1_6_0.StorageGroup")
    access_state: AccessState | None = None
    actions: Actions | None = None
    authentication_method: AuthenticationMethod | None = None
    chap_info: list[ChapInformation] | None = None
    client_endpoint_groups: list[IdRef] | None = None
    client_endpoint_groups_odata_count: int | None = Field(
        alias="ClientEndpointGroups@odata.count", default=None
    )
    dh_chap_info: list[DhchapInformation] | None = Field(alias="DHChapInfo", default=None)
    description: str | None = None
    id: str
    identifier: Identifier | None = None
    links: Links | None = None
    mapped_volumes: list[MappedVolume] | None = None
    members_are_consistent: bool | None = None
    name: str
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
    volumes_are_exposed: bool | None = None


class StorageGroupOnCreate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(
        alias="@odata.type", default="#StorageGroup.v1_6_0.StorageGroup"
    )
    access_state: AccessState | None = None
    actions: Actions | None = None
    authentication_method: AuthenticationMethod | None = None
    chap_info: list[ChapInformation] | None = None
    client_endpoint_groups: list[IdRef] | None = None
    client_endpoint_groups_odata_count: int | None = Field(
        alias="ClientEndpointGroups@odata.count", default=None
    )
    dh_chap_info: list[DhchapInformation] | None = Field(alias="DHChapInfo", default=None)
    description: str | None = None
    id: str | None = None
    identifier: Identifier | None = None
    links: Links | None = None
    mapped_volumes: list[MappedVolume] | None = None
    members_are_consistent: bool | None = None
    name: str | None = None
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
    volumes_are_exposed: bool | None = None

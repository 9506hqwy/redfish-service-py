from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Status


class AccessCapability(StrEnum):
    READ = "Read"
    WRITE = "Write"


class AccessState(StrEnum):
    OPTIMIZED = "Optimized"
    NON_OPTIMIZED = "NonOptimized"
    STANDBY = "Standby"
    UNAVAILABLE = "Unavailable"
    TRANSITIONING = "Transitioning"


class Actions(RedfishModel):
    add_volume_info: AddVolumeInfo | None = Field(
        serialization_alias="#Connection.AddVolumeInfo", default=None
    )
    remove_volume_info: RemoveVolumeInfo | None = Field(
        serialization_alias="#Connection.RemoveVolumeInfo", default=None
    )
    oem: dict[str, Any] | None = None


class AddVolumeInfo(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class AddVolumeInfoRequest(RedfishModel):
    access_capabilities: list[AccessCapability] | None = None
    lun: int | None = Field(serialization_alias="LUN", default=None)
    volume: IdRef


class ChapConnectionKey(RedfishModel):
    chap_password: str | None = Field(serialization_alias="CHAPPassword", default=None)
    chap_username: str | None = Field(serialization_alias="CHAPUsername", default=None)
    initiator_chap_password: str | None = Field(
        serialization_alias="InitiatorCHAPPassword", default=None
    )
    initiator_chap_username: str | None = Field(
        serialization_alias="InitiatorCHAPUsername", default=None
    )
    target_chap_password: str | None = Field(
        serialization_alias="TargetCHAPPassword", default=None
    )


class Connection(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#Connection.v1_4_0.Connection"
    )
    actions: Actions | None = None
    connection_keys: ConnectionKey | None = None
    connection_type: ConnectionType | None = None
    description: str | None = None
    id: str
    links: Links | None = None
    memory_chunk_info: list[MemoryChunkInfo] | None = None
    memory_region_info: list[MemoryRegionInfo] | None = None
    name: str
    oem: dict[str, Any] | None = None
    status: Status | None = None
    volume_info: list[VolumeInfo] | None = None


class ConnectionOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type", default="#Connection.v1_4_0.Connection"
    )
    actions: Actions | None = None
    connection_keys: ConnectionKey | None = None
    connection_type: ConnectionType | None = None
    description: str | None = None
    id: str | None = None
    links: Links | None = None
    memory_chunk_info: list[MemoryChunkInfo] | None = None
    memory_region_info: list[MemoryRegionInfo] | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
    volume_info: list[VolumeInfo] | None = None


class ConnectionOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    connection_keys: ConnectionKey | None = None
    links: Links | None = None
    memory_chunk_info: list[MemoryChunkInfo] | None = None
    memory_region_info: list[MemoryRegionInfo] | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
    volume_info: list[VolumeInfo] | None = None


class ConnectionKey(RedfishModel):
    chap: ChapConnectionKey | None = Field(serialization_alias="CHAP", default=None)
    dhchap: DhchapKey | None = Field(serialization_alias="DHCHAP", default=None)
    gen_z: GenZConnectionKey | None = None


class ConnectionType(StrEnum):
    STORAGE = "Storage"
    MEMORY = "Memory"


class DhchapKey(RedfishModel):
    local_dhchap_auth_secret: str | None = Field(
        serialization_alias="LocalDHCHAPAuthSecret", default=None
    )
    peer_dhchap_auth_secret: str | None = Field(
        serialization_alias="PeerDHCHAPAuthSecret", default=None
    )


class GenZConnectionKey(RedfishModel):
    access_key: str | None = None
    r_key_domain_checking_enabled: bool | None = None
    r_key_read_only_key: str | None = None
    r_key_read_write_key: str | None = None


class Links(RedfishModel):
    initiator_endpoint_groups: list[IdRef] | None = None
    initiator_endpoint_groups_odata_count: int | None = Field(
        serialization_alias="InitiatorEndpointGroups@odata.count", default=None
    )
    initiator_endpoints: list[IdRef] | None = None
    initiator_endpoints_odata_count: int | None = Field(
        serialization_alias="InitiatorEndpoints@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    target_endpoint_groups: list[IdRef] | None = None
    target_endpoint_groups_odata_count: int | None = Field(
        serialization_alias="TargetEndpointGroups@odata.count", default=None
    )
    target_endpoints: list[IdRef] | None = None
    target_endpoints_odata_count: int | None = Field(
        serialization_alias="TargetEndpoints@odata.count", default=None
    )


class MemoryChunkInfo(RedfishModel):
    access_capabilities: list[AccessCapability] | None = None
    access_state: AccessState | None = None
    memory_chunk: IdRef | None = None


class MemoryRegionInfo(RedfishModel):
    access_capabilities: list[AccessCapability] | None = None
    access_state: AccessState | None = None
    memory_region: IdRef | None = None


class RemoveVolumeInfo(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class RemoveVolumeInfoRequest(RedfishModel):
    lun: int | None = Field(serialization_alias="LUN", default=None)
    volume: IdRef


class VolumeInfo(RedfishModel):
    access_capabilities: list[AccessCapability] | None = None
    access_state: AccessState | None = None
    lun: int | None = Field(serialization_alias="LUN", default=None)
    volume: IdRef | None = None

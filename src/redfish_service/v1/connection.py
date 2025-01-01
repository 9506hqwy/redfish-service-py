from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
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
    oem: dict[str, Any] | None = None


class ChapconnectionKey(RedfishModel):
    chappassword: str | None = Field(alias="CHAPPassword", default=None)
    chapusername: str | None = Field(alias="CHAPUsername", default=None)
    initiator_chappassword: str | None = Field(alias="InitiatorCHAPPassword", default=None)
    initiator_chapusername: str | None = Field(alias="InitiatorCHAPUsername", default=None)
    target_chappassword: str | None = Field(alias="TargetCHAPPassword", default=None)


class Connection(RedfishResource):
    actions: Actions | None = None
    connection_keys: ConnectionKey | None = None
    connection_type: ConnectionType | None = None
    description: str | None = None
    links: Links | None = None
    memory_chunk_info: list[MemoryChunkInfo] | None = None
    memory_region_info: list[MemoryRegionInfo] | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
    volume_info: list[VolumeInfo] | None = None


class ConnectionKey(RedfishModel):
    chap: ChapconnectionKey | None = Field(alias="CHAP", default=None)
    dhchap: Dhchapkey | None = Field(alias="DHCHAP", default=None)
    gen_z: GenZconnectionKey | None = None


class ConnectionType(StrEnum):
    STORAGE = "Storage"
    MEMORY = "Memory"


class Dhchapkey(RedfishModel):
    local_dhchapauth_secret: str | None = Field(alias="LocalDHCHAPAuthSecret", default=None)
    peer_dhchapauth_secret: str | None = Field(alias="PeerDHCHAPAuthSecret", default=None)


class GenZconnectionKey(RedfishModel):
    access_key: str | None = None
    rkey_domain_checking_enabled: bool | None = Field(
        alias="RKeyDomainCheckingEnabled", default=None
    )
    rkey_read_only_key: str | None = Field(alias="RKeyReadOnlyKey", default=None)
    rkey_read_write_key: str | None = Field(alias="RKeyReadWriteKey", default=None)


class Links(RedfishModel):
    initiator_endpoint_groups: list[IdRef] | None = None
    initiator_endpoint_groups_odata_count: int | None = Field(
        alias="InitiatorEndpointGroups@odata.count", default=None
    )
    initiator_endpoints: list[IdRef] | None = None
    initiator_endpoints_odata_count: int | None = Field(
        alias="InitiatorEndpoints@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    target_endpoint_groups: list[IdRef] | None = None
    target_endpoint_groups_odata_count: int | None = Field(
        alias="TargetEndpointGroups@odata.count", default=None
    )
    target_endpoints: list[IdRef] | None = None
    target_endpoints_odata_count: int | None = Field(
        alias="TargetEndpoints@odata.count", default=None
    )


class MemoryChunkInfo(RedfishModel):
    access_capabilities: list[AccessCapability] | None = None
    access_state: AccessState | None = None
    memory_chunk: IdRef | None = None


class MemoryRegionInfo(RedfishModel):
    access_capabilities: list[AccessCapability] | None = None
    access_state: AccessState | None = None
    memory_region: IdRef | None = None


class VolumeInfo(RedfishModel):
    access_capabilities: list[AccessCapability] | None = None
    access_state: AccessState | None = None
    lun: int | None = Field(alias="LUN", default=None)
    volume: IdRef | None = None

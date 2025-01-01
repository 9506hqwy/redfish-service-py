from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..odata_v4 import IdRef
from ..resource import Identifier
from ..swordfish.capacity import Capacity
from ..swordfish.data_storage_lo_scapabilities import StorageAccessCapability
from ..swordfish.iostatistics import Iostatistics
from ..swordfish.storage_replica_info import ReplicaInfo


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class CharacterCodeSet(StrEnum):
    ASCII = "ASCII"
    UNICODE = "Unicode"
    ISO2022 = "ISO2022"
    ISO8859_1 = "ISO8859_1"
    EXTENDED_UNIXCODE = "ExtendedUNIXCode"
    UTF_8 = "UTF_8"
    UTF_16 = "UTF_16"
    UCS_2 = "UCS_2"


class FileProtocol(StrEnum):
    NFSV3 = "NFSv3"
    NFSV4_0 = "NFSv4_0"
    NFSV4_1 = "NFSv4_1"
    SMBV2_0 = "SMBv2_0"
    SMBV2_1 = "SMBv2_1"
    SMBV3_0 = "SMBv3_0"
    SMBV3_0_2 = "SMBv3_0_2"
    SMBV3_1_1 = "SMBv3_1_1"


class FileSystem(RedfishResource):
    access_capabilities: list[StorageAccessCapability] | None = None
    actions: Actions | None = None
    block_size_bytes: int | None = None
    capacity: Capacity | None = None
    capacity_sources: list[IdRef] | None = None
    capacity_sources_odata_count: int | None = Field(
        alias="CapacitySources@odata.count", default=None
    )
    case_preserved: bool | None = None
    case_sensitive: bool | None = None
    character_code_set: list[CharacterCodeSet] | None = None
    cluster_size_bytes: int | None = None
    description: str | None = None
    exported_shares: IdRef | None = None
    iostatistics: Iostatistics | None = Field(alias="IOStatistics", default=None)
    identifiers: list[Identifier] | None = None
    imported_shares: list[dict[str, Any]] | None = None
    links: Links | None = None
    low_space_warning_threshold_percents: list[int] | None = None
    max_file_name_length_bytes: int | None = None
    metrics: IdRef | None = None
    oem: dict[str, Any] | None = None
    recoverable_capacity_source_count: int | None = None
    remaining_capacity: Capacity | None = None
    remaining_capacity_percent: int | None = None
    replica_info: ReplicaInfo | None = None
    replica_targets: list[IdRef] | None = None
    replica_targets_odata_count: int | None = Field(
        alias="ReplicaTargets@odata.count", default=None
    )
    replication_enabled: bool | None = None


class Links(RedfishModel):
    class_of_service: IdRef | None = None
    oem: dict[str, Any] | None = None
    replica_collection: list[IdRef] | None = None
    replica_collection_odata_count: int | None = Field(
        alias="ReplicaCollection@odata.count", default=None
    )
    spare_resource_sets: list[IdRef] | None = None
    spare_resource_sets_odata_count: int | None = Field(
        alias="SpareResourceSets@odata.count", default=None
    )

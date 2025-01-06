from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .. import RedfishModel
from ..odata_v4 import IdRef
from ..resource import Identifier
from ..swordfish.capacity import Capacity
from ..swordfish.data_storage_los_capabilities import StorageAccessCapability
from ..swordfish.io_statistics import IoStatistics
from ..swordfish.storage_replica_info import ReplicaInfo


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class CharacterCodeSet(StrEnum):
    ASCII = "ASCII"
    UNICODE = "Unicode"
    ISO2022 = "ISO2022"
    IS_O8859_1 = "ISO8859_1"
    EXTENDED_UNIX_CODE = "ExtendedUNIXCode"
    UT_F_8 = "UTF_8"
    UT_F_16 = "UTF_16"
    UC_S_2 = "UCS_2"


class FileProtocol(StrEnum):
    NF_SV3 = "NFSv3"
    NF_SV4_0 = "NFSv4_0"
    NF_SV4_1 = "NFSv4_1"
    SM_BV2_0 = "SMBv2_0"
    SM_BV2_1 = "SMBv2_1"
    SM_BV3_0 = "SMBv3_0"
    SM_BV3_0_2 = "SMBv3_0_2"
    SM_BV3_1_1 = "SMBv3_1_1"


class FileSystem(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#FileSystem.v1_4_1.FileSystem")
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
    io_statistics: IoStatistics | None = Field(alias="IOStatistics", default=None)
    id: str
    identifiers: list[Identifier] | None = None
    imported_shares: list[dict[str, Any]] | None = None
    links: Links | None = None
    low_space_warning_threshold_percents: list[int] | None = None
    max_file_name_length_bytes: int | None = None
    metrics: IdRef | None = None
    name: str
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


class FileSystemOnCreate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(alias="@odata.type", default="#FileSystem.v1_4_1.FileSystem")
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
    io_statistics: IoStatistics | None = Field(alias="IOStatistics", default=None)
    id: str | None = None
    identifiers: list[Identifier] | None = None
    imported_shares: list[dict[str, Any]] | None = None
    links: Links | None = None
    low_space_warning_threshold_percents: list[int] | None = None
    max_file_name_length_bytes: int | None = None
    metrics: IdRef | None = None
    name: str | None = None
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

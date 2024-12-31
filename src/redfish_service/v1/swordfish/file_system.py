from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..odata_v4 import IdRef
from ..resource import Identifier
from ..swordfish.capacity import Capacity
from ..swordfish.iostatistics import Iostatistics
from ..swordfish.storage_replica_info import ReplicaInfo


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


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
    access_capabilities: list[str] | None = None
    actions: Actions | None = None
    block_size_bytes: str | None = None
    capacity: Capacity | None = None
    capacity_sources: list[IdRef] | None = None
    case_preserved: str | None = None
    case_sensitive: str | None = None
    character_code_set: list[str] | None = None
    cluster_size_bytes: str | None = None
    description: str | None = None
    exported_shares: IdRef | None = None
    iostatistics: Iostatistics | None = None
    identifiers: list[Identifier] | None = None
    imported_shares: list[dict[str, Any]] | None = None
    links: Links | None = None
    low_space_warning_threshold_percents: list[str] | None = None
    max_file_name_length_bytes: str | None = None
    metrics: str | None = None
    oem: dict[str, Any] | None = None
    recoverable_capacity_source_count: str | None = None
    remaining_capacity: Capacity | None = None
    remaining_capacity_percent: str | None = None
    replica_info: ReplicaInfo | None = None
    replica_targets: list[IdRef] | None = None
    replication_enabled: str | None = None


class Links(RedfishModel):
    class_of_service: IdRef | None = None
    oem: dict[str, Any] | None = None
    replica_collection: list[IdRef] | None = None
    spare_resource_sets: list[IdRef] | None = None

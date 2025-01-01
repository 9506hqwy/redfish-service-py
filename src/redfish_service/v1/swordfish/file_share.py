from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..odata_v4 import IdRef
from ..resource import Status
from ..swordfish.data_storage_lo_scapabilities import StorageAccessCapability
from ..swordfish.file_system import FileProtocol
from ..swordfish.storage_replica_info import ReplicaUpdateMode


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class FileShare(RedfishResource):
    actions: Actions | None = None
    casupported: bool | None = Field(alias="CASupported", default=None)
    default_access_capabilities: list[StorageAccessCapability] | None = None
    description: str | None = None
    ethernet_interfaces: IdRef | None = None
    execute_support: bool | None = None
    file_share_path: str | None = None
    file_share_quota_type: QuotaType | None = None
    file_share_remaining_quota_bytes: int | None = None
    file_share_total_quota_bytes: int | None = None
    file_sharing_protocols: list[FileProtocol] | None = None
    links: Links | None = None
    low_space_warning_threshold_percents: list[int] | None = None
    oem: dict[str, Any] | None = None
    remaining_capacity_percent: int | None = None
    replication_enabled: bool | None = None
    root_access: bool | None = None
    status: Status | None = None
    write_policy: ReplicaUpdateMode | None = None


class Links(RedfishModel):
    class_of_service: IdRef | None = None
    file_system: IdRef | None = None
    oem: dict[str, Any] | None = None


class QuotaType(StrEnum):
    SOFT = "Soft"
    HARD = "Hard"

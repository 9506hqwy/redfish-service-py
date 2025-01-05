from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .. import RedfishModel
from ..odata_v4 import IdRef
from ..resource import Status
from ..swordfish.data_storage_los_capabilities import StorageAccessCapability
from ..swordfish.file_system import FileProtocol
from ..swordfish.storage_replica_info import ReplicaUpdateMode


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class FileShare(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#FileShare.v1_3_0.FileShare")
    actions: Actions | None = None
    ca_supported: bool | None = Field(alias="CASupported", default=None)
    default_access_capabilities: list[StorageAccessCapability] | None = None
    description: str | None = None
    ethernet_interfaces: IdRef | None = None
    execute_support: bool | None = None
    file_share_path: str | None = None
    file_share_quota_type: QuotaType | None = None
    file_share_remaining_quota_bytes: int | None = None
    file_share_total_quota_bytes: int | None = None
    file_sharing_protocols: list[FileProtocol] | None = None
    id: str
    links: Links | None = None
    low_space_warning_threshold_percents: list[int] | None = None
    name: str
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

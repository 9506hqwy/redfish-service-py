from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .. import RedfishModel, RedfishModelOnUpdate
from ..odata_v4 import IdRef
from ..resource import Identifier
from ..swordfish.data_protection_los_capabilities import RecoveryAccessScope


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class DataStorageLosCapabilities(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(
        alias="@odata.type",
        default="#DataStorageLoSCapabilities.v1_2_2.DataStorageLoSCapabilities",
    )
    actions: Actions | None = None
    description: str | None = None
    id: str
    identifier: Identifier | None = None
    maximum_recoverable_capacity_source_count: int | None = None
    name: str
    oem: dict[str, Any] | None = None
    supported_access_capabilities: list[StorageAccessCapability] | None = None
    supported_lines_of_service: list[IdRef] | None = None
    supported_lines_of_service_odata_count: int | None = Field(
        alias="SupportedLinesOfService@odata.count", default=None
    )
    supported_provisioning_policies: list[ProvisioningPolicy] | None = None
    supported_recovery_time_objectives: list[RecoveryAccessScope] | None = None
    supports_space_efficiency: bool | None = None


class DataStorageLosCapabilitiesOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    identifier: Identifier | None = None
    maximum_recoverable_capacity_source_count: int | None = None
    oem: dict[str, Any] | None = None
    supported_access_capabilities: list[StorageAccessCapability] | None = None
    supported_lines_of_service: list[IdRef] | None = None
    supported_provisioning_policies: list[ProvisioningPolicy] | None = None
    supported_recovery_time_objectives: list[RecoveryAccessScope] | None = None
    supports_space_efficiency: bool | None = None


class ProvisioningPolicy(StrEnum):
    FIXED = "Fixed"
    THIN = "Thin"


class StorageAccessCapability(StrEnum):
    READ = "Read"
    WRITE = "Write"
    WRITE_ONCE = "WriteOnce"
    APPEND = "Append"
    STREAMING = "Streaming"
    EXECUTE = "Execute"

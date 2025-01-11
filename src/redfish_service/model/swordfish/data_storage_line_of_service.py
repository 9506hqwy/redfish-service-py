from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .. import RedfishModel
from ..swordfish.data_protection_los_capabilities import RecoveryAccessScope
from ..swordfish.data_storage_los_capabilities import ProvisioningPolicy, StorageAccessCapability


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class DataStorageLineOfService(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(
        alias="@odata.type", default="#DataStorageLineOfService.v1_3_1.DataStorageLineOfService"
    )
    access_capabilities: list[StorageAccessCapability] | None = None
    actions: Actions | None = None
    description: str | None = None
    id: str
    is_space_efficient: bool | None = None
    name: str
    oem: dict[str, Any] | None = None
    provisioning_policy: ProvisioningPolicy | None = None
    recoverable_capacity_source_count: int | None = None
    recovery_time_objectives: RecoveryAccessScope | None = None


class DataStorageLineOfServiceOnUpdate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(
        alias="@odata.type", default="#DataStorageLineOfService.v1_3_1.DataStorageLineOfService"
    )
    access_capabilities: list[StorageAccessCapability] | None = None
    actions: Actions | None = None
    description: str | None = None
    id: str | None = None
    is_space_efficient: bool | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    provisioning_policy: ProvisioningPolicy | None = None
    recoverable_capacity_source_count: int | None = None
    recovery_time_objectives: RecoveryAccessScope | None = None

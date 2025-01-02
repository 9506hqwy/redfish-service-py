from __future__ import annotations  # PEP563 Forward References

from typing import Any

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..swordfish.data_protection_los_capabilities import RecoveryAccessScope
from ..swordfish.data_storage_los_capabilities import ProvisioningPolicy, StorageAccessCapability


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class DataStorageLineOfService(RedfishResource):
    access_capabilities: list[StorageAccessCapability] | None = None
    actions: Actions | None = None
    description: str | None = None
    is_space_efficient: bool | None = None
    oem: dict[str, Any] | None = None
    provisioning_policy: ProvisioningPolicy | None = None
    recoverable_capacity_source_count: int | None = None
    recovery_time_objectives: RecoveryAccessScope | None = None

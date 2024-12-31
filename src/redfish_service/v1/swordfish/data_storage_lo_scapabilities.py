from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..odata_v4 import IdRef
from ..resource import Identifier


class Actions(RedfishModel):
    oem: OemActions | None = None


class DataStorageLoScapabilities(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    identifier: Identifier | None = None
    maximum_recoverable_capacity_source_count: str | None = None
    oem: dict[str, Any] | None = None
    supported_access_capabilities: list[str] | None = None
    supported_lines_of_service: list[IdRef] | None = None
    supported_provisioning_policies: list[str] | None = None
    supported_recovery_time_objectives: list[str] | None = None
    supports_space_efficiency: str | None = None


class OemActions(RedfishModel):
    pass


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

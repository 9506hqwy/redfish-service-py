from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class AllowableTargetReferenceType(StrEnum):
    SOFTWARE_INVENTORY = "SoftwareInventory"
    DEVICE_RESOURCE = "DeviceResource"
    RESOURCE_COLLECTION = "ResourceCollection"
    AGGREGATE = "Aggregate"
    COMPUTER_SYSTEM = "ComputerSystem"


class UpdateServiceCapabilities(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type",
        default="#UpdateServiceCapabilities.v1_1_0.UpdateServiceCapabilities",
    )
    actions: Actions | None = None
    allowable_staging: list[str] | None = None
    allowable_target_reference_types: list[AllowableTargetReferenceType] | None = None
    allowable_targets: list[str] | None = None
    description: str | None = None
    exclude_targets_parameter_supported: bool | None = None
    force_update_parameter_supported: bool | None = None
    id: str
    local_image_parameter_supported: bool | None = None
    name: str
    oem: dict[str, Any] | None = None
    stage_parameter_supported: bool | None = None
    targets_parameter_supported: bool | None = None

from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .physical_context import PhysicalContext
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class AdditionalVersions(RedfishModel):
    bootloader: str | None = None
    kernel: str | None = None
    microcode: str | None = None
    osdistribution: str | None = Field(alias="OSDistribution", default=None)
    oem: dict[str, Any] | None = None


class MeasurementBlock(RedfishModel):
    measurement: str | None = None
    measurement_index: str | None = None
    measurement_size: str | None = None
    measurement_specification: str | None = None


class SoftwareInventory(RedfishResource):
    actions: Actions | None = None
    additional_versions: AdditionalVersions | None = None
    associated_physical_context: PhysicalContext | None = None
    description: str | None = None
    lowest_supported_version: str | None = None
    manufacturer: str | None = None
    measurement: MeasurementBlock | None = None
    oem: dict[str, Any] | None = None
    related_item: list[IdRef] | None = None
    related_item_odata_count: int | None = Field(alias="RelatedItem@odata.count", default=None)
    release_date: str | None = None
    release_type: str | None = None
    software_id: str | None = None
    status: Status | None = None
    uefi_device_paths: list[str] | None = None
    updateable: str | None = None
    version: str | None = None
    version_scheme: str | None = None
    write_protected: str | None = None

from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class AdditionalVersions(RedfishResource):
    bootloader: str | None = None
    kernel: str | None = None
    microcode: str | None = None
    osdistribution: str | None = None
    oem: dict[str, Any] | None = None


class MeasurementBlock(RedfishResource):
    measurement: str | None = None
    measurement_index: str | None = None
    measurement_size: str | None = None
    measurement_specification: str | None = None


class OemActions(RedfishResource):
    pass


class SoftwareInventory(RedfishResource):
    actions: Actions | None = None
    additional_versions: AdditionalVersions | None = None
    description: str | None = None
    lowest_supported_version: str | None = None
    manufacturer: str | None = None
    measurement: MeasurementBlock | None = None
    oem: dict[str, Any] | None = None
    related_item: list[IdRef] | None = None
    release_date: str | None = None
    software_id: str | None = None
    status: Status | None = None
    uefi_device_paths: list[str] | None = None
    updateable: str | None = None
    version: str | None = None
    version_scheme: str | None = None
    write_protected: str | None = None

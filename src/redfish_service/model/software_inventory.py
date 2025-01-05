from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .physical_context import PhysicalContext
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class AdditionalVersions(RedfishModel):
    bootloader: str | None = None
    kernel: str | None = None
    microcode: str | None = None
    os_distribution: str | None = Field(alias="OSDistribution", default=None)
    oem: dict[str, Any] | None = None


class MeasurementBlock(RedfishModel):
    measurement: str | None = None
    measurement_index: int | None = None
    measurement_size: int | None = None
    measurement_specification: int | None = None


class ReleaseType(StrEnum):
    PRODUCTION = "Production"
    PROTOTYPE = "Prototype"
    OTHER = "Other"


class SoftwareInventory(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(
        alias="@odata.type", default="#SoftwareInventory.v1_10_2.SoftwareInventory"
    )
    actions: Actions | None = None
    additional_versions: AdditionalVersions | None = None
    associated_physical_context: PhysicalContext | None = None
    description: str | None = None
    id: str
    lowest_supported_version: str | None = None
    manufacturer: str | None = None
    measurement: MeasurementBlock | None = None
    name: str
    oem: dict[str, Any] | None = None
    related_item: list[IdRef] | None = None
    related_item_odata_count: int | None = Field(alias="RelatedItem@odata.count", default=None)
    release_date: str | None = None
    release_type: ReleaseType | None = None
    software_id: str | None = None
    status: Status | None = None
    uefi_device_paths: list[str] | None = None
    updateable: bool | None = None
    version: str | None = None
    version_scheme: VersionScheme | None = None
    write_protected: bool | None = None


class VersionScheme(StrEnum):
    SEM_VER = "SemVer"
    DOT_INTEGER_NOTATION = "DotIntegerNotation"
    OEM = "OEM"

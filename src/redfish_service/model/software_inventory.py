from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .physical_context import PhysicalContext
from .resource import Status


class Actions(RedfishModel):
    activate: Activate | None = Field(
        serialization_alias="#SoftwareInventory.Activate", default=None
    )
    oem: dict[str, Any] | None = None


class Activate(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ActivateRequest(RedfishModel):
    targets: list[IdRef] | None = None


class AdditionalVersions(RedfishModel):
    boot_parameters: str | None = None
    bootloader: str | None = None
    factory_configuration: str | None = None
    kernel: str | None = None
    microcode: str | None = None
    os_distribution: str | None = Field(serialization_alias="OSDistribution", default=None)
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    active_targets: list[IdRef] | None = None
    active_targets_odata_count: int | None = Field(
        serialization_alias="ActiveTargets@odata.count", default=None
    )
    staged_targets: list[IdRef] | None = None
    staged_targets_odata_count: int | None = Field(
        serialization_alias="StagedTargets@odata.count", default=None
    )


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
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#SoftwareInventory.v1_12_0.SoftwareInventory"
    )
    actions: Actions | None = None
    active: bool | None = None
    additional_versions: AdditionalVersions | None = None
    associated_physical_context: PhysicalContext | None = None
    description: str | None = None
    id: str
    links: Links | None = None
    lowest_supported_version: str | None = None
    manufacturer: str | None = None
    measurement: MeasurementBlock | None = None
    name: str
    oem: dict[str, Any] | None = None
    related_item: list[IdRef] | None = None
    related_item_odata_count: int | None = Field(
        serialization_alias="RelatedItem@odata.count", default=None
    )
    release_date: str | None = None
    release_type: ReleaseType | None = None
    reset_required_on_update: bool | None = None
    software_id: str | None = None
    staged: bool | None = None
    status: Status | None = None
    uefi_device_paths: list[str] | None = None
    updateable: bool | None = None
    version: str | None = None
    version_scheme: VersionScheme | None = None
    write_protected: bool | None = None


class SoftwareInventoryOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    additional_versions: AdditionalVersions | None = None
    links: Links | None = None
    measurement: MeasurementBlock | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None
    write_protected: bool | None = None


class VersionScheme(StrEnum):
    SEM_VER = "SemVer"
    DOT_INTEGER_NOTATION = "DotIntegerNotation"
    OEM = "OEM"

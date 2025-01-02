from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import RedfishModel
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    tpm_get_event_log: TpmGetEventLog | None = Field(
        alias="#TrustedComponent.TPMGetEventLog", default=None
    )
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    active_software_image: IdRef | None = None
    component_integrity: list[IdRef] | None = None
    component_integrity_odata_count: int | None = Field(
        alias="ComponentIntegrity@odata.count", default=None
    )
    components_protected: list[IdRef] | None = None
    components_protected_odata_count: int | None = Field(
        alias="ComponentsProtected@odata.count", default=None
    )
    integrated_into: IdRef | None = None
    oem: dict[str, Any] | None = None
    owner: IdRef | None = None
    software_images: list[IdRef] | None = None
    software_images_odata_count: int | None = Field(
        alias="SoftwareImages@odata.count", default=None
    )


class Tpm(RedfishModel):
    capabilities_vendor_id: str | None = Field(alias="CapabilitiesVendorID", default=None)
    hardware_interface_vendor_id: str | None = Field(
        alias="HardwareInterfaceVendorID", default=None
    )


class TpmGetEventLog(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class TrustedComponent(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    certificates: IdRef | None = None
    description: str | None = None
    firmware_version: str | None = None
    id: str
    links: Links | None = None
    manufacturer: str | None = None
    model: str | None = None
    name: str
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    sku: str | None = Field(alias="SKU", default=None)
    serial_number: str | None = None
    status: Status | None = None
    tpm: Tpm | None = Field(alias="TPM", default=None)
    trusted_component_type: TrustedComponentType
    uuid: str | None = Field(alias="UUID", default=None)


class TrustedComponentType(StrEnum):
    DISCRETE = "Discrete"
    INTEGRATED = "Integrated"

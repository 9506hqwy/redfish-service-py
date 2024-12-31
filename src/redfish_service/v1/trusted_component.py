from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: OemActions | None = None


class Links(RedfishModel):
    active_software_image: IdRef | None = None
    component_integrity: list[IdRef] | None = None
    components_protected: list[IdRef] | None = None
    integrated_into: IdRef | None = None
    oem: dict[str, Any] | None = None
    owner: str | None = None
    software_images: list[IdRef] | None = None


class OemActions(RedfishModel):
    pass


class Tpm(RedfishModel):
    capabilities_vendor_id: str | None = None
    hardware_interface_vendor_id: str | None = None


class TpmgetEventLog(RedfishModel):
    target: str | None = None
    title: str | None = None


class TrustedComponent(RedfishResource):
    actions: Actions | None = None
    certificates: IdRef | None = None
    description: str | None = None
    firmware_version: str | None = None
    links: Links | None = None
    manufacturer: str | None = None
    model: str | None = None
    oem: dict[str, Any] | None = None
    part_number: str | None = None
    sku: str | None = None
    serial_number: str | None = None
    status: Status | None = None
    tpm: Tpm | None = None
    trusted_component_type: TrustedComponentType
    uuid: str | None = None


class TrustedComponentType(StrEnum):
    DISCRETE = "Discrete"
    INTEGRATED = "Integrated"

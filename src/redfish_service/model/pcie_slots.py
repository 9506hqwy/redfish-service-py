from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .pcie_device import PcieTypes
from .resource import Location, Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class PcieLinks(RedfishModel):
    oem: dict[str, Any] | None = None
    pcie_device: list[IdRef] | None = Field(alias="PCIeDevice", default=None)
    pcie_device_odata_count: int | None = Field(alias="PCIeDevice@odata.count", default=None)
    processors: list[IdRef] | None = None
    processors_odata_count: int | None = Field(alias="Processors@odata.count", default=None)


class PcieSlot(RedfishModel):
    hot_pluggable: bool | None = None
    lanes: int | None = None
    links: PcieLinks | None = None
    location: Location | None = None
    location_indicator_active: bool | None = None
    oem: dict[str, Any] | None = None
    pcie_type: PcieTypes | None = Field(alias="PCIeType", default=None)
    slot_type: SlotTypes | None = None
    status: Status | None = None


class PcieSlots(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#PCIeSlots.v1_6_1.PCIeSlots")
    actions: Actions | None = None
    description: str | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
    slots: list[PcieSlot] | None = None


class SlotTypes(StrEnum):
    FULL_LENGTH = "FullLength"
    HALF_LENGTH = "HalfLength"
    LOW_PROFILE = "LowProfile"
    MINI = "Mini"
    M2 = "M2"
    OEM = "OEM"
    OCP3_SMALL = "OCP3Small"
    OCP3_LARGE = "OCP3Large"
    U2 = "U2"

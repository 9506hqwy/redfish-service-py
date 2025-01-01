from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from ..base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class NvmeDeviceType(StrEnum):
    DRIVE = "Drive"
    JBOF = "JBOF"
    FABRIC_ATTACH_ARRAY = "FabricAttachArray"


class NvmeFirmwareImage(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    firmware_version: str | None = None
    nvme_device_type: NvmeDeviceType | None = Field(alias="NVMeDeviceType", default=None)
    oem: dict[str, Any] | None = None
    vendor: str | None = None

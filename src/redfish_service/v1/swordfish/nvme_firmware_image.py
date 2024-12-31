from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from ..base import RedfishResource


class Actions(RedfishResource):
    oem: OemActions | None = None


class NvmeDeviceType(StrEnum):
    DRIVE = "Drive"
    JBOF = "JBOF"
    FABRIC_ATTACH_ARRAY = "FabricAttachArray"


class NvmeFirmwareImage(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    firmware_version: str | None = None
    nvme_device_type: str | None = None
    oem: dict[str, Any] | None = None
    vendor: str | None = None


class OemActions(RedfishResource):
    pass

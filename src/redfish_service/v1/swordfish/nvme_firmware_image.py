from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .. import RedfishModel


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class NvmeDeviceType(StrEnum):
    DRIVE = "Drive"
    JBOF = "JBOF"
    FABRIC_ATTACH_ARRAY = "FabricAttachArray"


class NvmeFirmwareImage(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    description: str | None = None
    firmware_version: str | None = None
    id: str
    nvme_device_type: NvmeDeviceType | None = Field(alias="NVMeDeviceType", default=None)
    name: str
    oem: dict[str, Any] | None = None
    vendor: str | None = None

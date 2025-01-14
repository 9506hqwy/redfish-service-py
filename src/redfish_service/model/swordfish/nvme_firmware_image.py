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
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#NVMeFirmwareImage.v1_2_0.NVMeFirmwareImage"
    )
    actions: Actions | None = None
    description: str | None = None
    firmware_version: str | None = None
    id: str
    nvme_device_type: NvmeDeviceType | None = Field(
        serialization_alias="NVMeDeviceType", default=None
    )
    name: str
    oem: dict[str, Any] | None = None
    vendor: str | None = None

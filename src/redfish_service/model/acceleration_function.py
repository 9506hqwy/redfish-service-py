from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .resource import Status


class AccelerationFunction(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type",
        default="#AccelerationFunction.v1_0_5.AccelerationFunction",
    )
    acceleration_function_type: AccelerationFunctionType | None = None
    actions: Actions | None = None
    description: str | None = None
    fpga_reconfiguration_slots: list[str] | None = None
    id: str
    links: Links | None = None
    manufacturer: str | None = None
    name: str
    oem: dict[str, Any] | None = None
    power_watts: int | None = None
    status: Status | None = None
    uuid: str | None = Field(serialization_alias="UUID", default=None)
    version: str | None = None


class AccelerationFunctionType(StrEnum):
    ENCRYPTION = "Encryption"
    COMPRESSION = "Compression"
    PACKET_INSPECTION = "PacketInspection"
    PACKET_SWITCH = "PacketSwitch"
    SCHEDULER = "Scheduler"
    AUDIO_PROCESSING = "AudioProcessing"
    VIDEO_PROCESSING = "VideoProcessing"
    OEM = "OEM"


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(
        serialization_alias="Endpoints@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    pcie_functions: list[IdRef] | None = Field(serialization_alias="PCIeFunctions", default=None)
    pcie_functions_odata_count: int | None = Field(
        serialization_alias="PCIeFunctions@odata.count", default=None
    )

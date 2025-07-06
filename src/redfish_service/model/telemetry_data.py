from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class TelemetryData(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#TelemetryData.v1_0_0.TelemetryData"
    )
    actions: Actions | None = None
    additional_data: str | None = None
    additional_data_size_bytes: int | None = None
    additional_data_uri: str | None = Field(serialization_alias="AdditionalDataURI", default=None)
    description: str | None = None
    id: str
    name: str
    oem_telemetry_data_type: str | None = Field(
        serialization_alias="OEMTelemetryDataType", default=None
    )
    oem: dict[str, Any] | None = None
    telemetry_data_type: TelemetryDataTypes | None = None
    timestamp: str | None = None


class TelemetryDataTypes(StrEnum):
    OEM = "OEM"

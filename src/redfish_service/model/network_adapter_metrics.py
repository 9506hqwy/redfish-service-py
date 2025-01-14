from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel


class Actions(RedfishModel):
    reset_metrics: ResetMetrics | None = Field(
        serialization_alias="#NetworkAdapterMetrics.ResetMetrics", default=None
    )
    oem: dict[str, Any] | None = None


class NetworkAdapterMetrics(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type",
        default="#NetworkAdapterMetrics.v1_1_0.NetworkAdapterMetrics",
    )
    actions: Actions | None = None
    cpu_core_percent: float | None = Field(serialization_alias="CPUCorePercent", default=None)
    description: str | None = None
    host_bus_rx_percent: float | None = Field(serialization_alias="HostBusRXPercent", default=None)
    host_bus_tx_percent: float | None = Field(serialization_alias="HostBusTXPercent", default=None)
    id: str
    ncsirx_bytes: int | None = Field(serialization_alias="NCSIRXBytes", default=None)
    ncsirx_frames: int | None = Field(serialization_alias="NCSIRXFrames", default=None)
    ncsitx_bytes: int | None = Field(serialization_alias="NCSITXBytes", default=None)
    ncsitx_frames: int | None = Field(serialization_alias="NCSITXFrames", default=None)
    name: str
    oem: dict[str, Any] | None = None
    rx_bytes: int | None = Field(serialization_alias="RXBytes", default=None)
    rx_multicast_frames: int | None = Field(serialization_alias="RXMulticastFrames", default=None)
    rx_unicast_frames: int | None = Field(serialization_alias="RXUnicastFrames", default=None)
    tx_bytes: int | None = Field(serialization_alias="TXBytes", default=None)
    tx_multicast_frames: int | None = Field(serialization_alias="TXMulticastFrames", default=None)
    tx_unicast_frames: int | None = Field(serialization_alias="TXUnicastFrames", default=None)


class ResetMetrics(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)

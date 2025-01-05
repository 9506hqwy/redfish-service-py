from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel


class Actions(RedfishModel):
    reset_metrics: ResetMetrics | None = Field(
        alias="#NetworkAdapterMetrics.ResetMetrics", default=None
    )
    oem: dict[str, Any] | None = None


class NetworkAdapterMetrics(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(
        alias="@odata.type", default="#NetworkAdapterMetrics.v1_1_0.NetworkAdapterMetrics"
    )
    actions: Actions | None = None
    cpu_core_percent: float | None = Field(alias="CPUCorePercent", default=None)
    description: str | None = None
    host_bus_rx_percent: float | None = Field(alias="HostBusRXPercent", default=None)
    host_bus_tx_percent: float | None = Field(alias="HostBusTXPercent", default=None)
    id: str
    ncsirx_bytes: int | None = Field(alias="NCSIRXBytes", default=None)
    ncsirx_frames: int | None = Field(alias="NCSIRXFrames", default=None)
    ncsitx_bytes: int | None = Field(alias="NCSITXBytes", default=None)
    ncsitx_frames: int | None = Field(alias="NCSITXFrames", default=None)
    name: str
    oem: dict[str, Any] | None = None
    rx_bytes: int | None = Field(alias="RXBytes", default=None)
    rx_multicast_frames: int | None = Field(alias="RXMulticastFrames", default=None)
    rx_unicast_frames: int | None = Field(alias="RXUnicastFrames", default=None)
    tx_bytes: int | None = Field(alias="TXBytes", default=None)
    tx_multicast_frames: int | None = Field(alias="TXMulticastFrames", default=None)
    tx_unicast_frames: int | None = Field(alias="TXUnicastFrames", default=None)


class ResetMetrics(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)

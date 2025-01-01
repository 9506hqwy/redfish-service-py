from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    reset_metrics: ResetMetrics | None = Field(
        alias="#NetworkAdapterMetrics.ResetMetrics", default=None
    )
    oem: dict[str, Any] | None = None


class NetworkAdapterMetrics(RedfishResource):
    actions: Actions | None = None
    cpucore_percent: float | None = Field(alias="CPUCorePercent", default=None)
    description: str | None = None
    host_bus_rxpercent: float | None = Field(alias="HostBusRXPercent", default=None)
    host_bus_txpercent: float | None = Field(alias="HostBusTXPercent", default=None)
    ncsirxbytes: int | None = Field(alias="NCSIRXBytes", default=None)
    ncsirxframes: int | None = Field(alias="NCSIRXFrames", default=None)
    ncsitxbytes: int | None = Field(alias="NCSITXBytes", default=None)
    ncsitxframes: int | None = Field(alias="NCSITXFrames", default=None)
    oem: dict[str, Any] | None = None
    rxbytes: int | None = Field(alias="RXBytes", default=None)
    rxmulticast_frames: int | None = Field(alias="RXMulticastFrames", default=None)
    rxunicast_frames: int | None = Field(alias="RXUnicastFrames", default=None)
    txbytes: int | None = Field(alias="TXBytes", default=None)
    txmulticast_frames: int | None = Field(alias="TXMulticastFrames", default=None)
    txunicast_frames: int | None = Field(alias="TXUnicastFrames", default=None)


class ResetMetrics(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)

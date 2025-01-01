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
    cpucore_percent: str | None = Field(alias="CPUCorePercent", default=None)
    description: str | None = None
    host_bus_rxpercent: str | None = Field(alias="HostBusRXPercent", default=None)
    host_bus_txpercent: str | None = Field(alias="HostBusTXPercent", default=None)
    ncsirxbytes: str | None = Field(alias="NCSIRXBytes", default=None)
    ncsirxframes: str | None = Field(alias="NCSIRXFrames", default=None)
    ncsitxbytes: str | None = Field(alias="NCSITXBytes", default=None)
    ncsitxframes: str | None = Field(alias="NCSITXFrames", default=None)
    oem: dict[str, Any] | None = None
    rxbytes: str | None = Field(alias="RXBytes", default=None)
    rxmulticast_frames: str | None = Field(alias="RXMulticastFrames", default=None)
    rxunicast_frames: str | None = Field(alias="RXUnicastFrames", default=None)
    txbytes: str | None = Field(alias="TXBytes", default=None)
    txmulticast_frames: str | None = Field(alias="TXMulticastFrames", default=None)
    txunicast_frames: str | None = Field(alias="TXUnicastFrames", default=None)


class ResetMetrics(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)

from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    oem: OemActions | None = None


class NetworkAdapterMetrics(RedfishResource):
    actions: Actions | None = None
    cpucore_percent: str | None = None
    description: str | None = None
    host_bus_rxpercent: str | None = None
    host_bus_txpercent: str | None = None
    ncsirxbytes: str | None = None
    ncsirxframes: str | None = None
    ncsitxbytes: str | None = None
    ncsitxframes: str | None = None
    oem: dict[str, Any] | None = None
    rxbytes: str | None = None
    rxmulticast_frames: str | None = None
    rxunicast_frames: str | None = None
    txbytes: str | None = None
    txmulticast_frames: str | None = None
    txunicast_frames: str | None = None


class OemActions(RedfishModel):
    pass


class ResetMetrics(RedfishModel):
    target: str | None = None
    title: str | None = None

from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    reset_metrics: ResetMetrics | None = Field(
        alias="#NetworkDeviceFunctionMetrics.ResetMetrics", default=None
    )
    oem: dict[str, Any] | None = None


class Ethernet(RedfishModel):
    num_offloaded_ipv4_conns: int | None = Field(alias="NumOffloadedIPv4Conns", default=None)
    num_offloaded_ipv6_conns: int | None = Field(alias="NumOffloadedIPv6Conns", default=None)


class FibreChannel(RedfishModel):
    port_login_accepts: int | None = None
    port_login_rejects: int | None = None
    port_login_requests: int | None = None
    rxcongestion_fpins: int | None = Field(alias="RXCongestionFPINs", default=None)
    rxdelivery_fpins: int | None = Field(alias="RXDeliveryFPINs", default=None)
    rxexchanges: int | None = Field(alias="RXExchanges", default=None)
    rxlink_integrity_fpins: int | None = Field(alias="RXLinkIntegrityFPINs", default=None)
    rxpeer_congestion_fpins: int | None = Field(alias="RXPeerCongestionFPINs", default=None)
    rxsequences: int | None = Field(alias="RXSequences", default=None)
    txcongestion_fpins: int | None = Field(alias="TXCongestionFPINs", default=None)
    txdelivery_fpins: int | None = Field(alias="TXDeliveryFPINs", default=None)
    txexchanges: int | None = Field(alias="TXExchanges", default=None)
    txlink_integrity_fpins: int | None = Field(alias="TXLinkIntegrityFPINs", default=None)
    txpeer_congestion_fpins: int | None = Field(alias="TXPeerCongestionFPINs", default=None)
    txsequences: int | None = Field(alias="TXSequences", default=None)


class NetworkDeviceFunctionMetrics(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    ethernet: Ethernet | None = None
    fibre_channel: FibreChannel | None = None
    oem: dict[str, Any] | None = None
    rxavg_queue_depth_percent: float | None = Field(alias="RXAvgQueueDepthPercent", default=None)
    rxbytes: int | None = Field(alias="RXBytes", default=None)
    rxframes: int | None = Field(alias="RXFrames", default=None)
    rxmulticast_frames: int | None = Field(alias="RXMulticastFrames", default=None)
    rxqueues_empty: bool | None = Field(alias="RXQueuesEmpty", default=None)
    rxqueues_full: int | None = Field(alias="RXQueuesFull", default=None)
    rxunicast_frames: int | None = Field(alias="RXUnicastFrames", default=None)
    txavg_queue_depth_percent: float | None = Field(alias="TXAvgQueueDepthPercent", default=None)
    txbytes: int | None = Field(alias="TXBytes", default=None)
    txframes: int | None = Field(alias="TXFrames", default=None)
    txmulticast_frames: int | None = Field(alias="TXMulticastFrames", default=None)
    txqueues_empty: bool | None = Field(alias="TXQueuesEmpty", default=None)
    txqueues_full: int | None = Field(alias="TXQueuesFull", default=None)
    txunicast_frames: int | None = Field(alias="TXUnicastFrames", default=None)


class ResetMetrics(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)

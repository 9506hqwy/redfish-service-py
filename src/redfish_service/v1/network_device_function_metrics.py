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
    num_offloaded_ipv4_conns: str | None = Field(alias="NumOffloadedIPv4Conns", default=None)
    num_offloaded_ipv6_conns: str | None = Field(alias="NumOffloadedIPv6Conns", default=None)


class FibreChannel(RedfishModel):
    port_login_accepts: str | None = None
    port_login_rejects: str | None = None
    port_login_requests: str | None = None
    rxcongestion_fpins: str | None = Field(alias="RXCongestionFPINs", default=None)
    rxdelivery_fpins: str | None = Field(alias="RXDeliveryFPINs", default=None)
    rxexchanges: str | None = Field(alias="RXExchanges", default=None)
    rxlink_integrity_fpins: str | None = Field(alias="RXLinkIntegrityFPINs", default=None)
    rxpeer_congestion_fpins: str | None = Field(alias="RXPeerCongestionFPINs", default=None)
    rxsequences: str | None = Field(alias="RXSequences", default=None)
    txcongestion_fpins: str | None = Field(alias="TXCongestionFPINs", default=None)
    txdelivery_fpins: str | None = Field(alias="TXDeliveryFPINs", default=None)
    txexchanges: str | None = Field(alias="TXExchanges", default=None)
    txlink_integrity_fpins: str | None = Field(alias="TXLinkIntegrityFPINs", default=None)
    txpeer_congestion_fpins: str | None = Field(alias="TXPeerCongestionFPINs", default=None)
    txsequences: str | None = Field(alias="TXSequences", default=None)


class NetworkDeviceFunctionMetrics(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    ethernet: Ethernet | None = None
    fibre_channel: FibreChannel | None = None
    oem: dict[str, Any] | None = None
    rxavg_queue_depth_percent: str | None = Field(alias="RXAvgQueueDepthPercent", default=None)
    rxbytes: str | None = Field(alias="RXBytes", default=None)
    rxframes: str | None = Field(alias="RXFrames", default=None)
    rxmulticast_frames: str | None = Field(alias="RXMulticastFrames", default=None)
    rxqueues_empty: str | None = Field(alias="RXQueuesEmpty", default=None)
    rxqueues_full: str | None = Field(alias="RXQueuesFull", default=None)
    rxunicast_frames: str | None = Field(alias="RXUnicastFrames", default=None)
    txavg_queue_depth_percent: str | None = Field(alias="TXAvgQueueDepthPercent", default=None)
    txbytes: str | None = Field(alias="TXBytes", default=None)
    txframes: str | None = Field(alias="TXFrames", default=None)
    txmulticast_frames: str | None = Field(alias="TXMulticastFrames", default=None)
    txqueues_empty: str | None = Field(alias="TXQueuesEmpty", default=None)
    txqueues_full: str | None = Field(alias="TXQueuesFull", default=None)
    txunicast_frames: str | None = Field(alias="TXUnicastFrames", default=None)


class ResetMetrics(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)

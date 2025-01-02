from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import RedfishModel


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
    rx_congestion_fpi_ns: int | None = Field(alias="RXCongestionFPINs", default=None)
    rx_delivery_fpi_ns: int | None = Field(alias="RXDeliveryFPINs", default=None)
    rx_exchanges: int | None = Field(alias="RXExchanges", default=None)
    rx_link_integrity_fpi_ns: int | None = Field(alias="RXLinkIntegrityFPINs", default=None)
    rx_peer_congestion_fpi_ns: int | None = Field(alias="RXPeerCongestionFPINs", default=None)
    rx_sequences: int | None = Field(alias="RXSequences", default=None)
    tx_congestion_fpi_ns: int | None = Field(alias="TXCongestionFPINs", default=None)
    tx_delivery_fpi_ns: int | None = Field(alias="TXDeliveryFPINs", default=None)
    tx_exchanges: int | None = Field(alias="TXExchanges", default=None)
    tx_link_integrity_fpi_ns: int | None = Field(alias="TXLinkIntegrityFPINs", default=None)
    tx_peer_congestion_fpi_ns: int | None = Field(alias="TXPeerCongestionFPINs", default=None)
    tx_sequences: int | None = Field(alias="TXSequences", default=None)


class NetworkDeviceFunctionMetrics(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    description: str | None = None
    ethernet: Ethernet | None = None
    fibre_channel: FibreChannel | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
    rx_avg_queue_depth_percent: float | None = Field(alias="RXAvgQueueDepthPercent", default=None)
    rx_bytes: int | None = Field(alias="RXBytes", default=None)
    rx_frames: int | None = Field(alias="RXFrames", default=None)
    rx_multicast_frames: int | None = Field(alias="RXMulticastFrames", default=None)
    rx_queues_empty: bool | None = Field(alias="RXQueuesEmpty", default=None)
    rx_queues_full: int | None = Field(alias="RXQueuesFull", default=None)
    rx_unicast_frames: int | None = Field(alias="RXUnicastFrames", default=None)
    tx_avg_queue_depth_percent: float | None = Field(alias="TXAvgQueueDepthPercent", default=None)
    tx_bytes: int | None = Field(alias="TXBytes", default=None)
    tx_frames: int | None = Field(alias="TXFrames", default=None)
    tx_multicast_frames: int | None = Field(alias="TXMulticastFrames", default=None)
    tx_queues_empty: bool | None = Field(alias="TXQueuesEmpty", default=None)
    tx_queues_full: int | None = Field(alias="TXQueuesFull", default=None)
    tx_unicast_frames: int | None = Field(alias="TXUnicastFrames", default=None)


class ResetMetrics(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)

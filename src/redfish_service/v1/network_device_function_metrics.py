from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource


class Actions(RedfishResource):
    oem: OemActions | None = None


class Ethernet(RedfishResource):
    num_offloaded_ipv4_conns: str | None = None
    num_offloaded_ipv6_conns: str | None = None


class FibreChannel(RedfishResource):
    port_login_accepts: str | None = None
    port_login_rejects: str | None = None
    port_login_requests: str | None = None
    rxcongestion_fpins: str | None = None
    rxdelivery_fpins: str | None = None
    rxexchanges: str | None = None
    rxlink_integrity_fpins: str | None = None
    rxpeer_congestion_fpins: str | None = None
    rxsequences: str | None = None
    txcongestion_fpins: str | None = None
    txdelivery_fpins: str | None = None
    txexchanges: str | None = None
    txlink_integrity_fpins: str | None = None
    txpeer_congestion_fpins: str | None = None
    txsequences: str | None = None


class NetworkDeviceFunctionMetrics(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    ethernet: Ethernet | None = None
    fibre_channel: FibreChannel | None = None
    oem: dict[str, Any] | None = None
    rxavg_queue_depth_percent: str | None = None
    rxbytes: str | None = None
    rxframes: str | None = None
    rxmulticast_frames: str | None = None
    rxqueues_empty: str | None = None
    rxqueues_full: str | None = None
    rxunicast_frames: str | None = None
    txavg_queue_depth_percent: str | None = None
    txbytes: str | None = None
    txframes: str | None = None
    txmulticast_frames: str | None = None
    txqueues_empty: str | None = None
    txqueues_full: str | None = None
    txunicast_frames: str | None = None


class OemActions(RedfishResource):
    pass


class ResetMetrics(RedfishResource):
    target: str | None = None
    title: str | None = None

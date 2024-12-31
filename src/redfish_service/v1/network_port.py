from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class NetDevFuncMaxBwalloc(RedfishModel):
    max_bwalloc_percent: str | None = None
    network_device_function: IdRef | None = None


class NetDevFuncMinBwalloc(RedfishModel):
    min_bwalloc_percent: str | None = None
    network_device_function: IdRef | None = None


class NetworkPort(RedfishResource):
    actions: Actions | None = None
    active_link_technology: str | None = None
    associated_network_addresses: list[str] | None = None
    current_link_speed_mbps: str | None = None
    description: str | None = None
    eeeenabled: str | None = None
    fcfabric_name: str | None = None
    fcport_connection_type: str | None = None
    flow_control_configuration: str | None = None
    flow_control_status: str | None = None
    link_status: str | None = None
    max_frame_size: str | None = None
    net_dev_func_max_bwalloc: list[NetDevFuncMaxBwalloc] | None = None
    net_dev_func_min_bwalloc: list[NetDevFuncMinBwalloc] | None = None
    number_discovered_remote_ports: str | None = None
    oem: dict[str, Any] | None = None
    physical_port_number: str | None = None
    port_maximum_mtu: str | None = None
    signal_detected: str | None = None
    status: Status | None = None
    supported_ethernet_capabilities: list[str] | None = None
    supported_link_capabilities: list[SupportedLinkCapabilities] | None = None
    vendor_id: str | None = None
    wake_on_lanenabled: str | None = None


class SupportedLinkCapabilities(RedfishModel):
    auto_speed_negotiation: str | None = None
    capable_link_speed_mbps: list[str] | None = None
    link_network_technology: str | None = None
    link_speed_mbps: str | None = None

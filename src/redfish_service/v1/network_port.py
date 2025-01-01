from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class FlowControl(StrEnum):
    NONE = "None"
    TX = "TX"
    RX = "RX"
    TX__RX = "TX_RX"


class LinkNetworkTechnology(StrEnum):
    ETHERNET = "Ethernet"
    INFINI_BAND = "InfiniBand"
    FIBRE_CHANNEL = "FibreChannel"


class LinkStatus(StrEnum):
    DOWN = "Down"
    UP = "Up"
    STARTING = "Starting"
    TRAINING = "Training"


class NetDevFuncMaxBwalloc(RedfishModel):
    max_bwalloc_percent: int | None = Field(alias="MaxBWAllocPercent", default=None)
    network_device_function: IdRef | None = None


class NetDevFuncMinBwalloc(RedfishModel):
    min_bwalloc_percent: int | None = Field(alias="MinBWAllocPercent", default=None)
    network_device_function: IdRef | None = None


class NetworkPort(RedfishResource):
    actions: Actions | None = None
    active_link_technology: LinkNetworkTechnology | None = None
    associated_network_addresses: list[str] | None = None
    current_link_speed_mbps: int | None = None
    description: str | None = None
    eeeenabled: bool | None = Field(alias="EEEEnabled", default=None)
    fcfabric_name: str | None = Field(alias="FCFabricName", default=None)
    fcport_connection_type: PortConnectionType | None = Field(
        alias="FCPortConnectionType", default=None
    )
    flow_control_configuration: FlowControl | None = None
    flow_control_status: FlowControl | None = None
    link_status: LinkStatus | None = None
    max_frame_size: int | None = None
    net_dev_func_max_bwalloc: list[NetDevFuncMaxBwalloc] | None = Field(
        alias="NetDevFuncMaxBWAlloc", default=None
    )
    net_dev_func_min_bwalloc: list[NetDevFuncMinBwalloc] | None = Field(
        alias="NetDevFuncMinBWAlloc", default=None
    )
    number_discovered_remote_ports: int | None = None
    oem: dict[str, Any] | None = None
    physical_port_number: str | None = None
    port_maximum_mtu: int | None = Field(alias="PortMaximumMTU", default=None)
    signal_detected: bool | None = None
    status: Status | None = None
    supported_ethernet_capabilities: list[SupportedEthernetCapabilities] | None = None
    supported_link_capabilities: list[SupportedLinkCapabilities] | None = None
    vendor_id: str | None = None
    wake_on_lanenabled: bool | None = Field(alias="WakeOnLANEnabled", default=None)


class PortConnectionType(StrEnum):
    NOT_CONNECTED = "NotConnected"
    NPORT = "NPort"
    POINT_TO_POINT = "PointToPoint"
    PRIVATE_LOOP = "PrivateLoop"
    PUBLIC_LOOP = "PublicLoop"
    GENERIC = "Generic"
    EXTENDER_FABRIC = "ExtenderFabric"


class SupportedEthernetCapabilities(StrEnum):
    WAKE_ON_LAN = "WakeOnLAN"
    EEE = "EEE"


class SupportedLinkCapabilities(RedfishModel):
    auto_speed_negotiation: bool | None = None
    capable_link_speed_mbps: list[int] | None = None
    link_network_technology: LinkNetworkTechnology | None = None
    link_speed_mbps: int | None = None

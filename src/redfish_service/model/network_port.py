from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class FlowControl(StrEnum):
    NONE = "None"
    TX = "TX"
    RX = "RX"
    T_X_RX = "TX_RX"


class LinkNetworkTechnology(StrEnum):
    ETHERNET = "Ethernet"
    INFINI_BAND = "InfiniBand"
    FIBRE_CHANNEL = "FibreChannel"


class LinkStatus(StrEnum):
    DOWN = "Down"
    UP = "Up"
    STARTING = "Starting"
    TRAINING = "Training"


class NetDevFuncMaxBwAlloc(RedfishModel):
    max_bw_alloc_percent: int | None = Field(alias="MaxBWAllocPercent", default=None)
    network_device_function: IdRef | None = None


class NetDevFuncMinBwAlloc(RedfishModel):
    min_bw_alloc_percent: int | None = Field(alias="MinBWAllocPercent", default=None)
    network_device_function: IdRef | None = None


class NetworkPort(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#NetworkPort.v1_4_3.NetworkPort")
    actions: Actions | None = None
    active_link_technology: LinkNetworkTechnology | None = None
    associated_network_addresses: list[str] | None = None
    current_link_speed_mbps: int | None = None
    description: str | None = None
    eee_enabled: bool | None = Field(alias="EEEEnabled", default=None)
    fc_fabric_name: str | None = Field(alias="FCFabricName", default=None)
    fc_port_connection_type: PortConnectionType | None = Field(
        alias="FCPortConnectionType", default=None
    )
    flow_control_configuration: FlowControl | None = None
    flow_control_status: FlowControl | None = None
    id: str
    link_status: LinkStatus | None = None
    max_frame_size: int | None = None
    name: str
    net_dev_func_max_bw_alloc: list[NetDevFuncMaxBwAlloc] | None = Field(
        alias="NetDevFuncMaxBWAlloc", default=None
    )
    net_dev_func_min_bw_alloc: list[NetDevFuncMinBwAlloc] | None = Field(
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
    wake_on_lan_enabled: bool | None = Field(alias="WakeOnLANEnabled", default=None)


class NetworkPortOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    active_link_technology: LinkNetworkTechnology | None = None
    current_link_speed_mbps: int | None = None
    eee_enabled: bool | None = Field(alias="EEEEnabled", default=None)
    flow_control_configuration: FlowControl | None = None
    net_dev_func_max_bw_alloc: list[NetDevFuncMaxBwAlloc] | None = Field(
        alias="NetDevFuncMaxBWAlloc", default=None
    )
    net_dev_func_min_bw_alloc: list[NetDevFuncMinBwAlloc] | None = Field(
        alias="NetDevFuncMinBWAlloc", default=None
    )
    oem: dict[str, Any] | None = None
    status: Status | None = None
    supported_link_capabilities: list[SupportedLinkCapabilities] | None = None
    wake_on_lan_enabled: bool | None = Field(alias="WakeOnLANEnabled", default=None)


class PortConnectionType(StrEnum):
    NOT_CONNECTED = "NotConnected"
    N_PORT = "NPort"
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

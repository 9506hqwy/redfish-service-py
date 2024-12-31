from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Location, Status


class Actions(RedfishModel):
    oem: OemActions | None = None


class FunctionMaxBandwidth(RedfishModel):
    allocation_percent: str | None = None
    network_device_function: IdRef | None = None


class FunctionMinBandwidth(RedfishModel):
    allocation_percent: str | None = None
    network_device_function: IdRef | None = None


class GenZ(RedfishModel):
    lprt: IdRef | None = None
    mprt: IdRef | None = None
    vcat: IdRef | None = None


class LinkConfiguration(RedfishModel):
    auto_speed_negotiation_capable: str | None = None
    auto_speed_negotiation_enabled: str | None = None
    capable_link_speed_gbps: list[str] | None = None
    configured_network_links: list[str] | None = None


class LinkState(StrEnum):
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class LinkStatus(StrEnum):
    LINK_UP = "LinkUp"
    STARTING = "Starting"
    TRAINING = "Training"
    LINK_DOWN = "LinkDown"
    NO_LINK = "NoLink"


class Links(RedfishModel):
    associated_endpoints: list[IdRef] | None = None
    cables: list[IdRef] | None = None
    connected_ports: list[IdRef] | None = None
    connected_switch_ports: list[IdRef] | None = None
    connected_switches: list[IdRef] | None = None
    ethernet_interfaces: list[IdRef] | None = None
    oem: dict[str, Any] | None = None


class OemActions(RedfishModel):
    pass


class Port(RedfishResource):
    actions: Actions | None = None
    active_width: int | None = None
    cxl: str | None = None
    capable_protocol_versions: list[str] | None = None
    current_protocol_version: str | None = None
    current_speed_gbps: str | None = None
    description: str | None = None
    enabled: bool | None = None
    environment_metrics: IdRef | None = None
    ethernet: str | None = None
    fibre_channel: str | None = None
    function_max_bandwidth: list[FunctionMaxBandwidth] | None = None
    function_min_bandwidth: list[FunctionMinBandwidth] | None = None
    gen_z: GenZ | None = None
    infini_band: str | None = None
    interface_enabled: str | None = None
    link_configuration: list[LinkConfiguration] | None = None
    link_network_technology: str | None = None
    link_state: LinkState | None = None
    link_status: LinkStatus | None = None
    link_transition_indicator: int | None = None
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: str | None = None
    max_frame_size: str | None = None
    max_speed_gbps: str | None = None
    metrics: str | None = None
    oem: dict[str, Any] | None = None
    port_id: str | None = None
    port_medium: str | None = None
    port_protocol: str | None = None
    port_type: str | None = None
    remote_port_id: str | None = None
    sfp: str | None = None
    signal_detected: str | None = None
    status: Status | None = None
    width: str | None = None


class Reset(RedfishModel):
    target: str | None = None
    title: str | None = None


class ResetPpb(RedfishModel):
    target: str | None = None
    title: str | None = None

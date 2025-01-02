from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import RedfishModel
from .odata_v4 import IdRef
from .protocol import Protocol
from .resource import Location, Status


class Actions(RedfishModel):
    reset: Reset | None = Field(alias="#Port.Reset", default=None)
    reset_ppb: ResetPpb | None = Field(alias="#Port.ResetPPB", default=None)
    oem: dict[str, Any] | None = None


class Cxl(RedfishModel):
    congestion: Congestion | None = None
    connected_device_mode: ConnectedDeviceMode | None = None
    connected_device_type: ConnectedDeviceType | None = None
    current_port_configuration_state: CurrentPortConfigurationState | None = None
    max_logical_device_count: int | None = None
    qos_telemetry_capabilities: QosTelemetryCapabilities | None = Field(
        alias="QoSTelemetryCapabilities", default=None
    )
    supported_cxl_modes: list[ConnectedDeviceMode] | None = Field(
        alias="SupportedCXLModes", default=None
    )
    temporary_throughput_reduction_enabled: bool | None = None


class ConfiguredNetworkLink(RedfishModel):
    configured_link_speed_gbps: float | None = None
    configured_width: int | None = None


class Congestion(RedfishModel):
    backpressure_sample_interval: int | None = None
    completion_collection_interval: int | None = None
    congestion_telemetry_enabled: bool | None = None
    egress_moderate_percentage: int | None = None
    egress_severe_percentage: int | None = None
    max_sustained_request_cmp_bias: int | None = None


class ConnectedDeviceMode(StrEnum):
    DISCONNECTED = "Disconnected"
    RCD = "RCD"
    CXL68B_FLIT_AND_VH = "CXL68BFlitAndVH"
    STANDARD256_B_FLIT = "Standard256BFlit"
    CXL_LATENCY_OPTIMIZED256_B_FLIT = "CXLLatencyOptimized256BFlit"
    PBR = "PBR"


class ConnectedDeviceType(StrEnum):
    NONE = "None"
    PCIE_DEVICE = "PCIeDevice"
    TYPE1 = "Type1"
    TYPE2 = "Type2"
    TYPE3_SLD = "Type3SLD"
    TYPE3_MLD = "Type3MLD"


class CurrentPortConfigurationState(StrEnum):
    DISABLED = "Disabled"
    BIND_IN_PROGRESS = "BindInProgress"
    UNBIND_IN_PROGRESS = "UnbindInProgress"
    DSP = "DSP"
    USP = "USP"
    RESERVED = "Reserved"
    FABRIC_LINK = "FabricLink"


class EthernetProperties(RedfishModel):
    associated_mac_addresses: list[str] | None = Field(
        alias="AssociatedMACAddresses", default=None
    )
    eee_enabled: bool | None = Field(alias="EEEEnabled", default=None)
    flow_control_configuration: FlowControl | None = None
    flow_control_status: FlowControl | None = None
    lldp_enabled: bool | None = Field(alias="LLDPEnabled", default=None)
    lldp_receive: LldpReceive | None = Field(alias="LLDPReceive", default=None)
    lldp_transmit: LldpTransmit | None = Field(alias="LLDPTransmit", default=None)
    supported_ethernet_capabilities: list[SupportedEthernetCapabilities] | None = None
    wake_on_lan_enabled: bool | None = Field(alias="WakeOnLANEnabled", default=None)


class FiberConnectionType(StrEnum):
    SINGLE_MODE = "SingleMode"
    MULTI_MODE = "MultiMode"


class FibreChannelProperties(RedfishModel):
    associated_world_wide_names: list[str] | None = None
    fabric_name: str | None = None
    number_discovered_remote_ports: int | None = None
    port_connection_type: PortConnectionType | None = None


class FlowControl(StrEnum):
    NONE = "None"
    TX = "TX"
    RX = "RX"
    T_X_RX = "TX_RX"


class FunctionMaxBandwidth(RedfishModel):
    allocation_percent: int | None = None
    network_device_function: IdRef | None = None


class FunctionMinBandwidth(RedfishModel):
    allocation_percent: int | None = None
    network_device_function: IdRef | None = None


class GenZ(RedfishModel):
    lprt: IdRef | None = Field(alias="LPRT", default=None)
    mprt: IdRef | None = Field(alias="MPRT", default=None)
    vcat: IdRef | None = Field(alias="VCAT", default=None)


class Ieee802IdSubtype(StrEnum):
    CHASSIS_COMP = "ChassisComp"
    IF_ALIAS = "IfAlias"
    PORT_COMP = "PortComp"
    MAC_ADDR = "MacAddr"
    NETWORK_ADDR = "NetworkAddr"
    IF_NAME = "IfName"
    AGENT_ID = "AgentId"
    LOCAL_ASSIGN = "LocalAssign"
    NOT_TRANSMITTED = "NotTransmitted"


class InfiniBandProperties(RedfishModel):
    associated_node_guids: list[str] | None = Field(alias="AssociatedNodeGUIDs", default=None)
    associated_port_guids: list[str] | None = Field(alias="AssociatedPortGUIDs", default=None)
    associated_system_guids: list[str] | None = Field(alias="AssociatedSystemGUIDs", default=None)


class LldpReceive(RedfishModel):
    chassis_id: str | None = None
    chassis_id_subtype: Ieee802IdSubtype | None = None
    management_address_ipv4: str | None = Field(alias="ManagementAddressIPv4", default=None)
    management_address_ipv6: str | None = Field(alias="ManagementAddressIPv6", default=None)
    management_address_mac: str | None = Field(alias="ManagementAddressMAC", default=None)
    management_vlan_id: int | None = None
    port_id: str | None = None
    port_id_subtype: Ieee802IdSubtype | None = None
    system_capabilities: list[LldpSystemCapabilities] | None = None
    system_description: str | None = None
    system_name: str | None = None


class LldpSystemCapabilities(StrEnum):
    NONE = "None"
    BRIDGE = "Bridge"
    DOCSIS_CABLE_DEVICE = "DOCSISCableDevice"
    OTHER = "Other"
    REPEATER = "Repeater"
    ROUTER = "Router"
    STATION = "Station"
    TELEPHONE = "Telephone"
    WLAN_ACCESS_POINT = "WLANAccessPoint"


class LldpTransmit(RedfishModel):
    chassis_id: str | None = None
    chassis_id_subtype: Ieee802IdSubtype | None = None
    management_address_ipv4: str | None = Field(alias="ManagementAddressIPv4", default=None)
    management_address_ipv6: str | None = Field(alias="ManagementAddressIPv6", default=None)
    management_address_mac: str | None = Field(alias="ManagementAddressMAC", default=None)
    management_vlan_id: int | None = None
    port_id: str | None = None
    port_id_subtype: Ieee802IdSubtype | None = None
    system_capabilities: list[LldpSystemCapabilities] | None = None
    system_description: str | None = None
    system_name: str | None = None


class LinkConfiguration(RedfishModel):
    auto_speed_negotiation_capable: bool | None = None
    auto_speed_negotiation_enabled: bool | None = None
    capable_link_speed_gbps: list[float] | None = None
    configured_network_links: list[ConfiguredNetworkLink] | None = None


class LinkNetworkTechnology(StrEnum):
    ETHERNET = "Ethernet"
    INFINI_BAND = "InfiniBand"
    FIBRE_CHANNEL = "FibreChannel"
    GEN_Z = "GenZ"
    PCIE = "PCIe"


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
    associated_endpoints_odata_count: int | None = Field(
        alias="AssociatedEndpoints@odata.count", default=None
    )
    cables: list[IdRef] | None = None
    cables_odata_count: int | None = Field(alias="Cables@odata.count", default=None)
    connected_ports: list[IdRef] | None = None
    connected_ports_odata_count: int | None = Field(
        alias="ConnectedPorts@odata.count", default=None
    )
    connected_switch_ports: list[IdRef] | None = None
    connected_switch_ports_odata_count: int | None = Field(
        alias="ConnectedSwitchPorts@odata.count", default=None
    )
    connected_switches: list[IdRef] | None = None
    connected_switches_odata_count: int | None = Field(
        alias="ConnectedSwitches@odata.count", default=None
    )
    ethernet_interfaces: list[IdRef] | None = None
    ethernet_interfaces_odata_count: int | None = Field(
        alias="EthernetInterfaces@odata.count", default=None
    )
    oem: dict[str, Any] | None = None


class MediumType(StrEnum):
    COPPER = "Copper"
    FIBER_OPTIC = "FiberOptic"


class Port(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    active_width: int | None = None
    cxl: Cxl | None = Field(alias="CXL", default=None)
    capable_protocol_versions: list[str] | None = None
    current_protocol_version: str | None = None
    current_speed_gbps: float | None = None
    description: str | None = None
    enabled: bool | None = None
    environment_metrics: IdRef | None = None
    ethernet: EthernetProperties | None = None
    fibre_channel: FibreChannelProperties | None = None
    function_max_bandwidth: list[FunctionMaxBandwidth] | None = None
    function_min_bandwidth: list[FunctionMinBandwidth] | None = None
    gen_z: GenZ | None = None
    id: str
    infini_band: InfiniBandProperties | None = None
    interface_enabled: bool | None = None
    link_configuration: list[LinkConfiguration] | None = None
    link_network_technology: LinkNetworkTechnology | None = None
    link_state: LinkState | None = None
    link_status: LinkStatus | None = None
    link_transition_indicator: int | None = None
    links: Links | None = None
    location: Location | None = None
    location_indicator_active: bool | None = None
    max_frame_size: int | None = None
    max_speed_gbps: float | None = None
    metrics: IdRef | None = None
    name: str
    oem: dict[str, Any] | None = None
    port_id: str | None = None
    port_medium: PortMedium | None = None
    port_protocol: Protocol | None = None
    port_type: PortType | None = None
    remote_port_id: str | None = None
    sfp: Sfp | None = Field(alias="SFP", default=None)
    signal_detected: bool | None = None
    status: Status | None = None
    width: int | None = None


class PortConnectionType(StrEnum):
    NOT_CONNECTED = "NotConnected"
    N_PORT = "NPort"
    POINT_TO_POINT = "PointToPoint"
    PRIVATE_LOOP = "PrivateLoop"
    PUBLIC_LOOP = "PublicLoop"
    GENERIC = "Generic"
    EXTENDER_FABRIC = "ExtenderFabric"
    F_PORT = "FPort"
    E_PORT = "EPort"
    TE_PORT = "TEPort"
    NP_PORT = "NPPort"
    G_PORT = "GPort"
    NL_PORT = "NLPort"
    FL_PORT = "FLPort"
    EX_PORT = "EXPort"
    U_PORT = "UPort"
    D_PORT = "DPort"


class PortMedium(StrEnum):
    ELECTRICAL = "Electrical"
    OPTICAL = "Optical"


class PortType(StrEnum):
    UPSTREAM_PORT = "UpstreamPort"
    DOWNSTREAM_PORT = "DownstreamPort"
    INTERSWITCH_PORT = "InterswitchPort"
    MANAGEMENT_PORT = "ManagementPort"
    BIDIRECTIONAL_PORT = "BidirectionalPort"
    UNCONFIGURED_PORT = "UnconfiguredPort"


class QosTelemetryCapabilities(RedfishModel):
    egress_port_backpressure_supported: bool | None = None
    temporary_throughput_reduction_supported: bool | None = None


class Reset(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class ResetPpb(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Sfp(RedfishModel):
    date_code: str | None = None
    fiber_connection_type: FiberConnectionType | None = None
    manufacturer: str | None = None
    medium_type: MediumType | None = None
    part_number: str | None = None
    serial_number: str | None = None
    status: Status | None = None
    supported_sfp_types: list[SfpType] | None = Field(alias="SupportedSFPTypes", default=None)
    type: SfpType | None = None
    vendor_oui: str | None = Field(alias="VendorOUI", default=None)
    version: str | None = None


class SfpType(StrEnum):
    SFP = "SFP"
    SFP_PLUS = "SFPPlus"
    SFP28 = "SFP28"
    CSFP = "cSFP"
    SFPDD = "SFPDD"
    QSFP = "QSFP"
    QSFP_PLUS = "QSFPPlus"
    QSFP14 = "QSFP14"
    QSFP28 = "QSFP28"
    QSFP56 = "QSFP56"
    MINI_SASHD = "MiniSASHD"
    QSFPDD = "QSFPDD"
    OSFP = "OSFP"


class SupportedEthernetCapabilities(StrEnum):
    WAKE_ON_LAN = "WakeOnLAN"
    EEE = "EEE"

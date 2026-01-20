from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .protocol import Protocol
from .resource import Status
from .vlan_network_interface import Vlan


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class AuthenticationMethod(StrEnum):
    NONE = "None"
    CHAP = "CHAP"
    MUTUAL_CHAP = "MutualCHAP"


class BootMode(StrEnum):
    DISABLED = "Disabled"
    PXE = "PXE"
    ISCSI = "iSCSI"
    FIBRE_CHANNEL = "FibreChannel"
    FIBRE_CHANNEL_OVER_ETHERNET = "FibreChannelOverEthernet"
    HTTP = "HTTP"


class BootTargets(RedfishModel):
    boot_priority: int | None = None
    lunid: str | None = Field(serialization_alias="LUNID", default=None)
    wwpn: str | None = Field(serialization_alias="WWPN", default=None)


class DataDirection(StrEnum):
    NONE = "None"
    INGRESS = "Ingress"
    EGRESS = "Egress"


class Ethernet(RedfishModel):
    additional_protocols: list[Protocol] | None = None
    ethernet_interfaces: IdRef | None = None
    mac_address: str | None = Field(serialization_alias="MACAddress", default=None)
    mtu_size: int | None = Field(serialization_alias="MTUSize", default=None)
    mtu_size_maximum: int | None = Field(serialization_alias="MTUSizeMaximum", default=None)
    permanent_mac_address: str | None = Field(
        serialization_alias="PermanentMACAddress", default=None
    )
    vlan: Vlan | None = Field(serialization_alias="VLAN", default=None)
    vlans: IdRef | None = Field(serialization_alias="VLANs", default=None)


class FibreChannel(RedfishModel):
    allow_fip_vlan_discovery: bool | None = Field(
        serialization_alias="AllowFIPVLANDiscovery", default=None
    )
    boot_targets: list[BootTargets] | None = None
    fc_oe_active_vlan_id: int | None = Field(serialization_alias="FCoEActiveVLANId", default=None)
    fc_oe_local_vlan_id: int | None = Field(serialization_alias="FCoELocalVLANId", default=None)
    fibre_channel_id: str | None = None
    permanent_wwnn: str | None = Field(serialization_alias="PermanentWWNN", default=None)
    permanent_wwpn: str | None = Field(serialization_alias="PermanentWWPN", default=None)
    wwnn: str | None = Field(serialization_alias="WWNN", default=None)
    wwn_source: WwnSource | None = Field(serialization_alias="WWNSource", default=None)
    wwpn: str | None = Field(serialization_alias="WWPN", default=None)


class HttpBoot(RedfishModel):
    boot_media_uri: str | None = Field(serialization_alias="BootMediaURI", default=None)


class IpAddressType(StrEnum):
    IPV4 = "IPv4"
    IPV6 = "IPv6"


class InfiniBand(RedfishModel):
    mtu_size: int | None = Field(serialization_alias="MTUSize", default=None)
    node_guid: str | None = Field(serialization_alias="NodeGUID", default=None)
    permanent_node_guid: str | None = Field(serialization_alias="PermanentNodeGUID", default=None)
    permanent_port_guid: str | None = Field(serialization_alias="PermanentPortGUID", default=None)
    permanent_system_guid: str | None = Field(
        serialization_alias="PermanentSystemGUID", default=None
    )
    port_guid: str | None = Field(serialization_alias="PortGUID", default=None)
    supported_mtu_sizes: list[int] | None = Field(
        serialization_alias="SupportedMTUSizes", default=None
    )
    system_guid: str | None = Field(serialization_alias="SystemGUID", default=None)


class Limit(RedfishModel):
    burst_bytes_per_second: int | None = None
    burst_packets_per_second: int | None = None
    direction: DataDirection | None = None
    sustained_bytes_per_second: int | None = None
    sustained_packets_per_second: int | None = None


class Links(RedfishModel):
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(
        serialization_alias="Endpoints@odata.count", default=None
    )
    ethernet_interface: IdRef | None = None
    ethernet_interfaces: list[IdRef] | None = None
    ethernet_interfaces_odata_count: int | None = Field(
        serialization_alias="EthernetInterfaces@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    offload_processors: list[IdRef] | None = None
    offload_processors_odata_count: int | None = Field(
        serialization_alias="OffloadProcessors@odata.count", default=None
    )
    offload_system: IdRef | None = None
    pcie_function: IdRef | None = Field(serialization_alias="PCIeFunction", default=None)
    physical_network_port_assignment: IdRef | None = None
    physical_port_assignment: IdRef | None = None


class NetworkDeviceFunction(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type",
        default="#NetworkDeviceFunction.v1_11_1.NetworkDeviceFunction",
    )
    actions: Actions | None = None
    allow_deny: IdRef | None = None
    assignable_physical_network_ports: list[IdRef] | None = None
    assignable_physical_network_ports_odata_count: int | None = Field(
        serialization_alias="AssignablePhysicalNetworkPorts@odata.count", default=None
    )
    assignable_physical_ports: list[IdRef] | None = None
    assignable_physical_ports_odata_count: int | None = Field(
        serialization_alias="AssignablePhysicalPorts@odata.count", default=None
    )
    boot_mode: BootMode | None = None
    description: str | None = None
    device_enabled: bool | None = None
    ethernet: Ethernet | None = None
    fibre_channel: FibreChannel | None = None
    http_boot: HttpBoot | None = Field(serialization_alias="HTTPBoot", default=None)
    id: str
    infini_band: InfiniBand | None = None
    limits: list[Limit] | None = None
    links: Links | None = None
    max_virtual_functions: int | None = None
    metrics: IdRef | None = None
    name: str
    net_dev_func_capabilities: list[NetworkDeviceTechnology] | None = None
    net_dev_func_type: NetworkDeviceTechnology | None = None
    oem: dict[str, Any] | None = None
    physical_network_port_assignment: IdRef | None = None
    physical_port_assignment: IdRef | None = None
    savi_enabled: bool | None = Field(serialization_alias="SAVIEnabled", default=None)
    status: Status | None = None
    virtual_function_allocation: int | None = None
    virtual_functions_enabled: bool | None = None
    i_scsi_boot: IScsiBoot | None = Field(serialization_alias="iSCSIBoot", default=None)


class NetworkDeviceFunctionOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    boot_mode: BootMode | None = None
    device_enabled: bool | None = None
    ethernet: Ethernet | None = None
    fibre_channel: FibreChannel | None = None
    http_boot: HttpBoot | None = Field(serialization_alias="HTTPBoot", default=None)
    infini_band: InfiniBand | None = None
    limits: list[Limit] | None = None
    links: Links | None = None
    net_dev_func_type: NetworkDeviceTechnology | None = None
    oem: dict[str, Any] | None = None
    savi_enabled: bool | None = Field(serialization_alias="SAVIEnabled", default=None)
    status: Status | None = None
    virtual_function_allocation: int | None = None
    i_scsi_boot: IScsiBoot | None = Field(serialization_alias="iSCSIBoot", default=None)


class NetworkDeviceTechnology(StrEnum):
    DISABLED = "Disabled"
    ETHERNET = "Ethernet"
    FIBRE_CHANNEL = "FibreChannel"
    ISCSI = "iSCSI"
    FIBRE_CHANNEL_OVER_ETHERNET = "FibreChannelOverEthernet"
    INFINI_BAND = "InfiniBand"


class WwnSource(StrEnum):
    CONFIGURED_LOCALLY = "ConfiguredLocally"
    PROVIDED_BY_FABRIC = "ProvidedByFabric"


class IScsiBoot(RedfishModel):
    authentication_method: AuthenticationMethod | None = None
    chap_secret: str | None = Field(serialization_alias="CHAPSecret", default=None)
    chap_username: str | None = Field(serialization_alias="CHAPUsername", default=None)
    ip_address_type: IpAddressType | None = Field(
        serialization_alias="IPAddressType", default=None
    )
    ip_mask_dns_via_dhcp: bool | None = Field(serialization_alias="IPMaskDNSViaDHCP", default=None)
    initiator_default_gateway: str | None = None
    initiator_ip_address: str | None = Field(
        serialization_alias="InitiatorIPAddress", default=None
    )
    initiator_name: str | None = None
    initiator_netmask: str | None = None
    mutual_chap_secret: str | None = Field(serialization_alias="MutualCHAPSecret", default=None)
    mutual_chap_username: str | None = Field(
        serialization_alias="MutualCHAPUsername", default=None
    )
    primary_dns: str | None = Field(serialization_alias="PrimaryDNS", default=None)
    primary_lun: int | None = Field(serialization_alias="PrimaryLUN", default=None)
    primary_target_ip_address: str | None = Field(
        serialization_alias="PrimaryTargetIPAddress", default=None
    )
    primary_target_name: str | None = None
    primary_target_tcp_port: int | None = Field(
        serialization_alias="PrimaryTargetTCPPort", default=None
    )
    primary_vlan_enable: bool | None = Field(serialization_alias="PrimaryVLANEnable", default=None)
    primary_vlan_id: int | None = Field(serialization_alias="PrimaryVLANId", default=None)
    router_advertisement_enabled: bool | None = None
    secondary_dns: str | None = Field(serialization_alias="SecondaryDNS", default=None)
    secondary_lun: int | None = Field(serialization_alias="SecondaryLUN", default=None)
    secondary_target_ip_address: str | None = Field(
        serialization_alias="SecondaryTargetIPAddress", default=None
    )
    secondary_target_name: str | None = None
    secondary_target_tcp_port: int | None = Field(
        serialization_alias="SecondaryTargetTCPPort", default=None
    )
    secondary_vlan_enable: bool | None = Field(
        serialization_alias="SecondaryVLANEnable", default=None
    )
    secondary_vlan_id: int | None = Field(serialization_alias="SecondaryVLANId", default=None)
    target_info_via_dhcp: bool | None = Field(
        serialization_alias="TargetInfoViaDHCP", default=None
    )

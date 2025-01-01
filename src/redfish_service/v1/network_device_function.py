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
    lunid: str | None = Field(alias="LUNID", default=None)
    wwpn: str | None = Field(alias="WWPN", default=None)


class DataDirection(StrEnum):
    NONE = "None"
    INGRESS = "Ingress"
    EGRESS = "Egress"


class Ethernet(RedfishModel):
    ethernet_interfaces: IdRef | None = None
    macaddress: str | None = Field(alias="MACAddress", default=None)
    mtusize: int | None = Field(alias="MTUSize", default=None)
    mtusize_maximum: int | None = Field(alias="MTUSizeMaximum", default=None)
    permanent_macaddress: str | None = Field(alias="PermanentMACAddress", default=None)
    vlan: Vlan | None = Field(alias="VLAN", default=None)
    vlans: IdRef | None = Field(alias="VLANs", default=None)


class FibreChannel(RedfishModel):
    allow_fipvlandiscovery: bool | None = Field(alias="AllowFIPVLANDiscovery", default=None)
    boot_targets: list[BootTargets] | None = None
    fco_eactive_vlanid: int | None = Field(alias="FCoEActiveVLANId", default=None)
    fco_elocal_vlanid: int | None = Field(alias="FCoELocalVLANId", default=None)
    fibre_channel_id: str | None = None
    permanent_wwnn: str | None = Field(alias="PermanentWWNN", default=None)
    permanent_wwpn: str | None = Field(alias="PermanentWWPN", default=None)
    wwnn: str | None = Field(alias="WWNN", default=None)
    wwnsource: Wwnsource | None = Field(alias="WWNSource", default=None)
    wwpn: str | None = Field(alias="WWPN", default=None)


class Httpboot(RedfishModel):
    boot_media_uri: str | None = Field(alias="BootMediaURI", default=None)


class IpaddressType(StrEnum):
    IPV4 = "IPv4"
    IPV6 = "IPv6"


class InfiniBand(RedfishModel):
    mtusize: int | None = Field(alias="MTUSize", default=None)
    node_guid: str | None = Field(alias="NodeGUID", default=None)
    permanent_node_guid: str | None = Field(alias="PermanentNodeGUID", default=None)
    permanent_port_guid: str | None = Field(alias="PermanentPortGUID", default=None)
    permanent_system_guid: str | None = Field(alias="PermanentSystemGUID", default=None)
    port_guid: str | None = Field(alias="PortGUID", default=None)
    supported_mtusizes: list[int] | None = Field(alias="SupportedMTUSizes", default=None)
    system_guid: str | None = Field(alias="SystemGUID", default=None)


class Limit(RedfishModel):
    burst_bytes_per_second: int | None = None
    burst_packets_per_second: int | None = None
    direction: DataDirection | None = None
    sustained_bytes_per_second: int | None = None
    sustained_packets_per_second: int | None = None


class Links(RedfishModel):
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(alias="Endpoints@odata.count", default=None)
    ethernet_interface: IdRef | None = None
    ethernet_interfaces: list[IdRef] | None = None
    ethernet_interfaces_odata_count: int | None = Field(
        alias="EthernetInterfaces@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    offload_processors: list[IdRef] | None = None
    offload_processors_odata_count: int | None = Field(
        alias="OffloadProcessors@odata.count", default=None
    )
    offload_system: IdRef | None = None
    pcie_function: IdRef | None = Field(alias="PCIeFunction", default=None)
    physical_network_port_assignment: IdRef | None = None
    physical_port_assignment: IdRef | None = None


class NetworkDeviceFunction(RedfishResource):
    actions: Actions | None = None
    allow_deny: IdRef | None = None
    assignable_physical_network_ports: list[IdRef] | None = None
    assignable_physical_network_ports_odata_count: int | None = Field(
        alias="AssignablePhysicalNetworkPorts@odata.count", default=None
    )
    assignable_physical_ports: list[IdRef] | None = None
    assignable_physical_ports_odata_count: int | None = Field(
        alias="AssignablePhysicalPorts@odata.count", default=None
    )
    boot_mode: BootMode | None = None
    description: str | None = None
    device_enabled: bool | None = None
    ethernet: Ethernet | None = None
    fibre_channel: FibreChannel | None = None
    httpboot: Httpboot | None = Field(alias="HTTPBoot", default=None)
    infini_band: InfiniBand | None = None
    limits: list[Limit] | None = None
    links: Links | None = None
    max_virtual_functions: int | None = None
    metrics: IdRef | None = None
    net_dev_func_capabilities: list[NetworkDeviceTechnology] | None = None
    net_dev_func_type: NetworkDeviceTechnology | None = None
    oem: dict[str, Any] | None = None
    physical_network_port_assignment: IdRef | None = None
    physical_port_assignment: IdRef | None = None
    savienabled: bool | None = Field(alias="SAVIEnabled", default=None)
    status: Status | None = None
    virtual_functions_enabled: bool | None = None
    i_scsiboot: IScsiboot | None = Field(alias="iSCSIBoot", default=None)


class NetworkDeviceTechnology(StrEnum):
    DISABLED = "Disabled"
    ETHERNET = "Ethernet"
    FIBRE_CHANNEL = "FibreChannel"
    ISCSI = "iSCSI"
    FIBRE_CHANNEL_OVER_ETHERNET = "FibreChannelOverEthernet"
    INFINI_BAND = "InfiniBand"


class Wwnsource(StrEnum):
    CONFIGURED_LOCALLY = "ConfiguredLocally"
    PROVIDED_BY_FABRIC = "ProvidedByFabric"


class IScsiboot(RedfishModel):
    authentication_method: AuthenticationMethod | None = None
    chapsecret: str | None = Field(alias="CHAPSecret", default=None)
    chapusername: str | None = Field(alias="CHAPUsername", default=None)
    ipaddress_type: IpaddressType | None = Field(alias="IPAddressType", default=None)
    ipmask_dnsvia_dhcp: bool | None = Field(alias="IPMaskDNSViaDHCP", default=None)
    initiator_default_gateway: str | None = None
    initiator_ipaddress: str | None = Field(alias="InitiatorIPAddress", default=None)
    initiator_name: str | None = None
    initiator_netmask: str | None = None
    mutual_chapsecret: str | None = Field(alias="MutualCHAPSecret", default=None)
    mutual_chapusername: str | None = Field(alias="MutualCHAPUsername", default=None)
    primary_dns: str | None = Field(alias="PrimaryDNS", default=None)
    primary_lun: int | None = Field(alias="PrimaryLUN", default=None)
    primary_target_ipaddress: str | None = Field(alias="PrimaryTargetIPAddress", default=None)
    primary_target_name: str | None = None
    primary_target_tcpport: int | None = Field(alias="PrimaryTargetTCPPort", default=None)
    primary_vlanenable: bool | None = Field(alias="PrimaryVLANEnable", default=None)
    primary_vlanid: int | None = Field(alias="PrimaryVLANId", default=None)
    router_advertisement_enabled: bool | None = None
    secondary_dns: str | None = Field(alias="SecondaryDNS", default=None)
    secondary_lun: int | None = Field(alias="SecondaryLUN", default=None)
    secondary_target_ipaddress: str | None = Field(alias="SecondaryTargetIPAddress", default=None)
    secondary_target_name: str | None = None
    secondary_target_tcpport: int | None = Field(alias="SecondaryTargetTCPPort", default=None)
    secondary_vlanenable: bool | None = Field(alias="SecondaryVLANEnable", default=None)
    secondary_vlanid: int | None = Field(alias="SecondaryVLANId", default=None)
    target_info_via_dhcp: bool | None = Field(alias="TargetInfoViaDHCP", default=None)

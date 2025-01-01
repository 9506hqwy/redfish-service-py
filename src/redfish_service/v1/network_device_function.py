from __future__ import annotations  # PEP563 Forward References

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


class Ethernet(RedfishModel):
    ethernet_interfaces: str | None = None
    macaddress: str | None = Field(alias="MACAddress", default=None)
    mtusize: str | None = Field(alias="MTUSize", default=None)
    mtusize_maximum: str | None = Field(alias="MTUSizeMaximum", default=None)
    permanent_macaddress: str | None = Field(alias="PermanentMACAddress", default=None)
    vlan: Vlan | None = Field(alias="VLAN", default=None)
    vlans: IdRef | None = Field(alias="VLANs", default=None)


class FibreChannel(RedfishModel):
    allow_fipvlandiscovery: str | None = Field(alias="AllowFIPVLANDiscovery", default=None)
    boot_targets: list[str] | None = None
    fco_eactive_vlanid: str | None = Field(alias="FCoEActiveVLANId", default=None)
    fco_elocal_vlanid: str | None = Field(alias="FCoELocalVLANId", default=None)
    fibre_channel_id: str | None = None
    permanent_wwnn: str | None = Field(alias="PermanentWWNN", default=None)
    permanent_wwpn: str | None = Field(alias="PermanentWWPN", default=None)
    wwnn: str | None = Field(alias="WWNN", default=None)
    wwnsource: str | None = Field(alias="WWNSource", default=None)
    wwpn: str | None = Field(alias="WWPN", default=None)


class Httpboot(RedfishModel):
    boot_media_uri: str | None = Field(alias="BootMediaURI", default=None)


class InfiniBand(RedfishModel):
    mtusize: str | None = Field(alias="MTUSize", default=None)
    node_guid: str | None = Field(alias="NodeGUID", default=None)
    permanent_node_guid: str | None = Field(alias="PermanentNodeGUID", default=None)
    permanent_port_guid: str | None = Field(alias="PermanentPortGUID", default=None)
    permanent_system_guid: str | None = Field(alias="PermanentSystemGUID", default=None)
    port_guid: str | None = Field(alias="PortGUID", default=None)
    supported_mtusizes: list[str] | None = Field(alias="SupportedMTUSizes", default=None)
    system_guid: str | None = Field(alias="SystemGUID", default=None)


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
    boot_mode: str | None = None
    description: str | None = None
    device_enabled: str | None = None
    ethernet: Ethernet | None = None
    fibre_channel: FibreChannel | None = None
    httpboot: Httpboot | None = Field(alias="HTTPBoot", default=None)
    infini_band: InfiniBand | None = None
    limits: list[str] | None = None
    links: Links | None = None
    max_virtual_functions: str | None = None
    metrics: str | None = None
    net_dev_func_capabilities: list[str] | None = None
    net_dev_func_type: str | None = None
    oem: dict[str, Any] | None = None
    physical_network_port_assignment: IdRef | None = None
    physical_port_assignment: IdRef | None = None
    savienabled: str | None = Field(alias="SAVIEnabled", default=None)
    status: Status | None = None
    virtual_functions_enabled: str | None = None
    i_scsiboot: IScsiboot | None = Field(alias="iSCSIBoot", default=None)


class IScsiboot(RedfishModel):
    authentication_method: str | None = None
    chapsecret: str | None = Field(alias="CHAPSecret", default=None)
    chapusername: str | None = Field(alias="CHAPUsername", default=None)
    ipaddress_type: str | None = Field(alias="IPAddressType", default=None)
    ipmask_dnsvia_dhcp: str | None = Field(alias="IPMaskDNSViaDHCP", default=None)
    initiator_default_gateway: str | None = None
    initiator_ipaddress: str | None = Field(alias="InitiatorIPAddress", default=None)
    initiator_name: str | None = None
    initiator_netmask: str | None = None
    mutual_chapsecret: str | None = Field(alias="MutualCHAPSecret", default=None)
    mutual_chapusername: str | None = Field(alias="MutualCHAPUsername", default=None)
    primary_dns: str | None = Field(alias="PrimaryDNS", default=None)
    primary_lun: str | None = Field(alias="PrimaryLUN", default=None)
    primary_target_ipaddress: str | None = Field(alias="PrimaryTargetIPAddress", default=None)
    primary_target_name: str | None = None
    primary_target_tcpport: str | None = Field(alias="PrimaryTargetTCPPort", default=None)
    primary_vlanenable: str | None = Field(alias="PrimaryVLANEnable", default=None)
    primary_vlanid: str | None = Field(alias="PrimaryVLANId", default=None)
    router_advertisement_enabled: str | None = None
    secondary_dns: str | None = Field(alias="SecondaryDNS", default=None)
    secondary_lun: str | None = Field(alias="SecondaryLUN", default=None)
    secondary_target_ipaddress: str | None = Field(alias="SecondaryTargetIPAddress", default=None)
    secondary_target_name: str | None = None
    secondary_target_tcpport: str | None = Field(alias="SecondaryTargetTCPPort", default=None)
    secondary_vlanenable: str | None = Field(alias="SecondaryVLANEnable", default=None)
    secondary_vlanid: str | None = Field(alias="SecondaryVLANId", default=None)
    target_info_via_dhcp: str | None = Field(alias="TargetInfoViaDHCP", default=None)

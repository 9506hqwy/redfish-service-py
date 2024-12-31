from __future__ import annotations  # PEP563 Forward References

from typing import Any

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
    macaddress: str | None = None
    mtusize: str | None = None
    mtusize_maximum: str | None = None
    permanent_macaddress: str | None = None
    vlan: Vlan | None = None
    vlans: IdRef | None = None


class FibreChannel(RedfishModel):
    allow_fipvlandiscovery: str | None = None
    boot_targets: list[str] | None = None
    fco_eactive_vlanid: str | None = None
    fco_elocal_vlanid: str | None = None
    fibre_channel_id: str | None = None
    permanent_wwnn: str | None = None
    permanent_wwpn: str | None = None
    wwnn: str | None = None
    wwnsource: str | None = None
    wwpn: str | None = None


class Httpboot(RedfishModel):
    boot_media_uri: str | None = None


class InfiniBand(RedfishModel):
    mtusize: str | None = None
    node_guid: str | None = None
    permanent_node_guid: str | None = None
    permanent_port_guid: str | None = None
    permanent_system_guid: str | None = None
    port_guid: str | None = None
    supported_mtusizes: list[str] | None = None
    system_guid: str | None = None


class Links(RedfishModel):
    endpoints: list[IdRef] | None = None
    ethernet_interface: IdRef | None = None
    ethernet_interfaces: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    offload_processors: list[IdRef] | None = None
    offload_system: IdRef | None = None
    pcie_function: IdRef | None = None
    physical_network_port_assignment: IdRef | None = None
    physical_port_assignment: IdRef | None = None


class NetworkDeviceFunction(RedfishResource):
    actions: Actions | None = None
    allow_deny: IdRef | None = None
    assignable_physical_network_ports: list[IdRef] | None = None
    assignable_physical_ports: list[IdRef] | None = None
    boot_mode: str | None = None
    description: str | None = None
    device_enabled: str | None = None
    ethernet: Ethernet | None = None
    fibre_channel: FibreChannel | None = None
    httpboot: Httpboot | None = None
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
    savienabled: str | None = None
    status: Status | None = None
    virtual_functions_enabled: str | None = None
    i_scsiboot: IScsiboot | None = None


class IScsiboot(RedfishModel):
    authentication_method: str | None = None
    chapsecret: str | None = None
    chapusername: str | None = None
    ipaddress_type: str | None = None
    ipmask_dnsvia_dhcp: str | None = None
    initiator_default_gateway: str | None = None
    initiator_ipaddress: str | None = None
    initiator_name: str | None = None
    initiator_netmask: str | None = None
    mutual_chapsecret: str | None = None
    mutual_chapusername: str | None = None
    primary_dns: str | None = None
    primary_lun: str | None = None
    primary_target_ipaddress: str | None = None
    primary_target_name: str | None = None
    primary_target_tcpport: str | None = None
    primary_vlanenable: str | None = None
    primary_vlanid: str | None = None
    router_advertisement_enabled: str | None = None
    secondary_dns: str | None = None
    secondary_lun: str | None = None
    secondary_target_ipaddress: str | None = None
    secondary_target_name: str | None = None
    secondary_target_tcpport: str | None = None
    secondary_vlanenable: str | None = None
    secondary_vlanid: str | None = None
    target_info_via_dhcp: str | None = None

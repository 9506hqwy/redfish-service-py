from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .ipaddresses import Ipv4Address, Ipv6Address
from .odata_v4 import IdRef
from .resource import Status
from .vlan_network_interface import Vlan


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Dhcpv4Configuration(RedfishModel):
    dhcpenabled: str | None = None
    fallback_address: str | None = None
    use_dnsservers: str | None = None
    use_domain_name: str | None = None
    use_gateway: str | None = None
    use_ntpservers: str | None = None
    use_static_routes: str | None = None


class Dhcpv6Configuration(RedfishModel):
    operating_mode: str | None = None
    use_dnsservers: str | None = None
    use_domain_name: str | None = None
    use_ntpservers: str | None = None
    use_rapid_commit: str | None = None


class EthernetInterface(RedfishResource):
    actions: Actions | None = None
    auto_neg: str | None = None
    dhcpv4: Dhcpv4Configuration | None = None
    dhcpv6: Dhcpv6Configuration | None = None
    description: str | None = None
    ethernet_interface_type: str | None = None
    fqdn: str | None = None
    full_duplex: str | None = None
    host_name: str | None = None
    ipv4_addresses: list[Ipv4Address] | None = None
    ipv4_static_addresses: list[str] | None = None
    ipv6_address_policy_table: list[str] | None = None
    ipv6_addresses: list[Ipv6Address] | None = None
    ipv6_default_gateway: str | None = None
    ipv6_static_addresses: list[str] | None = None
    ipv6_static_default_gateways: list[str] | None = None
    interface_enabled: str | None = None
    link_status: str | None = None
    links: Links | None = None
    macaddress: str | None = None
    mtusize: str | None = None
    max_ipv6_static_addresses: str | None = None
    name_servers: list[str] | None = None
    oem: dict[str, Any] | None = None
    permanent_macaddress: str | None = None
    speed_mbps: str | None = None
    stateless_address_auto_config: StatelessAddressAutoConfiguration | None = None
    static_name_servers: list[str] | None = None
    status: Status | None = None
    team_mode: str | None = None
    uefi_device_path: str | None = None
    vlan: Vlan | None = None
    vlans: IdRef | None = None


class Links(RedfishModel):
    chassis: IdRef | None = None
    endpoints: list[IdRef] | None = None
    host_interface: IdRef | None = None
    network_device_function: str | None = None
    network_device_functions: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    ports: list[IdRef] | None = None
    related_interfaces: list[IdRef] | None = None


class StatelessAddressAutoConfiguration(RedfishModel):
    ipv4_auto_config_enabled: str | None = None
    ipv6_auto_config_enabled: str | None = None

from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import RedfishModel
from .ip_addresses import Ipv4Address, Ipv6Address, Ipv6GatewayStaticAddress, Ipv6StaticAddress
from .odata_v4 import IdRef
from .resource import Status
from .vlan_network_interface import Vlan


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class DhcpFallback(StrEnum):
    STATIC = "Static"
    AUTO_CONFIG = "AutoConfig"
    NONE = "None"


class Dhcpv4Configuration(RedfishModel):
    dhcp_enabled: bool | None = Field(alias="DHCPEnabled", default=None)
    fallback_address: DhcpFallback | None = None
    use_dns_servers: bool | None = Field(alias="UseDNSServers", default=None)
    use_domain_name: bool | None = None
    use_gateway: bool | None = None
    use_ntp_servers: bool | None = Field(alias="UseNTPServers", default=None)
    use_static_routes: bool | None = None


class Dhcpv6Configuration(RedfishModel):
    operating_mode: Dhcpv6OperatingMode | None = None
    use_dns_servers: bool | None = Field(alias="UseDNSServers", default=None)
    use_domain_name: bool | None = None
    use_ntp_servers: bool | None = Field(alias="UseNTPServers", default=None)
    use_rapid_commit: bool | None = None


class Dhcpv6OperatingMode(StrEnum):
    STATEFUL = "Stateful"
    STATELESS = "Stateless"
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class EthernetDeviceType(StrEnum):
    PHYSICAL = "Physical"
    VIRTUAL = "Virtual"


class EthernetInterface(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    auto_neg: bool | None = None
    dhcpv4: Dhcpv4Configuration | None = Field(alias="DHCPv4", default=None)
    dhcpv6: Dhcpv6Configuration | None = Field(alias="DHCPv6", default=None)
    description: str | None = None
    ethernet_interface_type: EthernetDeviceType | None = None
    fqdn: str | None = Field(alias="FQDN", default=None)
    full_duplex: bool | None = None
    host_name: str | None = None
    ipv4_addresses: list[Ipv4Address] | None = Field(alias="IPv4Addresses", default=None)
    ipv4_static_addresses: list[Ipv4Address] | None = Field(
        alias="IPv4StaticAddresses", default=None
    )
    ipv6_address_policy_table: list[Ipv6AddressPolicyEntry] | None = Field(
        alias="IPv6AddressPolicyTable", default=None
    )
    ipv6_addresses: list[Ipv6Address] | None = Field(alias="IPv6Addresses", default=None)
    ipv6_default_gateway: str | None = Field(alias="IPv6DefaultGateway", default=None)
    ipv6_enabled: bool | None = Field(alias="IPv6Enabled", default=None)
    ipv6_static_addresses: list[Ipv6StaticAddress] | None = Field(
        alias="IPv6StaticAddresses", default=None
    )
    ipv6_static_default_gateways: list[Ipv6GatewayStaticAddress] | None = Field(
        alias="IPv6StaticDefaultGateways", default=None
    )
    id: str
    interface_enabled: bool | None = None
    link_status: LinkStatus | None = None
    links: Links | None = None
    mac_address: str | None = Field(alias="MACAddress", default=None)
    mtu_size: int | None = Field(alias="MTUSize", default=None)
    max_ipv6_static_addresses: int | None = Field(alias="MaxIPv6StaticAddresses", default=None)
    name: str
    name_servers: list[str] | None = None
    oem: dict[str, Any] | None = None
    permanent_mac_address: str | None = Field(alias="PermanentMACAddress", default=None)
    routing_scope: RoutingScope | None = None
    speed_mbps: int | None = None
    stateless_address_auto_config: StatelessAddressAutoConfiguration | None = None
    static_name_servers: list[str] | None = None
    status: Status | None = None
    team_mode: TeamMode | None = None
    uefi_device_path: str | None = None
    vlan: Vlan | None = Field(alias="VLAN", default=None)
    vlans: IdRef | None = Field(alias="VLANs", default=None)


class Ipv6AddressPolicyEntry(RedfishModel):
    label: int | None = None
    precedence: int | None = None
    prefix: str | None = None


class LinkStatus(StrEnum):
    LINK_UP = "LinkUp"
    NO_LINK = "NoLink"
    LINK_DOWN = "LinkDown"


class Links(RedfishModel):
    affiliated_interfaces: list[IdRef] | None = None
    affiliated_interfaces_odata_count: int | None = Field(
        alias="AffiliatedInterfaces@odata.count", default=None
    )
    chassis: IdRef | None = None
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(alias="Endpoints@odata.count", default=None)
    host_interface: IdRef | None = None
    network_device_function: IdRef | None = None
    network_device_functions: list[IdRef] | None = None
    network_device_functions_odata_count: int | None = Field(
        alias="NetworkDeviceFunctions@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    ports: list[IdRef] | None = None
    ports_odata_count: int | None = Field(alias="Ports@odata.count", default=None)
    related_interfaces: list[IdRef] | None = None
    related_interfaces_odata_count: int | None = Field(
        alias="RelatedInterfaces@odata.count", default=None
    )


class RoutingScope(StrEnum):
    EXTERNAL = "External"
    HOST_ONLY = "HostOnly"
    INTERNAL = "Internal"
    LIMITED = "Limited"


class StatelessAddressAutoConfiguration(RedfishModel):
    ipv4_auto_config_enabled: bool | None = Field(alias="IPv4AutoConfigEnabled", default=None)
    ipv6_auto_config_enabled: bool | None = Field(alias="IPv6AutoConfigEnabled", default=None)


class TeamMode(StrEnum):
    NONE = "None"
    ROUND_ROBIN = "RoundRobin"
    ACTIVE_BACKUP = "ActiveBackup"
    XOR = "XOR"
    BROADCAST = "Broadcast"
    IEE_E802_3AD = "IEEE802_3ad"
    ADAPTIVE_TRANSMIT_LOAD_BALANCING = "AdaptiveTransmitLoadBalancing"
    ADAPTIVE_LOAD_BALANCING = "AdaptiveLoadBalancing"

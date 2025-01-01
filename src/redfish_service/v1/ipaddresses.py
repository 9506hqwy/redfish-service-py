from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import (
    RedfishModel,
)


class AddressState(StrEnum):
    PREFERRED = "Preferred"
    DEPRECATED = "Deprecated"
    TENTATIVE = "Tentative"
    FAILED = "Failed"


class Ipv4Address(RedfishModel):
    address: str | None = None
    address_origin: Ipv4AddressOrigin | None = None
    gateway: str | None = None
    oem: dict[str, Any] | None = None
    subnet_mask: str | None = None


class Ipv4AddressOrigin(StrEnum):
    STATIC = "Static"
    DHCP = "DHCP"
    BOOTP = "BOOTP"
    IPV4_LINK_LOCAL = "IPv4LinkLocal"


class Ipv6Address(RedfishModel):
    address: str | None = None
    address_origin: Ipv6AddressOrigin | None = None
    address_state: AddressState | None = None
    oem: dict[str, Any] | None = None
    prefix_length: int | None = None


class Ipv6AddressOrigin(StrEnum):
    STATIC = "Static"
    DHCPV6 = "DHCPv6"
    LINK_LOCAL = "LinkLocal"
    SLAAC = "SLAAC"


class Ipv6GatewayStaticAddress(RedfishModel):
    address: str | None = None
    oem: dict[str, Any] | None = None
    prefix_length: int | None = None


class Ipv6StaticAddress(RedfishModel):
    address: str | None = None
    oem: dict[str, Any] | None = None
    prefix_length: int | None = None

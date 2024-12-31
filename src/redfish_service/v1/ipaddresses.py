from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
)


class Ipv4Address(RedfishModel):
    address: str | None = None
    address_origin: str | None = None
    gateway: str | None = None
    oem: dict[str, Any] | None = None
    subnet_mask: str | None = None


class Ipv6Address(RedfishModel):
    address: str | None = None
    address_origin: str | None = None
    address_state: str | None = None
    oem: dict[str, Any] | None = None
    prefix_length: str | None = None


class Ipv6GatewayStaticAddress(RedfishModel):
    address: str
    oem: dict[str, Any] | None = None
    prefix_length: str | None = None


class Ipv6StaticAddress(RedfishModel):
    address: str
    oem: dict[str, Any] | None = None
    prefix_length: str

from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class AllowDeny(RedfishResource):
    actions: Actions | None = None
    allow_type: AllowType | None = None
    description: str | None = None
    destination_port_lower: int | None = None
    destination_port_upper: int | None = None
    direction: DataDirection | None = None
    ianaprotocol_number: int | None = Field(alias="IANAProtocolNumber", default=None)
    ipaddress_lower: str | None = Field(alias="IPAddressLower", default=None)
    ipaddress_type: IpaddressType | None = Field(alias="IPAddressType", default=None)
    ipaddress_upper: str | None = Field(alias="IPAddressUpper", default=None)
    oem: dict[str, Any] | None = None
    source_port_lower: int | None = None
    source_port_upper: int | None = None
    stateful_session: bool | None = None


class AllowType(StrEnum):
    ALLOW = "Allow"
    DENY = "Deny"


class DataDirection(StrEnum):
    INGRESS = "Ingress"
    EGRESS = "Egress"


class IpaddressType(StrEnum):
    IPV4 = "IPv4"
    IPV6 = "IPv6"

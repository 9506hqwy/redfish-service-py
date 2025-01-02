from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import RedfishModel


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class AllowDeny(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    allow_type: AllowType | None = None
    description: str | None = None
    destination_port_lower: int | None = None
    destination_port_upper: int | None = None
    direction: DataDirection | None = None
    iana_protocol_number: int | None = Field(alias="IANAProtocolNumber", default=None)
    ip_address_lower: str | None = Field(alias="IPAddressLower", default=None)
    ip_address_type: IpAddressType | None = Field(alias="IPAddressType", default=None)
    ip_address_upper: str | None = Field(alias="IPAddressUpper", default=None)
    id: str
    name: str
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


class IpAddressType(StrEnum):
    IPV4 = "IPv4"
    IPV6 = "IPv6"

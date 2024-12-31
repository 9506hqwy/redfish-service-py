from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class AllowDeny(RedfishResource):
    actions: Actions | None = None
    allow_type: str | None = None
    description: str | None = None
    destination_port_lower: str | None = None
    destination_port_upper: str | None = None
    direction: str | None = None
    ianaprotocol_number: str | None = None
    ipaddress_lower: str | None = None
    ipaddress_type: str | None = None
    ipaddress_upper: str | None = None
    oem: dict[str, Any] | None = None
    source_port_lower: str | None = None
    source_port_upper: str | None = None
    stateful_session: str | None = None

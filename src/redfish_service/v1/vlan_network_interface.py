from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Vlan(RedfishModel):
    tagged: str | None = None
    vlanenable: str | None = None
    vlanid: str | None = None
    vlanpriority: str | None = None


class VlanNetworkInterface(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    oem: dict[str, Any] | None = None
    vlanenable: str | None = None
    vlanid: str | None = None
    vlanpriority: str | None = None

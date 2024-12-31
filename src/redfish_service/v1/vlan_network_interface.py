from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource


class Actions(RedfishResource):
    oem: OemActions | None = None


class OemActions(RedfishResource):
    pass


class Vlan(RedfishResource):
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

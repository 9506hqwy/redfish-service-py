from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Vlan(RedfishModel):
    tagged: str | None = None
    vlanenable: str | None = Field(alias="VLANEnable", default=None)
    vlanid: str | None = Field(alias="VLANId", default=None)
    vlanpriority: str | None = Field(alias="VLANPriority", default=None)


class VlanNetworkInterface(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    oem: dict[str, Any] | None = None
    vlanenable: str | None = Field(alias="VLANEnable", default=None)
    vlanid: str | None = Field(alias="VLANId", default=None)
    vlanpriority: str | None = Field(alias="VLANPriority", default=None)

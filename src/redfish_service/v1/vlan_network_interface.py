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
    tagged: bool | None = None
    vlanenable: bool | None = Field(alias="VLANEnable", default=None)
    vlanid: int | None = Field(alias="VLANId", default=None)
    vlanpriority: int | None = Field(alias="VLANPriority", default=None)


class VlanNetworkInterface(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    oem: dict[str, Any] | None = None
    vlanenable: bool | None = Field(alias="VLANEnable", default=None)
    vlanid: int | None = Field(alias="VLANId", default=None)
    vlanpriority: int | None = Field(alias="VLANPriority", default=None)

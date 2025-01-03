from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Vlan(RedfishModel):
    tagged: bool | None = None
    vlan_enable: bool | None = Field(alias="VLANEnable", default=None)
    vlan_id: int | None = Field(alias="VLANId", default=None)
    vlan_priority: int | None = Field(alias="VLANPriority", default=None)


class VlanNetworkInterface(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    description: str | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
    vlan_enable: bool | None = Field(alias="VLANEnable", default=None)
    vlan_id: int | None = Field(alias="VLANId", default=None)
    vlan_priority: int | None = Field(alias="VLANPriority", default=None)

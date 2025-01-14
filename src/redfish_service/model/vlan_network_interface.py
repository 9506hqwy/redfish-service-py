from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Vlan(RedfishModel):
    tagged: bool | None = None
    vlan_enable: bool | None = Field(serialization_alias="VLANEnable", default=None)
    vlan_id: int | None = Field(serialization_alias="VLANId", default=None)
    vlan_priority: int | None = Field(serialization_alias="VLANPriority", default=None)


class VlanNetworkInterface(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type",
        default="#VLanNetworkInterface.v1_3_1.VLanNetworkInterface",
    )
    actions: Actions | None = None
    description: str | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
    vlan_enable: bool | None = Field(serialization_alias="VLANEnable", default=None)
    vlan_id: int | None = Field(serialization_alias="VLANId", default=None)
    vlan_priority: int | None = Field(serialization_alias="VLANPriority", default=None)


class VlanNetworkInterfaceOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type",
        default="#VLanNetworkInterface.v1_3_1.VLanNetworkInterface",
    )
    actions: Actions | None = None
    description: str | None = None
    id: str | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    vlan_enable: bool | None = Field(serialization_alias="VLANEnable", default=None)
    vlan_id: int | None = Field(serialization_alias="VLANId", default=None)
    vlan_priority: int | None = Field(serialization_alias="VLANPriority", default=None)


class VlanNetworkInterfaceOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    oem: dict[str, Any] | None = None
    vlan_enable: bool | None = Field(serialization_alias="VLANEnable", default=None)
    vlan_id: int | None = Field(serialization_alias="VLANId", default=None)
    vlan_priority: int | None = Field(serialization_alias="VLANPriority", default=None)

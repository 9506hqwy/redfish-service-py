from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    endpoints: list[IdRef] | None = None
    endpoints_odata_count: int | None = Field(
        serialization_alias="Endpoints@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    port: IdRef | None = None


class VirtualPci2pciBridge(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type",
        default="#VirtualPCI2PCIBridge.v1_0_0.VirtualPCI2PCIBridge",
    )
    actions: Actions | None = None
    binding_status: VPpbStatusTypes | None = None
    bound_ld_id: int | None = Field(serialization_alias="BoundLDId", default=None)
    bound_pbr_id: int | None = Field(serialization_alias="BoundPBRId", default=None)
    bound_port_id: int | None = None
    description: str | None = None
    gcxlid: str | None = Field(serialization_alias="GCXLID", default=None)
    id: str
    links: Links | None = None
    name: str
    oem: dict[str, Any] | None = None
    status: Status | None = None
    vppb_id: str | None = Field(serialization_alias="VPPBId", default=None)


class VirtualPci2pciBridgeOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None


class VPpbStatusTypes(StrEnum):
    UNBOUND = "Unbound"
    BUSY = "Busy"
    BOUND_PHYSICAL_PORT = "BoundPhysicalPort"
    BOUND_LD = "BoundLD"
    BOUND_PID = "BoundPID"

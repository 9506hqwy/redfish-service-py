from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
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


class VirtualCxlSwitch(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#VirtualCXLSwitch.v1_0_0.VirtualCXLSwitch"
    )
    actions: Actions | None = None
    description: str | None = None
    hdm_decoders: int | None = Field(serialization_alias="HDMDecoders", default=None)
    id: str
    links: Links | None = None
    name: str
    oem: dict[str, Any] | None = None
    status: Status | None = None
    vcs_id: str | None = Field(serialization_alias="VCSId", default=None)
    vpp_bs: IdRef | None = Field(serialization_alias="VPPBs", default=None)

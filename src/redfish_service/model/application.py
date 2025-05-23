from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .resource import ResetType, Status


class Actions(RedfishModel):
    reset: Reset | None = Field(serialization_alias="#Application.Reset", default=None)
    oem: dict[str, Any] | None = None


class Application(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#Application.v1_0_1.Application"
    )
    actions: Actions | None = None
    description: str | None = None
    destination_ur_is: list[str] | None = Field(
        serialization_alias="DestinationURIs", default=None
    )
    id: str
    links: Links | None = None
    metrics_ur_is: list[str] | None = Field(serialization_alias="MetricsURIs", default=None)
    name: str
    oem: dict[str, Any] | None = None
    start_time: str | None = None
    status: Status | None = None
    vendor: str | None = None
    version: str | None = None


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    software_image: IdRef | None = None


class Reset(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ResetRequest(RedfishModel):
    reset_type: ResetType | None = None

from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    reset: Reset | None = Field(alias="#Application.Reset", default=None)
    oem: dict[str, Any] | None = None


class Application(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    destination_ur_is: list[str] | None = Field(alias="DestinationURIs", default=None)
    links: Links | None = None
    metrics_ur_is: list[str] | None = Field(alias="MetricsURIs", default=None)
    oem: dict[str, Any] | None = None
    start_time: str | None = None
    status: Status | None = None
    vendor: str | None = None
    version: str | None = None


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    software_image: IdRef | None = None


class Reset(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)

from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .manifest import Manifest
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    compose: Compose | None = Field(alias="#CompositionService.Compose", default=None)
    oem: dict[str, Any] | None = None


class Compose(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class ComposeRequest(RedfishModel):
    manifest: Manifest | None = None
    request_format: ComposeRequestFormat
    request_type: ComposeRequestType
    reservation_id: str | None = None


class ComposeRequestFormat(StrEnum):
    MANIFEST = "Manifest"


class ComposeRequestType(StrEnum):
    PREVIEW = "Preview"
    PREVIEW_RESERVE = "PreviewReserve"
    APPLY = "Apply"


class CompositionService(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(
        alias="@odata.type", default="#CompositionService.v1_2_3.CompositionService"
    )
    actions: Actions | None = None
    active_pool: IdRef | None = None
    allow_overprovisioning: bool | None = None
    allow_zone_affinity: bool | None = None
    composition_reservations: IdRef | None = None
    description: str | None = None
    free_pool: IdRef | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
    reservation_duration: str | None = None
    resource_blocks: IdRef | None = None
    resource_zones: IdRef | None = None
    service_enabled: bool | None = None
    status: Status | None = None


class CompositionServiceOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    allow_overprovisioning: bool | None = None
    oem: dict[str, Any] | None = None
    reservation_duration: str | None = None
    service_enabled: bool | None = None
    status: Status | None = None

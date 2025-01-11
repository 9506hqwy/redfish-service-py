from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    reset: Reset | None = Field(alias="#AggregationService.Reset", default=None)
    set_default_boot_order: SetDefaultBootOrder | None = Field(
        alias="#AggregationService.SetDefaultBootOrder", default=None
    )
    oem: dict[str, Any] | None = None


class AggregationService(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(
        alias="@odata.type", default="#AggregationService.v1_0_3.AggregationService"
    )
    actions: Actions | None = None
    aggregates: IdRef | None = None
    aggregation_sources: IdRef | None = None
    connection_methods: IdRef | None = None
    description: str | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
    service_enabled: bool | None = None
    status: Status | None = None


class AggregationServiceOnUpdate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(
        alias="@odata.type", default="#AggregationService.v1_0_3.AggregationService"
    )
    actions: Actions | None = None
    aggregates: IdRef | None = None
    aggregation_sources: IdRef | None = None
    connection_methods: IdRef | None = None
    description: str | None = None
    id: str | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    service_enabled: bool | None = None
    status: Status | None = None


class Reset(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class SetDefaultBootOrder(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)

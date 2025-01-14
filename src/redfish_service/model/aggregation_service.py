from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import ResetType, Status


class Actions(RedfishModel):
    reset: Reset | None = Field(serialization_alias="#AggregationService.Reset", default=None)
    set_default_boot_order: SetDefaultBootOrder | None = Field(
        serialization_alias="#AggregationService.SetDefaultBootOrder", default=None
    )
    oem: dict[str, Any] | None = None


class AggregationService(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#AggregationService.v1_0_3.AggregationService"
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


class AggregationServiceOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    oem: dict[str, Any] | None = None
    service_enabled: bool | None = None
    status: Status | None = None


class Reset(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ResetRequest(RedfishModel):
    batch_size: int | None = None
    delay_between_batches_in_seconds: int | None = None
    reset_type: ResetType | None = None
    target_ur_is: list[IdRef] = Field(serialization_alias="TargetURIs")


class SetDefaultBootOrder(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class SetDefaultBootOrderRequest(RedfishModel):
    systems: list[IdRef]

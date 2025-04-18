from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .resource import ResetType


class Actions(RedfishModel):
    add_elements: AddElements | None = Field(
        serialization_alias="#Aggregate.AddElements", default=None
    )
    remove_elements: RemoveElements | None = Field(
        serialization_alias="#Aggregate.RemoveElements", default=None
    )
    reset: Reset | None = Field(serialization_alias="#Aggregate.Reset", default=None)
    set_default_boot_order: SetDefaultBootOrder | None = Field(
        serialization_alias="#Aggregate.SetDefaultBootOrder", default=None
    )
    oem: dict[str, Any] | None = None


class AddElements(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class AddElementsRequest(RedfishModel):
    elements: list[IdRef]


class Aggregate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#Aggregate.v1_0_3.Aggregate"
    )
    actions: Actions | None = None
    description: str | None = None
    elements: list[IdRef]
    elements_odata_count: int | None = Field(
        serialization_alias="Elements@odata.count", default=None
    )
    elements_count: int | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None


class AggregateOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type", default="#Aggregate.v1_0_3.Aggregate"
    )
    actions: Actions | None = None
    description: str | None = None
    elements: list[IdRef]
    elements_odata_count: int | None = Field(
        serialization_alias="Elements@odata.count", default=None
    )
    elements_count: int | None = None
    id: str | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None


class RemoveElements(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class RemoveElementsRequest(RedfishModel):
    elements: list[IdRef]


class Reset(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class ResetRequest(RedfishModel):
    batch_size: int | None = None
    delay_between_batches_in_seconds: int | None = None
    reset_type: ResetType | None = None


class SetDefaultBootOrder(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)

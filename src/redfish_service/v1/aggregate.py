from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef


class Actions(RedfishModel):
    add_elements: AddElements | None = Field(alias="#Aggregate.AddElements", default=None)
    remove_elements: RemoveElements | None = Field(alias="#Aggregate.RemoveElements", default=None)
    reset: Reset | None = Field(alias="#Aggregate.Reset", default=None)
    set_default_boot_order: SetDefaultBootOrder | None = Field(
        alias="#Aggregate.SetDefaultBootOrder", default=None
    )
    oem: dict[str, Any] | None = None


class AddElements(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Aggregate(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    elements: list[IdRef]
    elements_odata_count: int | None = Field(alias="Elements@odata.count", default=None)
    elements_count: int | None = None
    oem: dict[str, Any] | None = None


class RemoveElements(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Reset(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class SetDefaultBootOrder(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)

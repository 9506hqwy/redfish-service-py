from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef


class Actions(RedfishModel):
    oem: OemActions | None = None


class AddElements(RedfishModel):
    target: str | None = None
    title: str | None = None


class Aggregate(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    elements: list[IdRef]
    elements_count: str | None = None
    oem: dict[str, Any] | None = None


class OemActions(RedfishModel):
    pass


class RemoveElements(RedfishModel):
    target: str | None = None
    title: str | None = None


class Reset(RedfishModel):
    target: str | None = None
    title: str | None = None


class SetDefaultBootOrder(RedfishModel):
    target: str | None = None
    title: str | None = None

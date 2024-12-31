from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef


class Actions(RedfishResource):
    oem: OemActions | None = None


class AddElements(RedfishResource):
    target: str | None = None
    title: str | None = None


class Aggregate(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    elements: list[IdRef]
    elements_count: str | None = None
    oem: dict[str, Any] | None = None


class OemActions(RedfishResource):
    pass


class RemoveElements(RedfishResource):
    target: str | None = None
    title: str | None = None


class Reset(RedfishResource):
    target: str | None = None
    title: str | None = None


class SetDefaultBootOrder(RedfishResource):
    target: str | None = None
    title: str | None = None

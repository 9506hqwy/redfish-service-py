from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class AggregationService(RedfishResource):
    actions: Actions | None = None
    aggregates: IdRef | None = None
    aggregation_sources: IdRef | None = None
    connection_methods: IdRef | None = None
    description: str | None = None
    oem: dict[str, Any] | None = None
    service_enabled: str | None = None
    status: Status | None = None


class OemActions(RedfishResource):
    pass


class Reset(RedfishResource):
    target: str | None = None
    title: str | None = None


class SetDefaultBootOrder(RedfishResource):
    target: str | None = None
    title: str | None = None

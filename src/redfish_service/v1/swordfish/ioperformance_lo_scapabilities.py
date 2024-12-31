from __future__ import annotations  # PEP563 Forward References

from typing import Any

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..odata_v4 import IdRef
from ..resource import Identifier
from ..schedule import Schedule


class Actions(RedfishModel):
    oem: OemActions | None = None


class IoperformanceLoScapabilities(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    iolimiting_is_supported: str | None = None
    identifier: Identifier | None = None
    max_sample_period: str | None = None
    min_sample_period: str | None = None
    min_supported_io_operation_latency_microseconds: str | None = None
    oem: dict[str, Any] | None = None
    supported_ioworkloads: list[str] | None = None
    supported_lines_of_service: list[IdRef] | None = None


class Ioworkload(RedfishModel):
    components: list[str] | None = None
    name: str | None = None


class IoworkloadComponent(RedfishModel):
    average_iobytes: str | None = None
    duration: str | None = None
    ioaccess_pattern: str | None = None
    percent_of_data: str | None = None
    percent_of_iops: str | None = None
    schedule: Schedule | None = None


class OemActions(RedfishModel):
    pass

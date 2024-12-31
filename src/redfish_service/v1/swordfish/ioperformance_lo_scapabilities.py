from __future__ import annotations  # PEP563 Forward References

from typing import Any

from ..base import RedfishResource
from ..odata_v4 import IdRef
from ..resource import Identifier
from ..schedule import Schedule


class Actions(RedfishResource):
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


class Ioworkload(RedfishResource):
    components: list[str] | None = None


class IoworkloadComponent(RedfishResource):
    average_iobytes: str | None = None
    duration: str | None = None
    ioaccess_pattern: str | None = None
    percent_of_data: str | None = None
    percent_of_iops: str | None = None
    schedule: Schedule | None = None


class OemActions(RedfishResource):
    pass

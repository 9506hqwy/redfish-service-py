from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..odata_v4 import IdRef
from ..resource import Identifier
from ..schedule import Schedule


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class IoAccessPattern(StrEnum):
    READ_WRITE = "ReadWrite"
    SEQUENTIAL_READ = "SequentialRead"
    SEQUENTIAL_WRITE = "SequentialWrite"
    RANDOM_READ_NEW = "RandomReadNew"
    RANDOM_READ_AGAIN = "RandomReadAgain"


class IoPerformanceLosCapabilities(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    io_limiting_is_supported: bool | None = Field(alias="IOLimitingIsSupported", default=None)
    identifier: Identifier | None = None
    max_sample_period: str | None = None
    min_sample_period: str | None = None
    min_supported_io_operation_latency_microseconds: int | None = None
    oem: dict[str, Any] | None = None
    supported_io_workloads: list[IoWorkload] | None = Field(
        alias="SupportedIOWorkloads", default=None
    )
    supported_lines_of_service: list[IdRef] | None = None
    supported_lines_of_service_odata_count: int | None = Field(
        alias="SupportedLinesOfService@odata.count", default=None
    )


class IoWorkload(RedfishModel):
    components: list[IoWorkloadComponent] | None = None
    name: str | None = None


class IoWorkloadComponent(RedfishModel):
    average_io_bytes: int | None = Field(alias="AverageIOBytes", default=None)
    duration: str | None = None
    io_access_pattern: IoAccessPattern | None = Field(alias="IOAccessPattern", default=None)
    percent_of_data: int | None = None
    percent_of_iops: int | None = Field(alias="PercentOfIOPS", default=None)
    schedule: Schedule | None = None

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


class IoaccessPattern(StrEnum):
    READ_WRITE = "ReadWrite"
    SEQUENTIAL_READ = "SequentialRead"
    SEQUENTIAL_WRITE = "SequentialWrite"
    RANDOM_READ_NEW = "RandomReadNew"
    RANDOM_READ_AGAIN = "RandomReadAgain"


class IoperformanceLoScapabilities(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    iolimiting_is_supported: bool | None = Field(alias="IOLimitingIsSupported", default=None)
    identifier: Identifier | None = None
    max_sample_period: str | None = None
    min_sample_period: str | None = None
    min_supported_io_operation_latency_microseconds: int | None = None
    oem: dict[str, Any] | None = None
    supported_ioworkloads: list[Ioworkload] | None = Field(
        alias="SupportedIOWorkloads", default=None
    )
    supported_lines_of_service: list[IdRef] | None = None
    supported_lines_of_service_odata_count: int | None = Field(
        alias="SupportedLinesOfService@odata.count", default=None
    )


class Ioworkload(RedfishModel):
    components: list[IoworkloadComponent] | None = None
    name: str | None = None


class IoworkloadComponent(RedfishModel):
    average_iobytes: int | None = Field(alias="AverageIOBytes", default=None)
    duration: str | None = None
    ioaccess_pattern: IoaccessPattern | None = Field(alias="IOAccessPattern", default=None)
    percent_of_data: int | None = None
    percent_of_iops: int | None = Field(alias="PercentOfIOPS", default=None)
    schedule: Schedule | None = None

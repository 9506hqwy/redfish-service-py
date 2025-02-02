from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .. import RedfishModel, RedfishModelOnUpdate
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


class IoPerformanceLosCapabilities(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type",
        default="#IOPerformanceLoSCapabilities.v1_3_0.IOPerformanceLoSCapabilities",
    )
    actions: Actions | None = None
    description: str | None = None
    io_limiting_is_supported: bool | None = Field(
        serialization_alias="IOLimitingIsSupported", default=None
    )
    id: str
    identifier: Identifier | None = None
    max_sample_period: str | None = None
    min_sample_period: str | None = None
    min_supported_io_operation_latency_microseconds: int | None = None
    name: str
    oem: dict[str, Any] | None = None
    supported_io_workloads: list[IoWorkload] | None = Field(
        serialization_alias="SupportedIOWorkloads", default=None
    )
    supported_lines_of_service: list[IdRef] | None = None
    supported_lines_of_service_odata_count: int | None = Field(
        serialization_alias="SupportedLinesOfService@odata.count", default=None
    )


class IoPerformanceLosCapabilitiesOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    io_limiting_is_supported: bool | None = Field(
        serialization_alias="IOLimitingIsSupported", default=None
    )
    identifier: Identifier | None = None
    max_sample_period: str | None = None
    min_sample_period: str | None = None
    min_supported_io_operation_latency_microseconds: int | None = None
    oem: dict[str, Any] | None = None
    supported_io_workloads: list[IoWorkload] | None = Field(
        serialization_alias="SupportedIOWorkloads", default=None
    )
    supported_lines_of_service: list[IdRef] | None = None


class IoWorkload(RedfishModel):
    components: list[IoWorkloadComponent] | None = None
    name: str | None = None


class IoWorkloadComponent(RedfishModel):
    average_io_bytes: int | None = Field(serialization_alias="AverageIOBytes", default=None)
    duration: str | None = None
    io_access_pattern: IoAccessPattern | None = Field(
        serialization_alias="IOAccessPattern", default=None
    )
    percent_of_data: int | None = None
    percent_of_iops: int | None = Field(serialization_alias="PercentOfIOPS", default=None)
    schedule: Schedule | None = None

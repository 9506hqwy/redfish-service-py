from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .storage_controller_metrics import NvmeSmartMetrics


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class DriveMetrics(RedfishResource):
    actions: Actions | None = None
    bad_block_count: int | None = None
    correctable_io_read_error_count: int | None = Field(
        alias="CorrectableIOReadErrorCount", default=None
    )
    correctable_io_write_error_count: int | None = Field(
        alias="CorrectableIOWriteErrorCount", default=None
    )
    description: str | None = None
    nvme_smart: NvmeSmartMetrics | None = Field(alias="NVMeSMART", default=None)
    native_command_queue_depth: int | None = None
    oem: dict[str, Any] | None = None
    power_on_hours: float | None = None
    read_io_kibytes: int | None = Field(alias="ReadIOKiBytes", default=None)
    uncorrectable_io_read_error_count: int | None = Field(
        alias="UncorrectableIOReadErrorCount", default=None
    )
    uncorrectable_io_write_error_count: int | None = Field(
        alias="UncorrectableIOWriteErrorCount", default=None
    )
    write_io_kibytes: int | None = Field(alias="WriteIOKiBytes", default=None)

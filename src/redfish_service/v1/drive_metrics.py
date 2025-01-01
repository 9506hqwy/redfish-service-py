from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .storage_controller_metrics import NvmeSmartmetrics


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class DriveMetrics(RedfishResource):
    actions: Actions | None = None
    bad_block_count: str | None = None
    correctable_ioread_error_count: str | None = Field(
        alias="CorrectableIOReadErrorCount", default=None
    )
    correctable_iowrite_error_count: str | None = Field(
        alias="CorrectableIOWriteErrorCount", default=None
    )
    description: str | None = None
    nvme_smart: NvmeSmartmetrics | None = Field(alias="NVMeSMART", default=None)
    native_command_queue_depth: str | None = None
    oem: dict[str, Any] | None = None
    power_on_hours: str | None = None
    read_ioki_bytes: str | None = Field(alias="ReadIOKiBytes", default=None)
    uncorrectable_ioread_error_count: str | None = Field(
        alias="UncorrectableIOReadErrorCount", default=None
    )
    uncorrectable_iowrite_error_count: str | None = Field(
        alias="UncorrectableIOWriteErrorCount", default=None
    )
    write_ioki_bytes: str | None = Field(alias="WriteIOKiBytes", default=None)

from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .storage_controller_metrics import NvmeSmartMetrics


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class DriveMetrics(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    bad_block_count: int | None = None
    correctable_io_read_error_count: int | None = Field(
        alias="CorrectableIOReadErrorCount", default=None
    )
    correctable_io_write_error_count: int | None = Field(
        alias="CorrectableIOWriteErrorCount", default=None
    )
    description: str | None = None
    id: str
    nvme_smart: NvmeSmartMetrics | None = Field(alias="NVMeSMART", default=None)
    name: str
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

from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .storage_controller_metrics import NvmeSmartMetrics


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class DriveMetrics(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#DriveMetrics.v1_3_0.DriveMetrics"
    )
    actions: Actions | None = None
    bad_block_count: int | None = None
    correctable_io_read_error_count: int | None = Field(
        serialization_alias="CorrectableIOReadErrorCount", default=None
    )
    correctable_io_write_error_count: int | None = Field(
        serialization_alias="CorrectableIOWriteErrorCount", default=None
    )
    description: str | None = None
    id: str
    lifetime_start_date_time: str | None = None
    nvme_smart: NvmeSmartMetrics | None = Field(serialization_alias="NVMeSMART", default=None)
    name: str
    native_command_queue_depth: int | None = None
    oem: dict[str, Any] | None = None
    power_on_hours: float | None = None
    read_io_kibytes: int | None = Field(serialization_alias="ReadIOKiBytes", default=None)
    uncorrectable_io_read_error_count: int | None = Field(
        serialization_alias="UncorrectableIOReadErrorCount", default=None
    )
    uncorrectable_io_write_error_count: int | None = Field(
        serialization_alias="UncorrectableIOWriteErrorCount", default=None
    )
    write_io_kibytes: int | None = Field(serialization_alias="WriteIOKiBytes", default=None)

from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .. import RedfishModel
from ..swordfish.io_statistics import IoStatistics


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class VolumeMetrics(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    consistency_check_count: float | None = None
    consistency_check_error_count: float | None = None
    correctable_io_read_error_count: int | None = Field(
        alias="CorrectableIOReadErrorCount", default=None
    )
    correctable_io_write_error_count: int | None = Field(
        alias="CorrectableIOWriteErrorCount", default=None
    )
    description: str | None = None
    io_statistics: IoStatistics | None = Field(alias="IOStatistics", default=None)
    id: str
    name: str
    oem: dict[str, Any] | None = None
    rebuild_error_count: float | None = None
    state_change_count: float | None = None
    uncorrectable_io_read_error_count: int | None = Field(
        alias="UncorrectableIOReadErrorCount", default=None
    )
    uncorrectable_io_write_error_count: int | None = Field(
        alias="UncorrectableIOWriteErrorCount", default=None
    )

from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..swordfish.iostatistics import Iostatistics


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class VolumeMetrics(RedfishResource):
    actions: Actions | None = None
    consistency_check_count: float | None = None
    consistency_check_error_count: float | None = None
    correctable_ioread_error_count: int | None = Field(
        alias="CorrectableIOReadErrorCount", default=None
    )
    correctable_iowrite_error_count: int | None = Field(
        alias="CorrectableIOWriteErrorCount", default=None
    )
    description: str | None = None
    iostatistics: Iostatistics | None = Field(alias="IOStatistics", default=None)
    oem: dict[str, Any] | None = None
    rebuild_error_count: float | None = None
    state_change_count: float | None = None
    uncorrectable_ioread_error_count: int | None = Field(
        alias="UncorrectableIOReadErrorCount", default=None
    )
    uncorrectable_iowrite_error_count: int | None = Field(
        alias="UncorrectableIOWriteErrorCount", default=None
    )

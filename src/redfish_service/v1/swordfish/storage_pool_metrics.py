from __future__ import annotations  # PEP563 Forward References

from typing import Any

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..swordfish.iostatistics import Iostatistics


class Actions(RedfishModel):
    oem: OemActions | None = None


class OemActions(RedfishModel):
    pass


class StoragePoolMetrics(RedfishResource):
    actions: Actions | None = None
    consistency_check_error_count: str | None = None
    correctable_ioread_error_count: str | None = None
    correctable_iowrite_error_count: str | None = None
    description: str | None = None
    iostatistics: Iostatistics | None = None
    oem: dict[str, Any] | None = None
    rebuild_error_count: str | None = None
    state_change_count: str | None = None
    uncorrectable_ioread_error_count: str | None = None
    uncorrectable_iowrite_error_count: str | None = None

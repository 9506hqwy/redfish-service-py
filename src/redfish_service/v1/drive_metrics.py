from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .storage_controller_metrics import NvmeSmartmetrics


class Actions(RedfishResource):
    oem: OemActions | None = None


class DriveMetrics(RedfishResource):
    actions: Actions | None = None
    bad_block_count: str | None = None
    correctable_ioread_error_count: str | None = None
    correctable_iowrite_error_count: str | None = None
    description: str | None = None
    nvme_smart: NvmeSmartmetrics | None = None
    native_command_queue_depth: str | None = None
    oem: dict[str, Any] | None = None
    power_on_hours: str | None = None
    read_ioki_bytes: str | None = None
    uncorrectable_ioread_error_count: str | None = None
    uncorrectable_iowrite_error_count: str | None = None
    write_ioki_bytes: str | None = None


class OemActions(RedfishResource):
    pass

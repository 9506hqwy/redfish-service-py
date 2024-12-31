from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .pcie_device import PcieErrors


class Actions(RedfishModel):
    oem: OemActions | None = None


class ClearCurrentPeriod(RedfishModel):
    target: str | None = None
    title: str | None = None


class CurrentPeriod(RedfishModel):
    correctable_eccerror_count: str | None = None
    uncorrectable_eccerror_count: str | None = None


class InternalMemoryMetrics(RedfishModel):
    current_period: CurrentPeriod | None = None
    life_time: LifeTime | None = None


class LifeTime(RedfishModel):
    correctable_eccerror_count: str | None = None
    uncorrectable_eccerror_count: str | None = None


class OemActions(RedfishModel):
    pass


class SwitchMetrics(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    internal_memory_metrics: InternalMemoryMetrics | None = None
    oem: dict[str, Any] | None = None
    pcie_errors: PcieErrors | None = None

from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .pcie_device import PcieErrors


class Actions(RedfishModel):
    clear_current_period: ClearCurrentPeriod | None = Field(
        alias="#SwitchMetrics.ClearCurrentPeriod", default=None
    )
    oem: dict[str, Any] | None = None


class ClearCurrentPeriod(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class CurrentPeriod(RedfishModel):
    correctable_eccerror_count: int | None = Field(alias="CorrectableECCErrorCount", default=None)
    uncorrectable_eccerror_count: int | None = Field(
        alias="UncorrectableECCErrorCount", default=None
    )


class InternalMemoryMetrics(RedfishModel):
    current_period: CurrentPeriod | None = None
    life_time: LifeTime | None = None


class LifeTime(RedfishModel):
    correctable_eccerror_count: int | None = Field(alias="CorrectableECCErrorCount", default=None)
    uncorrectable_eccerror_count: int | None = Field(
        alias="UncorrectableECCErrorCount", default=None
    )


class SwitchMetrics(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    internal_memory_metrics: InternalMemoryMetrics | None = None
    oem: dict[str, Any] | None = None
    pcie_errors: PcieErrors | None = Field(alias="PCIeErrors", default=None)

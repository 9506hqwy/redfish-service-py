from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .pcie_device import PcieErrors
from .sensor import SensorVoltageExcerpt


class Actions(RedfishModel):
    clear_current_period: ClearCurrentPeriod | None = Field(
        alias="#ProcessorMetrics.ClearCurrentPeriod", default=None
    )
    oem: dict[str, Any] | None = None


class CstateResidency(RedfishModel):
    level: str | None = None
    residency_percent: float | None = None


class CacheMetrics(RedfishModel):
    cache_miss: float | None = None
    cache_misses_per_instruction: float | None = None
    hit_ratio: float | None = None
    level: str | None = None
    occupancy_bytes: int | None = None
    occupancy_percent: float | None = None


class CacheMetricsTotal(RedfishModel):
    current_period: CurrentPeriod | None = None
    life_time: LifeTime | None = None


class ClearCurrentPeriod(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class CoreMetrics(RedfishModel):
    cstate_residency: list[CstateResidency] | None = Field(alias="CStateResidency", default=None)
    core_cache: list[CacheMetrics] | None = None
    core_id: str | None = None
    correctable_core_error_count: int | None = None
    correctable_other_error_count: int | None = None
    iostall_count: float | None = Field(alias="IOStallCount", default=None)
    instructions_per_cycle: float | None = None
    memory_stall_count: float | None = None
    uncorrectable_core_error_count: int | None = None
    uncorrectable_other_error_count: int | None = None
    unhalted_cycles: float | None = None


class CurrentPeriod(RedfishModel):
    correctable_eccerror_count: int | None = Field(alias="CorrectableECCErrorCount", default=None)
    uncorrectable_eccerror_count: int | None = Field(
        alias="UncorrectableECCErrorCount", default=None
    )


class LifeTime(RedfishModel):
    correctable_eccerror_count: int | None = Field(alias="CorrectableECCErrorCount", default=None)
    uncorrectable_eccerror_count: int | None = Field(
        alias="UncorrectableECCErrorCount", default=None
    )


class ProcessorMetrics(RedfishResource):
    actions: Actions | None = None
    average_frequency_mhz: float | None = Field(alias="AverageFrequencyMHz", default=None)
    bandwidth_percent: float | None = None
    cache: list[CacheMetrics] | None = None
    cache_metrics_total: CacheMetricsTotal | None = None
    consumed_power_watt: float | None = None
    core_metrics: list[CoreMetrics] | None = None
    core_voltage: SensorVoltageExcerpt | None = None
    correctable_core_error_count: int | None = None
    correctable_other_error_count: int | None = None
    description: str | None = None
    frequency_ratio: float | None = None
    kernel_percent: float | None = None
    local_memory_bandwidth_bytes: int | None = None
    oem: dict[str, Any] | None = None
    operating_speed_mhz: int | None = Field(alias="OperatingSpeedMHz", default=None)
    pcie_errors: PcieErrors | None = Field(alias="PCIeErrors", default=None)
    power_limit_throttle_duration: str | None = None
    remote_memory_bandwidth_bytes: int | None = None
    temperature_celsius: float | None = None
    thermal_limit_throttle_duration: str | None = None
    throttling_celsius: float | None = None
    uncorrectable_core_error_count: int | None = None
    uncorrectable_other_error_count: int | None = None
    user_percent: float | None = None

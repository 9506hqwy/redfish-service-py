from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .pcie_device import PcieErrors


class Actions(RedfishResource):
    oem: OemActions | None = None


class CstateResidency(RedfishResource):
    level: str | None = None
    residency_percent: str | None = None


class CacheMetrics(RedfishResource):
    cache_miss: str | None = None
    cache_misses_per_instruction: str | None = None
    hit_ratio: str | None = None
    level: str | None = None
    occupancy_bytes: str | None = None
    occupancy_percent: str | None = None


class CacheMetricsTotal(RedfishResource):
    current_period: CurrentPeriod | None = None
    life_time: LifeTime | None = None


class ClearCurrentPeriod(RedfishResource):
    target: str | None = None
    title: str | None = None


class CoreMetrics(RedfishResource):
    cstate_residency: list[CstateResidency] | None = None
    core_cache: list[CacheMetrics] | None = None
    core_id: str | None = None
    correctable_core_error_count: str | None = None
    correctable_other_error_count: str | None = None
    iostall_count: str | None = None
    instructions_per_cycle: str | None = None
    memory_stall_count: str | None = None
    uncorrectable_core_error_count: str | None = None
    uncorrectable_other_error_count: str | None = None
    unhalted_cycles: str | None = None


class CurrentPeriod(RedfishResource):
    correctable_eccerror_count: str | None = None
    uncorrectable_eccerror_count: str | None = None


class LifeTime(RedfishResource):
    correctable_eccerror_count: str | None = None
    uncorrectable_eccerror_count: str | None = None


class OemActions(RedfishResource):
    pass


class ProcessorMetrics(RedfishResource):
    actions: Actions | None = None
    average_frequency_mhz: str | None = None
    bandwidth_percent: str | None = None
    cache: list[CacheMetrics] | None = None
    cache_metrics_total: CacheMetricsTotal | None = None
    consumed_power_watt: str | None = None
    core_metrics: list[CoreMetrics] | None = None
    core_voltage: str | None = None
    correctable_core_error_count: str | None = None
    correctable_other_error_count: str | None = None
    description: str | None = None
    frequency_ratio: str | None = None
    kernel_percent: str | None = None
    local_memory_bandwidth_bytes: str | None = None
    oem: dict[str, Any] | None = None
    operating_speed_mhz: str | None = None
    pcie_errors: PcieErrors | None = None
    power_limit_throttle_duration: str | None = None
    remote_memory_bandwidth_bytes: str | None = None
    temperature_celsius: str | None = None
    thermal_limit_throttle_duration: str | None = None
    throttling_celsius: str | None = None
    uncorrectable_core_error_count: str | None = None
    uncorrectable_other_error_count: str | None = None
    user_percent: str | None = None

from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .physical_context import LogicalContext


class Actions(RedfishModel):
    oem: OemActions | None = None


class MetricDefinition(RedfishResource):
    accuracy: str | None = None
    actions: Actions | None = None
    calculable: str | None = None
    calculation_algorithm: str | None = None
    calculation_parameters: list[str] | None = None
    calculation_time_interval: str | None = None
    calibration: str | None = None
    description: str | None = None
    discrete_values: list[str] | None = None
    implementation: str | None = None
    is_linear: str | None = None
    logical_contexts: list[LogicalContext] | None = None
    max_reading_range: str | None = None
    metric_data_type: str | None = None
    metric_properties: list[str] | None = None
    metric_type: str | None = None
    min_reading_range: str | None = None
    oemcalculation_algorithm: str | None = None
    oem: dict[str, Any] | None = None
    physical_context: str | None = None
    precision: str | None = None
    sensing_interval: str | None = None
    timestamp_accuracy: str | None = None
    units: str | None = None
    wildcards: list[Wildcard] | None = None


class OemActions(RedfishModel):
    pass


class Wildcard(RedfishModel):
    name: str | None = None
    values: list[str] | None = None

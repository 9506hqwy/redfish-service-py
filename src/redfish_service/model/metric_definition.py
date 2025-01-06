from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .physical_context import LogicalContext, PhysicalContext


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Calculable(StrEnum):
    NON_CALCULATABLE = "NonCalculatable"
    SUMMABLE = "Summable"
    NON_SUMMABLE = "NonSummable"


class CalculationAlgorithmEnum(StrEnum):
    AVERAGE = "Average"
    MAXIMUM = "Maximum"
    MINIMUM = "Minimum"
    OEM = "OEM"


class CalculationParamsType(RedfishModel):
    result_metric: str | None = None
    source_metric: str | None = None


class ImplementationType(StrEnum):
    PHYSICAL_SENSOR = "PhysicalSensor"
    CALCULATED = "Calculated"
    SYNTHESIZED = "Synthesized"
    DIGITAL_METER = "DigitalMeter"


class MetricDataType(StrEnum):
    BOOLEAN = "Boolean"
    DATE_TIME = "DateTime"
    DECIMAL = "Decimal"
    INTEGER = "Integer"
    STRING = "String"
    ENUMERATION = "Enumeration"


class MetricDefinition(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(
        alias="@odata.type", default="#MetricDefinition.v1_3_4.MetricDefinition"
    )
    accuracy: float | None = None
    actions: Actions | None = None
    calculable: Calculable | None = None
    calculation_algorithm: CalculationAlgorithmEnum | None = None
    calculation_parameters: list[CalculationParamsType] | None = None
    calculation_time_interval: str | None = None
    calibration: float | None = None
    description: str | None = None
    discrete_values: list[str] | None = None
    id: str
    implementation: ImplementationType | None = None
    is_linear: bool | None = None
    logical_contexts: list[LogicalContext] | None = None
    max_reading_range: float | None = None
    metric_data_type: MetricDataType | None = None
    metric_properties: list[str] | None = None
    metric_type: MetricType | None = None
    min_reading_range: float | None = None
    name: str
    oem_calculation_algorithm: str | None = Field(alias="OEMCalculationAlgorithm", default=None)
    oem: dict[str, Any] | None = None
    physical_context: PhysicalContext | None = None
    precision: int | None = None
    sensing_interval: str | None = None
    timestamp_accuracy: str | None = None
    units: str | None = None
    wildcards: list[Wildcard] | None = None


class MetricDefinitionOnCreate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(
        alias="@odata.type", default="#MetricDefinition.v1_3_4.MetricDefinition"
    )
    accuracy: float | None = None
    actions: Actions | None = None
    calculable: Calculable | None = None
    calculation_algorithm: CalculationAlgorithmEnum | None = None
    calculation_parameters: list[CalculationParamsType] | None = None
    calculation_time_interval: str | None = None
    calibration: float | None = None
    description: str | None = None
    discrete_values: list[str] | None = None
    id: str | None = None
    implementation: ImplementationType | None = None
    is_linear: bool | None = None
    logical_contexts: list[LogicalContext] | None = None
    max_reading_range: float | None = None
    metric_data_type: MetricDataType | None = None
    metric_properties: list[str] | None = None
    metric_type: MetricType | None = None
    min_reading_range: float | None = None
    name: str | None = None
    oem_calculation_algorithm: str | None = Field(alias="OEMCalculationAlgorithm", default=None)
    oem: dict[str, Any] | None = None
    physical_context: PhysicalContext | None = None
    precision: int | None = None
    sensing_interval: str | None = None
    timestamp_accuracy: str | None = None
    units: str | None = None
    wildcards: list[Wildcard] | None = None


class MetricType(StrEnum):
    NUMERIC = "Numeric"
    DISCRETE = "Discrete"
    GAUGE = "Gauge"
    COUNTER = "Counter"
    COUNTDOWN = "Countdown"
    STRING = "String"


class Wildcard(RedfishModel):
    name: str | None = None
    values: list[str] | None = None

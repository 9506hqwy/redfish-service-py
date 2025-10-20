from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .pcie_device import PcieErrors


class Actions(RedfishModel):
    clear_current_period: ClearCurrentPeriod | None = Field(
        serialization_alias="#SwitchMetrics.ClearCurrentPeriod", default=None
    )
    oem: dict[str, Any] | None = None


class ClearCurrentPeriod(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class CurrentPeriod(RedfishModel):
    correctable_ecc_error_count: int | None = Field(
        serialization_alias="CorrectableECCErrorCount", default=None
    )
    uncorrectable_ecc_error_count: int | None = Field(
        serialization_alias="UncorrectableECCErrorCount", default=None
    )


class InternalMemoryMetrics(RedfishModel):
    current_period: CurrentPeriod | None = None
    life_time: LifeTime | None = None


class LifeTime(RedfishModel):
    correctable_ecc_error_count: int | None = Field(
        serialization_alias="CorrectableECCErrorCount", default=None
    )
    uncorrectable_ecc_error_count: int | None = Field(
        serialization_alias="UncorrectableECCErrorCount", default=None
    )


class SwitchMetrics(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#SwitchMetrics.v1_1_0.SwitchMetrics"
    )
    actions: Actions | None = None
    description: str | None = None
    id: str
    internal_memory_metrics: InternalMemoryMetrics | None = None
    lifetime_start_date_time: str | None = None
    name: str
    oem: dict[str, Any] | None = None
    pcie_errors: PcieErrors | None = Field(serialization_alias="PCIeErrors", default=None)

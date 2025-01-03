from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .circuit import NominalVoltageType, PhaseWiringType, PowerRestorePolicyTypes
from .odata_v4 import IdRef
from .resource import IndicatorLed, PowerState, Status
from .sensor import (
    ElectricalContext,
    SensorCurrentExcerpt,
    SensorEnergykWhExcerpt,
    SensorExcerpt,
    SensorPowerExcerpt,
    SensorVoltageExcerpt,
)


class Actions(RedfishModel):
    power_control: PowerControl | None = Field(alias="#Outlet.PowerControl", default=None)
    reset_metrics: ResetMetrics | None = Field(alias="#Outlet.ResetMetrics", default=None)
    oem: dict[str, Any] | None = None


class CurrentSensors(RedfishModel):
    line1: SensorCurrentExcerpt | None = None
    line2: SensorCurrentExcerpt | None = None
    line3: SensorCurrentExcerpt | None = None
    neutral: SensorCurrentExcerpt | None = None


class Links(RedfishModel):
    branch_circuit: IdRef | None = None
    chassis: list[IdRef] | None = None
    chassis_odata_count: int | None = Field(alias="Chassis@odata.count", default=None)
    distribution_circuits: list[IdRef] | None = None
    distribution_circuits_odata_count: int | None = Field(
        alias="DistributionCircuits@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    power_supplies: list[IdRef] | None = None
    power_supplies_odata_count: int | None = Field(alias="PowerSupplies@odata.count", default=None)


class Outlet(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    configuration_locked: bool | None = None
    current_amps: SensorCurrentExcerpt | None = None
    description: str | None = None
    electrical_consumer_names: list[str] | None = None
    electrical_context: ElectricalContext | None = None
    energyk_wh: SensorEnergykWhExcerpt | None = None
    frequency_hz: SensorExcerpt | None = None
    id: str
    indicator_led: IndicatorLed | None = Field(alias="IndicatorLED", default=None)
    links: Links | None = None
    location_indicator_active: bool | None = None
    name: str
    nominal_voltage: NominalVoltageType | None = None
    oem: dict[str, Any] | None = None
    outlet_type: ReceptacleType | None = None
    phase_wiring_type: PhaseWiringType | None = None
    poly_phase_current_amps: CurrentSensors | None = None
    poly_phase_voltage: VoltageSensors | None = None
    power_control_locked: bool | None = None
    power_cycle_delay_seconds: float | None = None
    power_enabled: bool | None = None
    power_load_percent: SensorExcerpt | None = None
    power_off_delay_seconds: float | None = None
    power_on_delay_seconds: float | None = None
    power_restore_delay_seconds: float | None = None
    power_restore_policy: PowerRestorePolicyTypes | None = None
    power_state: PowerState | None = None
    power_state_in_transition: bool | None = None
    power_watts: SensorPowerExcerpt | None = None
    rated_current_amps: float | None = None
    status: Status | None = None
    user_label: str | None = None
    voltage: SensorVoltageExcerpt | None = None
    voltage_type: VoltageType | None = None


class PowerControl(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class ReceptacleType(StrEnum):
    NEM_A_5_15_R = "NEMA_5_15R"
    NEM_A_5_20_R = "NEMA_5_20R"
    NEM_A_L5_20_R = "NEMA_L5_20R"
    NEM_A_L5_30_R = "NEMA_L5_30R"
    NEM_A_L6_20_R = "NEMA_L6_20R"
    NEM_A_L6_30_R = "NEMA_L6_30R"
    IE_C_60320_C13 = "IEC_60320_C13"
    IE_C_60320_C19 = "IEC_60320_C19"
    CE_E_7_TYPE_E = "CEE_7_Type_E"
    CE_E_7_TYPE_F = "CEE_7_Type_F"
    SE_V_1011_TYP_E_12 = "SEV_1011_TYPE_12"
    SE_V_1011_TYP_E_23 = "SEV_1011_TYPE_23"
    B_S_1363_TYPE_G = "BS_1363_Type_G"
    BUS_CONNECTION = "BusConnection"


class ResetMetrics(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class VoltageSensors(RedfishModel):
    line1_to_line2: SensorVoltageExcerpt | None = None
    line1_to_neutral: SensorVoltageExcerpt | None = None
    line2_to_line3: SensorVoltageExcerpt | None = None
    line2_to_neutral: SensorVoltageExcerpt | None = None
    line3_to_line1: SensorVoltageExcerpt | None = None
    line3_to_neutral: SensorVoltageExcerpt | None = None


class VoltageType(StrEnum):
    AC = "AC"
    DC = "DC"

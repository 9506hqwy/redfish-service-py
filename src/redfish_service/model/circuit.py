from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
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
    breaker_control: BreakerControl | None = Field(alias="#Circuit.BreakerControl", default=None)
    power_control: PowerControl | None = Field(alias="#Circuit.PowerControl", default=None)
    reset_metrics: ResetMetrics | None = Field(alias="#Circuit.ResetMetrics", default=None)
    oem: dict[str, Any] | None = None


class BreakerControl(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class BreakerStates(StrEnum):
    NORMAL = "Normal"
    TRIPPED = "Tripped"
    OFF = "Off"


class Circuit(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type", default="#Circuit.v1_8_1.Circuit")
    actions: Actions | None = None
    breaker_state: BreakerStates | None = None
    circuit_type: CircuitType | None = None
    configuration_locked: bool | None = None
    critical_circuit: bool | None = None
    current_amps: SensorCurrentExcerpt | None = None
    description: str | None = None
    electrical_consumer_names: list[str] | None = None
    electrical_context: ElectricalContext | None = None
    electrical_source_manager_uri: str | None = Field(
        alias="ElectricalSourceManagerURI", default=None
    )
    electrical_source_name: str | None = None
    energyk_wh: SensorEnergykWhExcerpt | None = None
    frequency_hz: SensorExcerpt | None = None
    id: str
    indicator_led: IndicatorLed | None = Field(alias="IndicatorLED", default=None)
    links: Links | None = None
    location_indicator_active: bool | None = None
    name: str
    nominal_frequency_hz: float | None = None
    nominal_voltage: NominalVoltageType | None = None
    oem: dict[str, Any] | None = None
    phase_wiring_type: PhaseWiringType | None = None
    plug_type: PlugType | None = None
    poly_phase_current_amps: CurrentSensors | None = None
    poly_phase_energyk_wh: EnergySensors | None = None
    poly_phase_power_watts: PowerSensors | None = None
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
    unbalanced_current_percent: SensorExcerpt | None = None
    unbalanced_voltage_percent: SensorExcerpt | None = None
    user_label: str | None = None
    voltage: SensorVoltageExcerpt | None = None
    voltage_type: VoltageType | None = None


class CircuitType(StrEnum):
    MAINS = "Mains"
    BRANCH = "Branch"
    SUBFEED = "Subfeed"
    FEEDER = "Feeder"
    BUS = "Bus"


class CurrentSensors(RedfishModel):
    line1: SensorCurrentExcerpt | None = None
    line2: SensorCurrentExcerpt | None = None
    line3: SensorCurrentExcerpt | None = None
    neutral: SensorCurrentExcerpt | None = None


class EnergySensors(RedfishModel):
    line1_to_line2: SensorEnergykWhExcerpt | None = None
    line1_to_neutral: SensorEnergykWhExcerpt | None = None
    line2_to_line3: SensorEnergykWhExcerpt | None = None
    line2_to_neutral: SensorEnergykWhExcerpt | None = None
    line3_to_line1: SensorEnergykWhExcerpt | None = None
    line3_to_neutral: SensorEnergykWhExcerpt | None = None


class Links(RedfishModel):
    branch_circuit: IdRef | None = None
    distribution_circuits: list[IdRef] | None = None
    distribution_circuits_odata_count: int | None = Field(
        alias="DistributionCircuits@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    outlets: list[IdRef] | None = None
    outlets_odata_count: int | None = Field(alias="Outlets@odata.count", default=None)
    power_outlet: IdRef | None = None
    source_circuit: IdRef | None = None


class NominalVoltageType(StrEnum):
    AC100_TO127_V = "AC100To127V"
    AC100_TO240_V = "AC100To240V"
    AC100_TO277_V = "AC100To277V"
    AC120_V = "AC120V"
    AC200_TO240_V = "AC200To240V"
    AC200_TO277_V = "AC200To277V"
    AC208_V = "AC208V"
    AC230_V = "AC230V"
    AC240_V = "AC240V"
    AC240_AND_DC380_V = "AC240AndDC380V"
    AC277_V = "AC277V"
    AC277_AND_DC380_V = "AC277AndDC380V"
    AC400_V = "AC400V"
    AC480_V = "AC480V"
    DC48_V = "DC48V"
    DC240_V = "DC240V"
    DC380_V = "DC380V"
    DC_NEG48_V = "DCNeg48V"
    DC16_V = "DC16V"
    DC12_V = "DC12V"
    DC9_V = "DC9V"
    DC5_V = "DC5V"
    D_C3_3_V = "DC3_3V"
    D_C1_8_V = "DC1_8V"


class PhaseWiringType(StrEnum):
    ONE_PHASE3_WIRE = "OnePhase3Wire"
    TWO_PHASE3_WIRE = "TwoPhase3Wire"
    ONE_OR_TWO_PHASE3_WIRE = "OneOrTwoPhase3Wire"
    TWO_PHASE4_WIRE = "TwoPhase4Wire"
    THREE_PHASE4_WIRE = "ThreePhase4Wire"
    THREE_PHASE5_WIRE = "ThreePhase5Wire"


class PlugType(StrEnum):
    NEM_A_5_15_P = "NEMA_5_15P"
    NEM_A_L5_15_P = "NEMA_L5_15P"
    NEM_A_5_20_P = "NEMA_5_20P"
    NEM_A_L5_20_P = "NEMA_L5_20P"
    NEM_A_L5_30_P = "NEMA_L5_30P"
    NEM_A_6_15_P = "NEMA_6_15P"
    NEM_A_L6_15_P = "NEMA_L6_15P"
    NEM_A_6_20_P = "NEMA_6_20P"
    NEM_A_L6_20_P = "NEMA_L6_20P"
    NEM_A_L6_30_P = "NEMA_L6_30P"
    NEM_A_L14_20_P = "NEMA_L14_20P"
    NEM_A_L14_30_P = "NEMA_L14_30P"
    NEM_A_L15_20_P = "NEMA_L15_20P"
    NEM_A_L15_30_P = "NEMA_L15_30P"
    NEM_A_L21_20_P = "NEMA_L21_20P"
    NEM_A_L21_30_P = "NEMA_L21_30P"
    NEM_A_L22_20_P = "NEMA_L22_20P"
    NEM_A_L22_30_P = "NEMA_L22_30P"
    CALIFORNIA_CS8265 = "California_CS8265"
    CALIFORNIA_CS8365 = "California_CS8365"
    IE_C_60320_C14 = "IEC_60320_C14"
    IE_C_60320_C20 = "IEC_60320_C20"
    IE_C_60309_316_P6 = "IEC_60309_316P6"
    IE_C_60309_332_P6 = "IEC_60309_332P6"
    IE_C_60309_363_P6 = "IEC_60309_363P6"
    IE_C_60309_516_P6 = "IEC_60309_516P6"
    IE_C_60309_532_P6 = "IEC_60309_532P6"
    IE_C_60309_563_P6 = "IEC_60309_563P6"
    IE_C_60309_460_P9 = "IEC_60309_460P9"
    IE_C_60309_560_P9 = "IEC_60309_560P9"
    FIELD_208_V_3_P4_W_60_A = "Field_208V_3P4W_60A"
    FIELD_400_V_3_P5_W_32_A = "Field_400V_3P5W_32A"


class PowerControl(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class PowerRestorePolicyTypes(StrEnum):
    ALWAYS_ON = "AlwaysOn"
    ALWAYS_OFF = "AlwaysOff"
    LAST_STATE = "LastState"


class PowerSensors(RedfishModel):
    line1_to_line2: SensorPowerExcerpt | None = None
    line1_to_neutral: SensorPowerExcerpt | None = None
    line2_to_line3: SensorPowerExcerpt | None = None
    line2_to_neutral: SensorPowerExcerpt | None = None
    line3_to_line1: SensorPowerExcerpt | None = None
    line3_to_neutral: SensorPowerExcerpt | None = None


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

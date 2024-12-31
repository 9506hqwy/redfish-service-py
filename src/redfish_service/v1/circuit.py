from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class BreakerControl(RedfishResource):
    target: str | None = None
    title: str | None = None


class BreakerStates(StrEnum):
    NORMAL = "Normal"
    TRIPPED = "Tripped"
    OFF = "Off"


class Circuit(RedfishResource):
    actions: Actions | None = None
    breaker_state: str | None = None
    circuit_type: str | None = None
    configuration_locked: bool | None = None
    critical_circuit: str | None = None
    current_amps: str | None = None
    description: str | None = None
    electrical_consumer_names: list[str] | None = None
    electrical_context: str | None = None
    electrical_source_manager_uri: str | None = None
    electrical_source_name: str | None = None
    energyk_wh: str | None = None
    frequency_hz: str | None = None
    indicator_led: str | None = None
    links: Links | None = None
    location_indicator_active: str | None = None
    nominal_frequency_hz: str | None = None
    nominal_voltage: str | None = None
    oem: dict[str, Any] | None = None
    phase_wiring_type: str | None = None
    plug_type: str | None = None
    poly_phase_current_amps: str | None = None
    poly_phase_energyk_wh: str | None = None
    poly_phase_power_watts: str | None = None
    poly_phase_voltage: str | None = None
    power_control_locked: bool | None = None
    power_cycle_delay_seconds: str | None = None
    power_enabled: str | None = None
    power_load_percent: str | None = None
    power_off_delay_seconds: str | None = None
    power_on_delay_seconds: str | None = None
    power_restore_delay_seconds: str | None = None
    power_restore_policy: PowerRestorePolicyTypes | None = None
    power_state: str | None = None
    power_state_in_transition: bool | None = None
    power_watts: str | None = None
    rated_current_amps: str | None = None
    status: Status | None = None
    unbalanced_current_percent: str | None = None
    unbalanced_voltage_percent: str | None = None
    user_label: str | None = None
    voltage: str | None = None
    voltage_type: str | None = None


class Links(RedfishResource):
    branch_circuit: str | None = None
    distribution_circuits: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    outlets: list[IdRef] | None = None
    power_outlet: str | None = None
    source_circuit: str | None = None


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
    DCNEG48_V = "DCNeg48V"
    DC16_V = "DC16V"
    DC12_V = "DC12V"
    DC9_V = "DC9V"
    DC5_V = "DC5V"
    DC3_3_V = "DC3_3V"
    DC1_8_V = "DC1_8V"


class OemActions(RedfishResource):
    pass


class PhaseWiringType(StrEnum):
    ONE_PHASE3_WIRE = "OnePhase3Wire"
    TWO_PHASE3_WIRE = "TwoPhase3Wire"
    ONE_OR_TWO_PHASE3_WIRE = "OneOrTwoPhase3Wire"
    TWO_PHASE4_WIRE = "TwoPhase4Wire"
    THREE_PHASE4_WIRE = "ThreePhase4Wire"
    THREE_PHASE5_WIRE = "ThreePhase5Wire"


class PlugType(StrEnum):
    NEMA_5_15_P = "NEMA_5_15P"
    NEMA__L5_15_P = "NEMA_L5_15P"
    NEMA_5_20_P = "NEMA_5_20P"
    NEMA__L5_20_P = "NEMA_L5_20P"
    NEMA__L5_30_P = "NEMA_L5_30P"
    NEMA_6_15_P = "NEMA_6_15P"
    NEMA__L6_15_P = "NEMA_L6_15P"
    NEMA_6_20_P = "NEMA_6_20P"
    NEMA__L6_20_P = "NEMA_L6_20P"
    NEMA__L6_30_P = "NEMA_L6_30P"
    NEMA__L14_20_P = "NEMA_L14_20P"
    NEMA__L14_30_P = "NEMA_L14_30P"
    NEMA__L15_20_P = "NEMA_L15_20P"
    NEMA__L15_30_P = "NEMA_L15_30P"
    NEMA__L21_20_P = "NEMA_L21_20P"
    NEMA__L21_30_P = "NEMA_L21_30P"
    NEMA__L22_20_P = "NEMA_L22_20P"
    NEMA__L22_30_P = "NEMA_L22_30P"
    CALIFORNIA__CS8265 = "California_CS8265"
    CALIFORNIA__CS8365 = "California_CS8365"
    IEC_60320__C14 = "IEC_60320_C14"
    IEC_60320__C20 = "IEC_60320_C20"
    IEC_60309_316_P6 = "IEC_60309_316P6"
    IEC_60309_332_P6 = "IEC_60309_332P6"
    IEC_60309_363_P6 = "IEC_60309_363P6"
    IEC_60309_516_P6 = "IEC_60309_516P6"
    IEC_60309_532_P6 = "IEC_60309_532P6"
    IEC_60309_563_P6 = "IEC_60309_563P6"
    IEC_60309_460_P9 = "IEC_60309_460P9"
    IEC_60309_560_P9 = "IEC_60309_560P9"
    FIELD_208_V_3_P4_W_60_A = "Field_208V_3P4W_60A"
    FIELD_400_V_3_P5_W_32_A = "Field_400V_3P5W_32A"


class PowerControl(RedfishResource):
    target: str | None = None
    title: str | None = None


class PowerRestorePolicyTypes(StrEnum):
    ALWAYS_ON = "AlwaysOn"
    ALWAYS_OFF = "AlwaysOff"
    LAST_STATE = "LastState"


class PowerState(StrEnum):
    ON = "On"
    OFF = "Off"
    POWER_CYCLE = "PowerCycle"


class ResetMetrics(RedfishResource):
    target: str | None = None
    title: str | None = None

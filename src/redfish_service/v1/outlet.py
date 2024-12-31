from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import RedfishResource
from .circuit import PowerRestorePolicyTypes
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class Links(RedfishResource):
    branch_circuit: str | None = None
    chassis: list[IdRef] | None = None
    distribution_circuits: list[IdRef] | None = None
    oem: dict[str, Any] | None = None
    power_supplies: list[IdRef] | None = None


class OemActions(RedfishResource):
    pass


class Outlet(RedfishResource):
    actions: Actions | None = None
    configuration_locked: bool | None = None
    current_amps: str | None = None
    description: str | None = None
    electrical_consumer_names: list[str] | None = None
    electrical_context: str | None = None
    energyk_wh: str | None = None
    frequency_hz: str | None = None
    indicator_led: str | None = None
    links: Links | None = None
    location_indicator_active: str | None = None
    nominal_voltage: str | None = None
    oem: dict[str, Any] | None = None
    outlet_type: str | None = None
    phase_wiring_type: str | None = None
    poly_phase_current_amps: str | None = None
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
    user_label: str | None = None
    voltage: str | None = None
    voltage_type: str | None = None


class PowerControl(RedfishResource):
    target: str | None = None
    title: str | None = None


class PowerState(StrEnum):
    ON = "On"
    OFF = "Off"
    POWER_CYCLE = "PowerCycle"


class ReceptacleType(StrEnum):
    NEMA_5_15_R = "NEMA_5_15R"
    NEMA_5_20_R = "NEMA_5_20R"
    NEMA__L5_20_R = "NEMA_L5_20R"
    NEMA__L5_30_R = "NEMA_L5_30R"
    NEMA__L6_20_R = "NEMA_L6_20R"
    NEMA__L6_30_R = "NEMA_L6_30R"
    IEC_60320__C13 = "IEC_60320_C13"
    IEC_60320__C19 = "IEC_60320_C19"
    CEE_7__TYPE__E = "CEE_7_Type_E"
    CEE_7__TYPE__F = "CEE_7_Type_F"
    SEV_1011__TYPE_12 = "SEV_1011_TYPE_12"
    SEV_1011__TYPE_23 = "SEV_1011_TYPE_23"
    BS_1363__TYPE__G = "BS_1363_Type_G"
    BUS_CONNECTION = "BusConnection"


class ResetMetrics(RedfishResource):
    target: str | None = None
    title: str | None = None

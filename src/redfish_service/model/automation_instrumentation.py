from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .automation_node import NodeState
from .control import ControlNodeExcerpt, ControlSingleLoopExcerpt
from .resource import Status
from .sensor import SensorCurrentExcerpt, SensorExcerpt, SensorVoltageExcerpt


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class AutomationInstrumentation(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type",
        default="#AutomationInstrumentation.v1_0_0.AutomationInstrumentation",
    )
    actions: Actions | None = None
    current_amps: SensorCurrentExcerpt | None = None
    description: str | None = None
    id: str
    name: str
    node_control: ControlNodeExcerpt | None = None
    node_state: NodeState | None = None
    oem: dict[str, Any] | None = None
    pid: ControlSingleLoopExcerpt | None = Field(serialization_alias="PID", default=None)
    status: Status | None = None
    temperature_celsius: SensorExcerpt | None = None
    voltage: SensorVoltageExcerpt | None = None


class AutomationInstrumentationOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    current_amps: SensorCurrentExcerpt | None = None
    node_control: ControlNodeExcerpt | None = None
    oem: dict[str, Any] | None = None
    pid: ControlSingleLoopExcerpt | None = Field(serialization_alias="PID", default=None)
    status: Status | None = None
    temperature_celsius: SensorExcerpt | None = None
    voltage: SensorVoltageExcerpt | None = None

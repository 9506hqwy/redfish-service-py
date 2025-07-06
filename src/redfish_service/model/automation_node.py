from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    reset: Reset | None = Field(serialization_alias="#AutomationNode.Reset", default=None)
    send_trigger: SendTrigger | None = Field(
        serialization_alias="#AutomationNode.SendTrigger", default=None
    )
    start: Start | None = Field(serialization_alias="#AutomationNode.Start", default=None)
    stop: Stop | None = Field(serialization_alias="#AutomationNode.Stop", default=None)
    wait: Wait | None = Field(serialization_alias="#AutomationNode.Wait", default=None)
    oem: dict[str, Any] | None = None


class AutomationNode(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#AutomationNode.v1_0_0.AutomationNode"
    )
    actions: Actions | None = None
    description: str | None = None
    id: str
    instrumentation: IdRef | None = None
    links: Links | None = None
    motion_axis: MotionAxisType | None = None
    motion_profile: MotionProfileType | None = None
    name: str
    node_state: NodeState | None = None
    node_type: NodeType | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None


class AutomationNodeOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    links: Links | None = None
    motion_axis: MotionAxisType | None = None
    motion_profile: MotionProfileType | None = None
    oem: dict[str, Any] | None = None
    status: Status | None = None


class Links(RedfishModel):
    automation_node_group: list[IdRef] | None = None
    automation_node_group_odata_count: int | None = Field(
        serialization_alias="AutomationNodeGroup@odata.count", default=None
    )
    chassis: list[IdRef] | None = None
    chassis_odata_count: int | None = Field(
        serialization_alias="Chassis@odata.count", default=None
    )
    oem: dict[str, Any] | None = None
    output_control: IdRef | None = None
    pid_feedback_sensor: IdRef | None = None
    position_sensor: IdRef | None = None
    velocity_sensor: IdRef | None = None


class MotionAxisType(StrEnum):
    X = "X"
    Y = "Y"
    Z = "Z"
    TWO_AXIS = "TwoAxis"
    THREE_AXIS = "ThreeAxis"


class MotionProfileType(StrEnum):
    TRAPEZOIDAL = "Trapezoidal"
    S_CURVE = "SCurve"
    NONE = "None"


class NodeState(StrEnum):
    IDLE = "Idle"
    DONE = "Done"
    WAITING = "Waiting"
    CONDITION_STOP = "ConditionStop"
    ERROR_STOP = "ErrorStop"
    RUNNING = "Running"


class NodeType(StrEnum):
    MOTION_POSITION = "MotionPosition"
    MOTION_VELOCITY = "MotionVelocity"
    MOTION_POSITION_GROUP = "MotionPositionGroup"
    PID = "PID"
    SIMPLE = "Simple"


class Reset(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class SendTrigger(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class Start(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class Stop(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class Wait(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)

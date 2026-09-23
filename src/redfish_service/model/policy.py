from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .resource import ResetType


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Condition(RedfishModel):
    compare_value: str | None = None
    operator: Operator | None = None
    property_path: str | None = None
    resource_path: str | None = None
    subordinate_conditions: list[Condition] | None = None
    type: ConditionType | None = None


class ConditionType(StrEnum):
    AND = "And"
    OR = "Or"
    COMPARE = "Compare"
    READ = "Read"
    SUM = "Sum"
    AVERAGE = "Average"
    EVENT = "Event"


class EventResponse(RedfishModel):
    message_args: list[str] | None = None
    message_id: str | None = None
    message_origin_of_condition: str | None = None


class HttpResponse(RedfishModel):
    body: str | None = None
    headers: dict[str, Any] | None = None
    operation: HttpVerb | None = None


class HttpVerb(StrEnum):
    GET = "GET"
    PATCH = "PATCH"
    POST = "POST"
    DELETE = "DELETE"


class Links(RedfishModel):
    oem: dict[str, Any] | None = None


class Operator(StrEnum):
    EQUAL = "Equal"
    NOT_EQUAL = "NotEqual"
    GREATER_THAN = "GreaterThan"
    LESS_THAN = "LessThan"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"


class Policy(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(serialization_alias="@odata.type", default="#Policy.v1_0_0.Policy")
    actions: Actions | None = None
    description: str | None = None
    enabled: bool | None = None
    id: str
    links: Links | None = None
    name: str
    oem: dict[str, Any] | None = None
    predefined: bool | None = None
    response: list[Response] | None = None
    trigger_condition: Condition | None = None


class PolicyOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type", default="#Policy.v1_0_0.Policy"
    )
    actions: Actions | None = None
    description: str | None = None
    enabled: bool | None = None
    id: str | None = None
    links: Links | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    predefined: bool | None = None
    response: list[Response] | None = None
    trigger_condition: Condition | None = None


class PolicyOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    enabled: bool | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    response: list[Response] | None = None
    trigger_condition: Condition | None = None


class Response(RedfishModel):
    delay_seconds: int | None = None
    event: EventResponse | None = None
    http: HttpResponse | None = Field(serialization_alias="HTTP", default=None)
    oem: dict[str, Any] | None = None
    reset_type: ResetType | None = None
    response_action: ResponseAction | None = None
    target_uri: str | None = Field(serialization_alias="TargetURI", default=None)


class ResponseAction(StrEnum):
    RECHECK = "Recheck"
    EVENT = "Event"
    RESET = "Reset"
    HTTP = "HTTP"
    OEM = "OEM"

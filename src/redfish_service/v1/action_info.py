from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)


class ActionInfo(RedfishResource):
    description: str | None = None
    oem: dict[str, Any] | None = None
    parameters: list[Parameters] | None = None


class Parameters(RedfishModel):
    allowable_numbers: list[str] | None = None
    allowable_pattern: str | None = None
    allowable_value_descriptions: list[str] | None = None
    allowable_values: list[str] | None = None
    array_size_maximum: str | None = None
    array_size_minimum: str | None = None
    data_type: str | None = None
    maximum_value: str | None = None
    minimum_value: str | None = None
    name: str
    object_data_type: str | None = None
    required: bool | None = None

from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel


class ActionInfo(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#ActionInfo.v1_4_2.ActionInfo"
    )
    description: str | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
    parameters: list[Parameters] | None = None


class ParameterTypes(StrEnum):
    BOOLEAN = "Boolean"
    NUMBER = "Number"
    NUMBER_ARRAY = "NumberArray"
    STRING = "String"
    STRING_ARRAY = "StringArray"
    OBJECT = "Object"
    OBJECT_ARRAY = "ObjectArray"


class Parameters(RedfishModel):
    allowable_numbers: list[str] | None = None
    allowable_pattern: str | None = None
    allowable_value_descriptions: list[str] | None = None
    allowable_values: list[str] | None = None
    array_size_maximum: int | None = None
    array_size_minimum: int | None = None
    data_type: ParameterTypes | None = None
    maximum_value: float | None = None
    minimum_value: float | None = None
    name: str
    object_data_type: str | None = None
    required: bool | None = None

from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class AttributeRegistry(RedfishModel):
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#AttributeRegistry.v1_3_9.AttributeRegistry"
    )
    actions: Actions | None = None
    description: str | None = None
    id: str
    language: str
    name: str
    oem: dict[str, Any] | None = None
    owning_entity: str
    registry_entries: RegistryEntries | None = None
    registry_version: str
    supported_systems: list[SupportedSystems] | None = None


class AttributeType(StrEnum):
    ENUMERATION = "Enumeration"
    STRING = "String"
    INTEGER = "Integer"
    BOOLEAN = "Boolean"
    PASSWORD = "Password"  # noqa: S105


class AttributeValue(RedfishModel):
    value_display_name: str | None = None
    value_name: str


class Attributes(RedfishModel):
    attribute_name: str
    current_value: str | None = None
    default_value: str | None = None
    display_name: str | None = None
    display_order: int | None = None
    gray_out: bool | None = None
    help_text: str | None = None
    hidden: bool | None = None
    immutable: bool | None = None
    is_system_unique_property: bool | None = None
    lower_bound: int | None = None
    max_length: int | None = None
    menu_path: str | None = None
    min_length: int | None = None
    oem: dict[str, Any] | None = None
    read_only: bool | None = None
    reset_required: bool | None = None
    scalar_increment: int | None = None
    type: AttributeType | None = None
    uefi_device_path: str | None = None
    uefi_keyword_name: str | None = None
    uefi_namespace_id: str | None = None
    upper_bound: int | None = None
    value: list[AttributeValue] | None = None
    value_expression: str | None = None
    warning_text: str | None = None
    write_only: bool | None = None


class Dependencies(RedfishModel):
    dependency: Dependency | None = None
    dependency_for: str | None = None
    type: DependencyType | None = None


class Dependency(RedfishModel):
    map_from: list[MapFrom] | None = None
    map_to_attribute: str | None = None
    map_to_property: MapToProperty | None = None
    map_to_value: str | None = None


class DependencyType(StrEnum):
    MAP = "Map"


class MapFrom(RedfishModel):
    map_from_attribute: str | None = None
    map_from_condition: MapFromCondition | None = None
    map_from_property: MapFromProperty | None = None
    map_from_value: str | None = None
    map_terms: MapTerms | None = None


class MapFromCondition(StrEnum):
    EQU = "EQU"
    NEQ = "NEQ"
    GTR = "GTR"
    GEQ = "GEQ"
    LSS = "LSS"
    LEQ = "LEQ"


class MapFromProperty(StrEnum):
    CURRENT_VALUE = "CurrentValue"
    DEFAULT_VALUE = "DefaultValue"
    READ_ONLY = "ReadOnly"
    WRITE_ONLY = "WriteOnly"
    GRAY_OUT = "GrayOut"
    HIDDEN = "Hidden"
    LOWER_BOUND = "LowerBound"
    UPPER_BOUND = "UpperBound"
    MIN_LENGTH = "MinLength"
    MAX_LENGTH = "MaxLength"
    SCALAR_INCREMENT = "ScalarIncrement"


class MapTerms(StrEnum):
    AND = "AND"
    OR = "OR"


class MapToProperty(StrEnum):
    CURRENT_VALUE = "CurrentValue"
    DEFAULT_VALUE = "DefaultValue"
    READ_ONLY = "ReadOnly"
    WRITE_ONLY = "WriteOnly"
    GRAY_OUT = "GrayOut"
    HIDDEN = "Hidden"
    IMMUTABLE = "Immutable"
    HELP_TEXT = "HelpText"
    WARNING_TEXT = "WarningText"
    DISPLAY_NAME = "DisplayName"
    DISPLAY_ORDER = "DisplayOrder"
    LOWER_BOUND = "LowerBound"
    UPPER_BOUND = "UpperBound"
    MIN_LENGTH = "MinLength"
    MAX_LENGTH = "MaxLength"
    SCALAR_INCREMENT = "ScalarIncrement"
    VALUE_EXPRESSION = "ValueExpression"


class Menus(RedfishModel):
    display_name: str | None = None
    display_order: int | None = None
    gray_out: bool | None = None
    hidden: bool | None = None
    menu_name: str | None = None
    menu_path: str | None = None
    oem: dict[str, Any] | None = None
    read_only: bool | None = None


class RegistryEntries(RedfishModel):
    attributes: list[Attributes] | None = None
    dependencies: list[Dependencies] | None = None
    menus: list[Menus] | None = None


class SupportedSystems(RedfishModel):
    firmware_version: str | None = None
    product_name: str | None = None
    system_id: str | None = None

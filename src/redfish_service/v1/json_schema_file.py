from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class JsonSchemaFile(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    languages: list[str]
    location: list[Location]
    oem: dict[str, Any] | None = None
    schema_value: str = Field(alias="Schema")


class Location(RedfishModel):
    archive_file: str | None = None
    archive_uri: str | None = None
    language: str | None = None
    publication_uri: str | None = None
    uri: str | None = None

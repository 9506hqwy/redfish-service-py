from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource


class Actions(RedfishResource):
    oem: OemActions | None = None


class JsonSchemaFile(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    languages: list[str]
    location: list[Location]
    oem: dict[str, Any] | None = None


class Location(RedfishResource):
    archive_file: str | None = None
    archive_uri: str | None = None
    language: str | None = None
    publication_uri: str | None = None
    uri: str | None = None


class OemActions(RedfishResource):
    pass

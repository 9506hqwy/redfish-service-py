from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    oem: OemActions | None = None


class Location(RedfishModel):
    archive_file: str | None = None
    archive_uri: str | None = None
    language: str | None = None
    publication_uri: str | None = None
    uri: str | None = None


class MessageRegistryFile(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    languages: list[str]
    location: list[Location]
    oem: dict[str, Any] | None = None
    registry: str


class OemActions(RedfishModel):
    pass

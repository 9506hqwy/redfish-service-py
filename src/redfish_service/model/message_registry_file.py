from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Location(RedfishModel):
    archive_file: str | None = None
    archive_uri: str | None = None
    language: str | None = None
    publication_uri: str | None = None
    uri: str | None = None


class MessageRegistryFile(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type",
        default="#MessageRegistryFile.v1_1_5.MessageRegistryFile",
    )
    actions: Actions | None = None
    description: str | None = None
    id: str
    languages: list[str]
    location: list[Location]
    name: str
    oem: dict[str, Any] | None = None
    registry: str

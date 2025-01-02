from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import RedfishModel


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class ClientType(StrEnum):
    MONITOR = "Monitor"
    CONFIGURE = "Configure"


class ManagedResource(RedfishModel):
    includes_subordinates: bool | None = None
    managed_resource_uri: str | None = Field(alias="ManagedResourceURI", default=None)
    prefer_exclusive: bool | None = None


class RegisteredClient(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    client_type: ClientType
    client_uri: str | None = Field(alias="ClientURI", default=None)
    context: str | None = None
    created_date: str | None = None
    description: str | None = None
    expiration_date: str | None = None
    id: str
    managed_resources: list[ManagedResource] | None = None
    name: str
    oem: dict[str, Any] | None = None
    sub_context: str | None = None

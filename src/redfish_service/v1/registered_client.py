from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class ClientType(StrEnum):
    MONITOR = "Monitor"
    CONFIGURE = "Configure"


class ManagedResource(RedfishModel):
    includes_subordinates: bool | None = None
    managed_resource_uri: str | None = Field(alias="ManagedResourceURI", default=None)
    prefer_exclusive: bool | None = None


class RegisteredClient(RedfishResource):
    actions: Actions | None = None
    client_type: ClientType
    client_uri: str | None = Field(alias="ClientURI", default=None)
    context: str | None = None
    created_date: str | None = None
    description: str | None = None
    expiration_date: str | None = None
    managed_resources: list[ManagedResource] | None = None
    oem: dict[str, Any] | None = None
    sub_context: str | None = None

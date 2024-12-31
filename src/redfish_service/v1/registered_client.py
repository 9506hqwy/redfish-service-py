from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class ClientType(StrEnum):
    MONITOR = "Monitor"
    CONFIGURE = "Configure"


class RegisteredClient(RedfishResource):
    actions: Actions | None = None
    client_type: ClientType
    client_uri: str | None = None
    context: str | None = None
    created_date: str | None = None
    description: str | None = None
    expiration_date: str | None = None
    managed_resources: list[str] | None = None
    oem: dict[str, Any] | None = None
    sub_context: str | None = None

from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import RedfishResource


class Actions(RedfishResource):
    oem: OemActions | None = None


class ClientType(StrEnum):
    MONITOR = "Monitor"
    CONFIGURE = "Configure"


class OemActions(RedfishResource):
    pass


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

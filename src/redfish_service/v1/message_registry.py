from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource


class Actions(RedfishResource):
    oem: OemActions | None = None


class MessageProperty(RedfishResource):
    pass


class MessageRegistry(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    language: str
    messages: MessageProperty
    oem: dict[str, Any] | None = None
    owning_entity: str
    registry_prefix: str
    registry_version: str


class OemActions(RedfishResource):
    pass

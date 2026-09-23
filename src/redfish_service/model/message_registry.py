from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class MessageRegistry(RedfishModel):
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#MessageRegistry.v1_9_0.MessageRegistry"
    )
    actions: Actions | None = None
    description: str | None = None
    id: str
    language: str | None = None
    messages: dict[str, Any] | None = None
    name: str
    oem: dict[str, Any] | None = None
    owning_entity: str | None = None
    referenced_registry: str | None = None
    registry_prefix: str | None = None
    registry_version: str | None = None
    release: str | None = None

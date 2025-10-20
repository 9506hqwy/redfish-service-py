from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class MessageRegistry(RedfishModel):
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#MessageRegistry.v1_7_0.MessageRegistry"
    )
    actions: Actions | None = None
    description: str | None = None
    id: str
    language: str
    messages: dict[str, Any]
    name: str
    oem: dict[str, Any] | None = None
    owning_entity: str
    registry_prefix: str
    registry_version: str
    release: str | None = None

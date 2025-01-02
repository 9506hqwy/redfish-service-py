from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import RedfishModel


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class MessageRegistry(RedfishModel):
    odata_type: str = Field(alias="@odata.type")
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

from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel


class Expand(StrEnum):
    NONE = "None"
    ALL = "All"
    RELEVANT = "Relevant"


class Manifest(RedfishModel):
    description: str | None = None
    expand: Expand | None = None
    stanzas: list[Stanza] | None = None
    timestamp: str | None = None


class Stanza(RedfishModel):
    oem_stanza_type: str | None = Field(alias="OEMStanzaType", default=None)
    request: dict[str, Any] | None = None
    response: dict[str, Any] | None = None
    stanza_id: str | None = None
    stanza_type: StanzaType | None = None


class StanzaType(StrEnum):
    COMPOSE_SYSTEM = "ComposeSystem"
    DECOMPOSE_SYSTEM = "DecomposeSystem"
    COMPOSE_RESOURCE = "ComposeResource"
    DECOMPOSE_RESOURCE = "DecomposeResource"
    OEM = "OEM"
    REGISTER_RESOURCE_BLOCK = "RegisterResourceBlock"

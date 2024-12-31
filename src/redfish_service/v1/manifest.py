from __future__ import annotations  # PEP563 Forward References

from .base import (
    RedfishModel,
)


class Manifest(RedfishModel):
    description: str | None = None
    expand: str | None = None
    stanzas: list[str] | None = None
    timestamp: str | None = None

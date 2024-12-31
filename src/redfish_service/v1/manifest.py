from __future__ import annotations  # PEP563 Forward References

from .base import RedfishResource


class Manifest(RedfishResource):
    description: str | None = None
    expand: str | None = None
    stanzas: list[str] | None = None
    timestamp: str | None = None

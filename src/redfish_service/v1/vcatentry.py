from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    oem: OemActions | None = None


class OemActions(RedfishModel):
    pass


class Vcatentry(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    oem: dict[str, Any] | None = None
    raw_entry_hex: str | None = None
    vcentries: list[VcatableEntry] | None = None


class VcatableEntry(RedfishModel):
    threshold: str | None = None
    vcmask: str | None = None

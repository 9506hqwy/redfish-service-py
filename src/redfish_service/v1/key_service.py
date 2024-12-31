from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef


class Actions(RedfishModel):
    oem: OemActions | None = None


class KeyService(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    nvmeo_fkey_policies: IdRef | None = None
    nvmeo_fsecrets: IdRef | None = None
    oem: dict[str, Any] | None = None


class OemActions(RedfishModel):
    pass

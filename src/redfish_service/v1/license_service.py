from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef


class Actions(RedfishResource):
    oem: OemActions | None = None


class Install(RedfishResource):
    target: str | None = None
    title: str | None = None


class LicenseService(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    license_expiration_warning_days: str | None = None
    licenses: IdRef | None = None
    oem: dict[str, Any] | None = None
    service_enabled: str | None = None


class OemActions(RedfishResource):
    pass

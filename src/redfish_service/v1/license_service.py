from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef


class Actions(RedfishModel):
    install: Install | None = Field(alias="#LicenseService.Install", default=None)
    oem: dict[str, Any] | None = None


class Install(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class LicenseService(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    license_expiration_warning_days: str | None = None
    licenses: IdRef | None = None
    oem: dict[str, Any] | None = None
    service_enabled: str | None = None

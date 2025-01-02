from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import RedfishModel
from .odata_v4 import IdRef


class Actions(RedfishModel):
    install: Install | None = Field(alias="#LicenseService.Install", default=None)
    oem: dict[str, Any] | None = None


class Install(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class LicenseService(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    description: str | None = None
    id: str
    license_expiration_warning_days: int | None = None
    licenses: IdRef | None = None
    name: str
    oem: dict[str, Any] | None = None
    service_enabled: bool | None = None

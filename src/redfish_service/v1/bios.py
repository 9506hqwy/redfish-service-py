from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef


class Actions(RedfishModel):
    change_password: ChangePassword | None = Field(alias="#Bios.ChangePassword", default=None)
    reset_bios: ResetBios | None = Field(alias="#Bios.ResetBios", default=None)
    oem: dict[str, Any] | None = None


class Bios(RedfishResource):
    actions: Actions | None = None
    attribute_registry: str | None = None
    attributes: dict[str, Any] | None = None
    description: str | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    reset_bios_to_defaults_pending: bool | None = None


class ChangePassword(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class Links(RedfishModel):
    active_software_image: IdRef | None = None
    oem: dict[str, Any] | None = None
    software_images: list[IdRef] | None = None
    software_images_odata_count: int | None = Field(
        alias="SoftwareImages@odata.count", default=None
    )


class ResetBios(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)

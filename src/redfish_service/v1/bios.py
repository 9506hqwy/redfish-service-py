from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef


class Actions(RedfishResource):
    oem: OemActions | None = None


class Attributes(RedfishResource):
    pass


class Bios(RedfishResource):
    actions: Actions | None = None
    attribute_registry: str | None = None
    attributes: Attributes | None = None
    description: str | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    reset_bios_to_defaults_pending: str | None = None


class ChangePassword(RedfishResource):
    target: str | None = None
    title: str | None = None


class Links(RedfishResource):
    active_software_image: IdRef | None = None
    oem: dict[str, Any] | None = None
    software_images: list[IdRef] | None = None


class OemActions(RedfishResource):
    pass


class ResetBios(RedfishResource):
    target: str | None = None
    title: str | None = None

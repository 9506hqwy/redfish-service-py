from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    eject_media: EjectMedia | None = Field(alias="#VirtualMedia.EjectMedia", default=None)
    insert_media: InsertMedia | None = Field(alias="#VirtualMedia.InsertMedia", default=None)
    oem: dict[str, Any] | None = None


class EjectMedia(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class InsertMedia(RedfishModel):
    target: str | None = Field(alias="target", default=None)
    title: str | None = Field(alias="title", default=None)


class MediaType(StrEnum):
    CD = "CD"
    FLOPPY = "Floppy"
    USBSTICK = "USBStick"
    DVD = "DVD"


class VirtualMedia(RedfishResource):
    actions: Actions | None = None
    certificates: IdRef | None = None
    client_certificates: IdRef | None = None
    connected_via: str | None = None
    description: str | None = None
    eject_policy: str | None = None
    eject_timeout: str | None = None
    image: str | None = None
    image_name: str | None = None
    inserted: str | None = None
    media_types: list[MediaType] | None = None
    oem: dict[str, Any] | None = None
    password: str | None = None
    status: Status | None = None
    transfer_method: str | None = None
    transfer_protocol_type: str | None = None
    user_name: str | None = None
    verify_certificate: str | None = None
    write_protected: str | None = None

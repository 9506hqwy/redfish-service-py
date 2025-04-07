from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    eject_media: EjectMedia | None = Field(
        serialization_alias="#VirtualMedia.EjectMedia", default=None
    )
    insert_media: InsertMedia | None = Field(
        serialization_alias="#VirtualMedia.InsertMedia", default=None
    )
    oem: dict[str, Any] | None = None


class ConnectedVia(StrEnum):
    NOT_CONNECTED = "NotConnected"
    URI = "URI"
    APPLET = "Applet"
    OEM = "Oem"


class EjectMedia(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class EjectPolicy(StrEnum):
    ON_POWER_OFF = "OnPowerOff"
    SESSION = "Session"
    TIMED = "Timed"
    AFTER_USE = "AfterUse"
    PERSISTENT = "Persistent"


class InsertMedia(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class InsertMediaRequest(RedfishModel):
    image: str
    inserted: bool | None = None
    password: str | None = None
    transfer_method: TransferMethod | None = None
    transfer_protocol_type: TransferProtocolType | None = None
    user_name: str | None = None
    write_protected: bool | None = None


class MediaType(StrEnum):
    CD = "CD"
    FLOPPY = "Floppy"
    USB_STICK = "USBStick"
    DVD = "DVD"


class TransferMethod(StrEnum):
    STREAM = "Stream"
    UPLOAD = "Upload"


class TransferProtocolType(StrEnum):
    CIFS = "CIFS"
    FTP = "FTP"
    SFTP = "SFTP"
    HTTP = "HTTP"
    HTTPS = "HTTPS"
    NFS = "NFS"
    SCP = "SCP"
    TFTP = "TFTP"
    OEM = "OEM"


class VirtualMedia(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#VirtualMedia.v1_6_5.VirtualMedia"
    )
    actions: Actions | None = None
    certificates: IdRef | None = None
    client_certificates: IdRef | None = None
    connected_via: ConnectedVia | None = None
    description: str | None = None
    eject_policy: EjectPolicy | None = None
    eject_timeout: str | None = None
    id: str
    image: str | None = None
    image_name: str | None = None
    inserted: bool | None = None
    media_types: list[MediaType] | None = None
    name: str
    oem: dict[str, Any] | None = None
    password: str | None = None
    status: Status | None = None
    transfer_method: TransferMethod | None = None
    transfer_protocol_type: TransferProtocolType | None = None
    user_name: str | None = None
    verify_certificate: bool | None = None
    write_protected: bool | None = None


class VirtualMediaOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    eject_policy: EjectPolicy | None = None
    eject_timeout: str | None = None
    image: str | None = None
    inserted: bool | None = None
    oem: dict[str, Any] | None = None
    password: str | None = None
    status: Status | None = None
    transfer_method: TransferMethod | None = None
    transfer_protocol_type: TransferProtocolType | None = None
    user_name: str | None = None
    verify_certificate: bool | None = None
    write_protected: bool | None = None

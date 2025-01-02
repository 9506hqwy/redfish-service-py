from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import RedfishModel
from .odata_v4 import IdRef


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    outbound_connection: IdRef | None = None


class Session(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")
    actions: Actions | None = None
    client_origin_ip_address: str | None = Field(alias="ClientOriginIPAddress", default=None)
    context: str | None = None
    created_time: str | None = None
    description: str | None = None
    id: str
    links: Links | None = None
    name: str
    oem: dict[str, Any] | None = None
    oem_session_type: str | None = None
    password: str | None = None
    roles: list[str] | None = None
    session_type: SessionTypes | None = None
    token: str | None = None
    user_name: str | None = None


class SessionTypes(StrEnum):
    HOST_CONSOLE = "HostConsole"
    MANAGER_CONSOLE = "ManagerConsole"
    IPMI = "IPMI"
    KVMIP = "KVMIP"
    OEM = "OEM"
    REDFISH = "Redfish"
    VIRTUAL_MEDIA = "VirtualMedia"
    WEB_UI = "WebUI"
    OUTBOUND_CONNECTION = "OutboundConnection"

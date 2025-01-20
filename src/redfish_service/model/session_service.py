from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class SessionService(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#SessionService.v1_2_0.SessionService"
    )
    absolute_session_timeout: int | None = None
    absolute_session_timeout_enabled: bool | None = None
    actions: Actions | None = None
    description: str | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None
    service_enabled: bool | None = None
    session_timeout: int | None = None
    sessions: IdRef | None = None
    status: Status | None = None


class SessionServiceOnUpdate(RedfishModelOnUpdate):
    absolute_session_timeout: int | None = None
    absolute_session_timeout_enabled: bool | None = None
    actions: Actions | None = None
    oem: dict[str, Any] | None = None
    service_enabled: bool | None = None
    session_timeout: int | None = None
    status: Status | None = None

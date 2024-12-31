from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef


class Actions(RedfishModel):
    oem: OemActions | None = None


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    outbound_connection: IdRef | None = None


class OemActions(RedfishModel):
    pass


class Session(RedfishResource):
    actions: Actions | None = None
    client_origin_ipaddress: str | None = None
    context: str | None = None
    created_time: str | None = None
    description: str | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    oem_session_type: str | None = None
    password: str | None = None
    roles: list[str] | None = None
    session_type: str | None = None
    token: str | None = None
    user_name: str | None = None

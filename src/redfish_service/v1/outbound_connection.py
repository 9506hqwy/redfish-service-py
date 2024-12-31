from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: OemActions | None = None


class HttpheaderProperty(RedfishModel):
    pass


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    session: str | None = None


class OemActions(RedfishModel):
    pass


class OutboundConnection(RedfishResource):
    actions: Actions | None = None
    authentication: str | None = None
    certificates: IdRef | None = None
    client_certificates: IdRef | None = None
    connection_enabled: str | None = None
    description: str | None = None
    endpoint_uri: str | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    pre_upgrade_httpheaders: HttpheaderProperty | None = None
    retry_policy: RetryPolicyType | None = None
    roles: list[str] | None = None
    status: Status | None = None
    web_socket_ping_interval_minutes: str | None = None


class RetryPolicyType(RedfishModel):
    connection_retry_policy: str | None = None
    retry_count: str | None = None
    retry_interval_minutes: str | None = None

from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel, RedfishModelOnUpdate
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class AuthenticationType(StrEnum):
    MTLS = "MTLS"
    JWT = "JWT"
    NONE = "None"
    OEM = "OEM"


class Links(RedfishModel):
    oem: dict[str, Any] | None = None
    session: IdRef | None = None


class OutboundConnection(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(
        alias="@odata.type", default="#OutboundConnection.v1_0_2.OutboundConnection"
    )
    actions: Actions | None = None
    authentication: AuthenticationType | None = None
    certificates: IdRef | None = None
    client_certificates: IdRef | None = None
    connection_enabled: bool | None = None
    description: str | None = None
    endpoint_uri: str | None = Field(alias="EndpointURI", default=None)
    id: str
    links: Links | None = None
    name: str
    oem: dict[str, Any] | None = None
    pre_upgrade_http_headers: dict[str, Any] | None = Field(
        alias="PreUpgradeHTTPHeaders", default=None
    )
    retry_policy: RetryPolicyType | None = None
    roles: list[str] | None = None
    status: Status | None = None
    web_socket_ping_interval_minutes: int | None = None


class OutboundConnectionOnCreate(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str | None = Field(alias="@odata.id", default=None)
    odata_type: str | None = Field(
        alias="@odata.type", default="#OutboundConnection.v1_0_2.OutboundConnection"
    )
    actions: Actions | None = None
    authentication: AuthenticationType | None = None
    certificates: IdRef | None = None
    client_certificates: IdRef | None = None
    connection_enabled: bool | None = None
    description: str | None = None
    endpoint_uri: str = Field(alias="EndpointURI")
    id: str | None = None
    links: Links | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    pre_upgrade_http_headers: dict[str, Any] | None = Field(
        alias="PreUpgradeHTTPHeaders", default=None
    )
    retry_policy: RetryPolicyType | None = None
    roles: list[str]
    status: Status | None = None
    web_socket_ping_interval_minutes: int | None = None


class OutboundConnectionOnUpdate(RedfishModelOnUpdate):
    actions: Actions | None = None
    connection_enabled: bool | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    pre_upgrade_http_headers: dict[str, Any] | None = Field(
        alias="PreUpgradeHTTPHeaders", default=None
    )
    retry_policy: RetryPolicyType | None = None
    status: Status | None = None
    web_socket_ping_interval_minutes: int | None = None


class OutboundConnectionRetryPolicyType(StrEnum):
    NONE = "None"
    RETRY_FOREVER = "RetryForever"
    RETRY_COUNT = "RetryCount"


class RetryPolicyType(RedfishModel):
    connection_retry_policy: OutboundConnectionRetryPolicyType | None = None
    retry_count: int | None = None
    retry_interval_minutes: int | None = None

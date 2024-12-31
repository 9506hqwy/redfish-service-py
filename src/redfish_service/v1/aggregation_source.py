from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: OemActions | None = None


class AggregationSource(RedfishResource):
    actions: Actions | None = None
    aggregation_type: AggregationType | None = None
    description: str | None = None
    host_name: str | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    password: str | None = None
    snmp: Snmpsettings | None = None
    sshsettings: SshsettingsType | None = None
    status: Status | None = None
    user_name: str | None = None


class AggregationType(StrEnum):
    NOTIFICATIONS_ONLY = "NotificationsOnly"
    FULL = "Full"


class GenerateSshidentityKeyPair(RedfishModel):
    target: str | None = None
    title: str | None = None


class Links(RedfishModel):
    connection_method: IdRef | None = None
    oem: dict[str, Any] | None = None
    resources_accessed: list[IdRef] | None = None


class OemActions(RedfishModel):
    pass


class RemoveSshidentityKeyPair(RedfishModel):
    target: str | None = None
    title: str | None = None


class Snmpsettings(RedfishModel):
    authentication_key: str | None = None
    authentication_key_set: bool | None = None
    authentication_protocol: str | None = None
    encryption_key: str | None = None
    encryption_key_set: bool | None = None
    encryption_protocol: str | None = None
    trap_community: str | None = None


class SshsettingsType(RedfishModel):
    presented_public_host_key: IdRef | None = None
    presented_public_host_key_timestamp: str | None = None
    public_identity_key: IdRef | None = None
    trusted_public_host_keys: IdRef | None = None
    user_authentication_method: str | None = None

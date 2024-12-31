from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from .base import RedfishResource
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishResource):
    oem: OemActions | None = None


class ApplyTime(StrEnum):
    IMMEDIATE = "Immediate"
    ON_RESET = "OnReset"
    AT_MAINTENANCE_WINDOW_START = "AtMaintenanceWindowStart"
    IN_MAINTENANCE_WINDOW_ON_RESET = "InMaintenanceWindowOnReset"


class HttpPushUriApplyTime(RedfishResource):
    apply_time: ApplyTime | None = None
    maintenance_window_duration_in_seconds: int | None = None
    maintenance_window_start_time: str | None = None


class HttpPushUriOptions(RedfishResource):
    http_push_uri_apply_time: HttpPushUriApplyTime | None = None


class OemActions(RedfishResource):
    pass


class SimpleUpdate(RedfishResource):
    target: str | None = None
    title: str | None = None


class StartUpdate(RedfishResource):
    target: str | None = None
    title: str | None = None


class UpdateParameters(RedfishResource):
    oem: dict[str, Any] | None = None
    targets: list[str] | None = None


class UpdateService(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    firmware_inventory: IdRef | None = None
    http_push_uri: str | None = None
    http_push_uri_options: HttpPushUriOptions | None = None
    http_push_uri_options_busy: str | None = None
    http_push_uri_targets: list[str] | None = None
    http_push_uri_targets_busy: str | None = None
    max_image_size_bytes: str | None = None
    multipart_http_push_uri: str | None = None
    oem: dict[str, Any] | None = None
    remote_server_certificates: IdRef | None = None
    service_enabled: str | None = None
    software_inventory: IdRef | None = None
    status: Status | None = None
    verify_remote_server_certificate: str | None = None

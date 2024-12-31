from __future__ import annotations  # PEP563 Forward References

from typing import Any

from ..base import (
    RedfishModel,
    RedfishResource,
)


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class DataSecurityLineOfService(RedfishResource):
    actions: Actions | None = None
    antivirus_engine_provider: str | None = None
    antivirus_scan_policies: list[str] | None = None
    channel_encryption_strength: str | None = None
    data_sanitization_policy: str | None = None
    description: str | None = None
    host_authentication_type: str | None = None
    media_encryption_strength: str | None = None
    oem: dict[str, Any] | None = None
    secure_channel_protocol: str | None = None
    user_authentication_type: str | None = None

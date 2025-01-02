from __future__ import annotations  # PEP563 Forward References

from typing import Any

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..swordfish.data_security_los_capabilities import (
    AntiVirusScanTrigger,
    AuthenticationType,
    DataSanitizationPolicy,
    KeySize,
    SecureChannelProtocol,
)


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class DataSecurityLineOfService(RedfishResource):
    actions: Actions | None = None
    antivirus_engine_provider: str | None = None
    antivirus_scan_policies: list[AntiVirusScanTrigger] | None = None
    channel_encryption_strength: KeySize | None = None
    data_sanitization_policy: DataSanitizationPolicy | None = None
    description: str | None = None
    host_authentication_type: AuthenticationType | None = None
    media_encryption_strength: KeySize | None = None
    oem: dict[str, Any] | None = None
    secure_channel_protocol: SecureChannelProtocol | None = None
    user_authentication_type: AuthenticationType | None = None

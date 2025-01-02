from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..odata_v4 import IdRef
from ..resource import Identifier


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class AntiVirusScanTrigger(StrEnum):
    NONE = "None"
    ON_FIRST_READ = "OnFirstRead"
    ON_PATTERN_UPDATE = "OnPatternUpdate"
    ON_UPDATE = "OnUpdate"
    ON_RENAME = "OnRename"


class AuthenticationType(StrEnum):
    NONE = "None"
    PKI = "PKI"
    TICKET = "Ticket"
    PASSWORD = "Password"  # noqa: S105


class DataSanitizationPolicy(StrEnum):
    NONE = "None"
    CLEAR = "Clear"
    CRYPTOGRAPHIC_ERASE = "CryptographicErase"


class DataSecurityLosCapabilities(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    identifier: Identifier | None = None
    oem: dict[str, Any] | None = None
    supported_antivirus_engine_providers: list[str] | None = None
    supported_antivirus_scan_policies: list[AntiVirusScanTrigger] | None = None
    supported_channel_encryption_strengths: list[KeySize] | None = None
    supported_data_sanitization_policies: list[DataSanitizationPolicy] | None = None
    supported_host_authentication_types: list[AuthenticationType] | None = None
    supported_lines_of_service: list[IdRef] | None = None
    supported_lines_of_service_odata_count: int | None = Field(
        alias="SupportedLinesOfService@odata.count", default=None
    )
    supported_media_encryption_strengths: list[KeySize] | None = None
    supported_secure_channel_protocols: list[SecureChannelProtocol] | None = None
    supported_user_authentication_types: list[AuthenticationType] | None = None


class KeySize(StrEnum):
    BITS_0 = "Bits_0"
    BITS_112 = "Bits_112"
    BITS_128 = "Bits_128"
    BITS_192 = "Bits_192"
    BITS_256 = "Bits_256"


class SecureChannelProtocol(StrEnum):
    NONE = "None"
    TLS = "TLS"
    I_PSEC = "IPsec"
    RPCSE_C_GSS = "RPCSEC_GSS"

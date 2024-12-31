from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

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


class DataSecurityLoScapabilities(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    identifier: Identifier | None = None
    oem: dict[str, Any] | None = None
    supported_antivirus_engine_providers: list[str] | None = None
    supported_antivirus_scan_policies: list[str] | None = None
    supported_channel_encryption_strengths: list[str] | None = None
    supported_data_sanitization_policies: list[str] | None = None
    supported_host_authentication_types: list[str] | None = None
    supported_lines_of_service: list[IdRef] | None = None
    supported_media_encryption_strengths: list[str] | None = None
    supported_secure_channel_protocols: list[str] | None = None
    supported_user_authentication_types: list[str] | None = None


class KeySize(StrEnum):
    BITS_0 = "Bits_0"
    BITS_112 = "Bits_112"
    BITS_128 = "Bits_128"
    BITS_192 = "Bits_192"
    BITS_256 = "Bits_256"


class SecureChannelProtocol(StrEnum):
    NONE = "None"
    TLS = "TLS"
    IPSEC = "IPsec"
    RPCSEC__GSS = "RPCSEC_GSS"

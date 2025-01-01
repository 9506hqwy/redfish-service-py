from __future__ import annotations  # PEP563 Forward References

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


class ClassOfService(RedfishResource):
    actions: Actions | None = None
    class_of_service_version: str | None = None
    data_protection_lines_of_service: list[IdRef] | None = None
    data_protection_lines_of_service_odata_count: int | None = Field(
        alias="DataProtectionLinesOfService@odata.count", default=None
    )
    data_security_lines_of_service: list[IdRef] | None = None
    data_security_lines_of_service_odata_count: int | None = Field(
        alias="DataSecurityLinesOfService@odata.count", default=None
    )
    data_storage_lines_of_service: list[IdRef] | None = None
    data_storage_lines_of_service_odata_count: int | None = Field(
        alias="DataStorageLinesOfService@odata.count", default=None
    )
    description: str | None = None
    ioconnectivity_lines_of_service: list[IdRef] | None = Field(
        alias="IOConnectivityLinesOfService", default=None
    )
    ioconnectivity_lines_of_service_odata_count: int | None = Field(
        alias="IOConnectivityLinesOfService@odata.count", default=None
    )
    ioperformance_lines_of_service: list[IdRef] | None = Field(
        alias="IOPerformanceLinesOfService", default=None
    )
    ioperformance_lines_of_service_odata_count: int | None = Field(
        alias="IOPerformanceLinesOfService@odata.count", default=None
    )
    identifier: Identifier | None = None
    oem: dict[str, Any] | None = None

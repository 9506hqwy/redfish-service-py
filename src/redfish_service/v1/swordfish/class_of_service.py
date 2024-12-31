from __future__ import annotations  # PEP563 Forward References

from typing import Any

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
    data_security_lines_of_service: list[IdRef] | None = None
    data_storage_lines_of_service: list[IdRef] | None = None
    description: str | None = None
    ioconnectivity_lines_of_service: list[IdRef] | None = None
    ioperformance_lines_of_service: list[IdRef] | None = None
    identifier: Identifier | None = None
    oem: dict[str, Any] | None = None

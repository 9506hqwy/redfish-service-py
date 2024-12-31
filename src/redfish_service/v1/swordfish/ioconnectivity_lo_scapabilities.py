from __future__ import annotations  # PEP563 Forward References

from typing import Any

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..odata_v4 import IdRef
from ..resource import Identifier


class Actions(RedfishModel):
    oem: OemActions | None = None


class IoconnectivityLoScapabilities(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    identifier: Identifier | None = None
    max_supported_bytes_per_second: str | None = None
    max_supported_iops: str | None = None
    oem: dict[str, Any] | None = None
    supported_access_protocols: list[str] | None = None
    supported_lines_of_service: list[IdRef] | None = None


class OemActions(RedfishModel):
    pass

from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..protocol import Protocol


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class IoconnectivityLineOfService(RedfishResource):
    access_protocols: list[Protocol] | None = None
    actions: Actions | None = None
    description: str | None = None
    max_bytes_per_second: int | None = None
    max_iops: int | None = Field(alias="MaxIOPS", default=None)
    oem: dict[str, Any] | None = None

from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from ..base import (
    RedfishModel,
    RedfishResource,
)
from ..swordfish.iostatistics import Iostatistics


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class FileSystemMetrics(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    iostatistics: Iostatistics | None = Field(alias="IOStatistics", default=None)
    oem: dict[str, Any] | None = None

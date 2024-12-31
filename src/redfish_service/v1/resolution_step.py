from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import (
    RedfishModel,
)


class ResolutionStep(RedfishModel):
    action_parameters: list[str] | None = None
    action_uri: str | None = None
    oem: dict[str, Any] | None = None
    priority: str | None = None
    resolution_type: str
    retry_count: str | None = None
    retry_interval_seconds: str | None = None
    target_component_uri: str | None = None

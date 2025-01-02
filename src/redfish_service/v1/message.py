from __future__ import annotations  # PEP563 Forward References

from typing import Any

from .base import RedfishModel
from .resolution_step import ResolutionStep
from .resource import Health


class Message(RedfishModel):
    message: str | None = None
    message_args: list[str] | None = None
    message_id: str
    message_severity: Health | None = None
    oem: dict[str, Any] | None = None
    related_properties: list[str] | None = None
    resolution: str | None = None
    resolution_steps: list[ResolutionStep] | None = None
    severity: str | None = None
    user_authentication_source: str | None = None
    username: str | None = None

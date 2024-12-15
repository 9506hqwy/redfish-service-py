from pydantic import Field

from .base import RedfishModel
from .resource import Health, Oem


class Message(RedfishModel):
    message: str | None = Field(default=None)
    message_args: list[str] | None = Field(default=None)
    message_id: str
    message_severity: Health | None = Field(default=None)
    oem: Oem | None = Field(default=None)
    related_properties: list[str] | None = Field(default=None)
    resolution: str | None = Field(default=None)
    # resolution_steps: list[] | None = Field(default=None)
    severity: str | None = Field(default=None)
    user_authentication_source: str | None = Field(default=None)
    username: str | None = Field(default=None)

from __future__ import annotations  # PEP563 Forward References

from pydantic import Field

from . import RedfishModel
from .message import Message


class RedfishError(RedfishModel):
    error: RedfishErrorContents = Field(alias="error")


class RedfishErrorContents(RedfishModel):
    code: str = Field(alias="code")
    message: str = Field(alias="message")
    message_extended_info: list[Message] | None = Field(
        alias="@Message.ExtendedInfo", default=None
    )

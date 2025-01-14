from __future__ import annotations  # PEP563 Forward References

from pydantic import Field

from . import RedfishModel
from .message import Message


class RedfishError(RedfishModel):
    error: RedfishErrorContents = Field(serialization_alias="error")


class RedfishErrorContents(RedfishModel):
    code: str = Field(serialization_alias="code")
    message: str = Field(serialization_alias="message")
    message_extended_info: list[Message] | None = Field(
        serialization_alias="@Message.ExtendedInfo", default=None
    )

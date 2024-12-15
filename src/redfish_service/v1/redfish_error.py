from pydantic import BaseModel, Field

from .message import Message


class RedfishErrorContents(BaseModel):
    code: str
    message: str
    message_extended_info: Message | None = Field(alias="@Message.ExtendedInfo", default=None)


class RedfishError(BaseModel):
    error: RedfishErrorContents

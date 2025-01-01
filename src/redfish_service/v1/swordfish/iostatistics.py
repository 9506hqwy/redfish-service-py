from __future__ import annotations  # PEP563 Forward References

from pydantic import Field

from ..base import (
    RedfishModel,
)


class Iostatistics(RedfishModel):
    non_iorequest_time: str | None = Field(alias="NonIORequestTime", default=None)
    non_iorequests: int | None = Field(alias="NonIORequests", default=None)
    read_hit_iorequests: int | None = Field(alias="ReadHitIORequests", default=None)
    read_ioki_bytes: int | None = Field(alias="ReadIOKiBytes", default=None)
    read_iorequest_time: str | None = Field(alias="ReadIORequestTime", default=None)
    read_iorequests: int | None = Field(alias="ReadIORequests", default=None)
    write_hit_iorequests: int | None = Field(alias="WriteHitIORequests", default=None)
    write_ioki_bytes: int | None = Field(alias="WriteIOKiBytes", default=None)
    write_iorequest_time: str | None = Field(alias="WriteIORequestTime", default=None)
    write_iorequests: int | None = Field(alias="WriteIORequests", default=None)

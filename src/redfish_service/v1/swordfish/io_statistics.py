from __future__ import annotations  # PEP563 Forward References

from pydantic import Field

from .. import RedfishModel


class IoStatistics(RedfishModel):
    non_io_request_time: str | None = Field(alias="NonIORequestTime", default=None)
    non_io_requests: int | None = Field(alias="NonIORequests", default=None)
    read_hit_io_requests: int | None = Field(alias="ReadHitIORequests", default=None)
    read_io_kibytes: int | None = Field(alias="ReadIOKiBytes", default=None)
    read_io_request_time: str | None = Field(alias="ReadIORequestTime", default=None)
    read_io_requests: int | None = Field(alias="ReadIORequests", default=None)
    write_hit_io_requests: int | None = Field(alias="WriteHitIORequests", default=None)
    write_io_kibytes: int | None = Field(alias="WriteIOKiBytes", default=None)
    write_io_request_time: str | None = Field(alias="WriteIORequestTime", default=None)
    write_io_requests: int | None = Field(alias="WriteIORequests", default=None)

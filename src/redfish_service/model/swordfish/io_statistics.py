from __future__ import annotations  # PEP563 Forward References

from pydantic import Field

from .. import RedfishModel


class IoStatistics(RedfishModel):
    non_io_request_time: str | None = Field(serialization_alias="NonIORequestTime", default=None)
    non_io_requests: int | None = Field(serialization_alias="NonIORequests", default=None)
    read_hit_io_requests: int | None = Field(serialization_alias="ReadHitIORequests", default=None)
    read_io_kibytes: int | None = Field(serialization_alias="ReadIOKiBytes", default=None)
    read_io_request_time: str | None = Field(serialization_alias="ReadIORequestTime", default=None)
    read_io_requests: int | None = Field(serialization_alias="ReadIORequests", default=None)
    write_hit_io_requests: int | None = Field(
        serialization_alias="WriteHitIORequests", default=None
    )
    write_io_kibytes: int | None = Field(serialization_alias="WriteIOKiBytes", default=None)
    write_io_request_time: str | None = Field(
        serialization_alias="WriteIORequestTime", default=None
    )
    write_io_requests: int | None = Field(serialization_alias="WriteIORequests", default=None)

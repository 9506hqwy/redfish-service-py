from __future__ import annotations  # PEP563 Forward References

from ..base import (
    RedfishModel,
)


class Iostatistics(RedfishModel):
    non_iorequest_time: str | None = None
    non_iorequests: str | None = None
    read_hit_iorequests: str | None = None
    read_ioki_bytes: str | None = None
    read_iorequest_time: str | None = None
    read_iorequests: str | None = None
    write_hit_iorequests: str | None = None
    write_ioki_bytes: str | None = None
    write_iorequest_time: str | None = None
    write_iorequests: str | None = None

from __future__ import annotations  # PEP563 Forward References

from pydantic import Field

from .base import RedfishModel


class IdRef(RedfishModel):
    odata_id: str | None = Field(alias="@odata.id", default=None)

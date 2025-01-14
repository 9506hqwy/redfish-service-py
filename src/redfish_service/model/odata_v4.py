from __future__ import annotations  # PEP563 Forward References

from pydantic import Field

from . import RedfishModel


class IdRef(RedfishModel):
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)

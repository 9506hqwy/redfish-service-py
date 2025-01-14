from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .resource import Condition, Health


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class ServiceConditions(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#ServiceConditions.v1_0_1.ServiceConditions"
    )
    actions: Actions | None = None
    conditions: list[Condition] | None = None
    description: str | None = None
    health_rollup: Health | None = None
    id: str
    name: str
    oem: dict[str, Any] | None = None

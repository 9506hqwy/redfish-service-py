from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class ConnectionMethod(RedfishResource):
    actions: Actions | None = None
    connection_method_type: str | None = None
    connection_method_variant: str | None = None
    description: str | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    tunneling_protocol: str | None = None


class Links(RedfishModel):
    aggregation_sources: list[IdRef] | None = None
    aggregation_sources_odata_count: int | None = Field(
        alias="AggregationSources@odata.count", default=None
    )
    oem: dict[str, Any] | None = None

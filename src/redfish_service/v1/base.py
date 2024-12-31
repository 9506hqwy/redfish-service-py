from typing import Any

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_pascal


class RedfishModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_pascal, populate_by_name=True)


class RedfishObject(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(alias="@odata.type")


class RedfishObjectId(RedfishModel):
    odata_id: str = Field(alias="@odata.id")


class RedfishResource(RedfishObject):
    id: str
    name: str


class RedfishResourceCollection(RedfishObject):
    description: str | None = Field(default=None)
    members: list[RedfishObjectId]
    members_count: int = Field(alias="Members@odata.count")
    members_next: str | None = Field(alias="Members@odata.nextLink", default=None)
    name: str
    oem: dict[str, Any] | None = None

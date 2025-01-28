from __future__ import annotations  # PEP563 Forward References

from pydantic import BaseModel, Field

from .model import RedfishModel


class OdataService(RedfishModel):
    odata_context: str = Field(serialization_alias="@odata.context")
    value: list[OdataServiceValue] = Field(serialization_alias="value")


class OdataServiceValue(BaseModel):
    name: str = Field(serialization_alias="name")
    kind: str = Field(serialization_alias="kind", default="Singleton")
    url: str = Field(serialization_alias="url")

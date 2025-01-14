from typing import Any

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_pascal


class RedfishModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_pascal, extra="forbid", populate_by_name=True, strict=True
    )

    extra_fields: dict[str, Any] = Field(exclude=True, default={})


class RedfishModelOnUpdate(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_pascal, extra="allow", populate_by_name=True, strict=True
    )

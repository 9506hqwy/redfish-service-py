from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_pascal


class RedfishModel(BaseModel):
    model_config = ConfigDict(alias_generator=to_pascal, extra="forbid", populate_by_name=True)

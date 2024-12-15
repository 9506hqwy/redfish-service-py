from pydantic import Field

from .base import RedfishModel, RedfishObjectId, RedfishResource
from .resource import Oem


class ServiceRootLinks(RedfishModel):
    oem: Oem | None = Field(default=None)
    sessions: RedfishObjectId


class ServiceRoot(RedfishResource):
    links: ServiceRootLinks
    uuid: str | None = Field(alias="UUID", default=None)
    vendor: str | None = None

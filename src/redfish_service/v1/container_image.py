from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from .base import (
    RedfishModel,
    RedfishResource,
)
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class ContainerImage(RedfishResource):
    actions: Actions | None = None
    create_time: str | None = None
    description: str | None = None
    links: Links | None = None
    oem: dict[str, Any] | None = None
    programmatic_id: str | None = None
    size_bytes: int | None = None
    status: Status | None = None
    type: ImageTypes | None = None
    version: str | None = None


class ImageTypes(StrEnum):
    DOCKER_V1 = "DockerV1"
    DOCKER_V2 = "DockerV2"
    OCI = "OCI"


class Links(RedfishModel):
    containers: list[IdRef] | None = None
    containers_odata_count: int | None = Field(alias="Containers@odata.count", default=None)
    oem: dict[str, Any] | None = None
    software_image: IdRef | None = None

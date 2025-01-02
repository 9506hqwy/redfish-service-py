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


class KeyService(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    nvme_of_key_policies: IdRef | None = Field(alias="NVMeoFKeyPolicies", default=None)
    nvme_of_secrets: IdRef | None = Field(alias="NVMeoFSecrets", default=None)
    oem: dict[str, Any] | None = None

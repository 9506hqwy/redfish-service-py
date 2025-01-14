from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class KeyService(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#KeyService.v1_0_1.KeyService"
    )
    actions: Actions | None = None
    description: str | None = None
    id: str
    nvme_of_key_policies: IdRef | None = Field(
        serialization_alias="NVMeoFKeyPolicies", default=None
    )
    nvme_of_secrets: IdRef | None = Field(serialization_alias="NVMeoFSecrets", default=None)
    name: str
    oem: dict[str, Any] | None = None

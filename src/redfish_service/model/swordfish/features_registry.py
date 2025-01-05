from __future__ import annotations  # PEP563 Forward References

from typing import Any

from pydantic import Field

from .. import RedfishModel
from ..odata_v4 import IdRef


class Actions(RedfishModel):
    oem: dict[str, Any] | None = None


class FeatureMap(RedfishModel):
    corresponding_profile_definition: str | None = None
    description: str | None = None
    feature_name: str | None = None
    resources: list[IdRef] | None = None
    resources_odata_count: int | None = Field(alias="Resources@odata.count", default=None)
    version: str | None = None


class FeaturesRegistry(RedfishModel):
    odata_context: str | None = Field(alias="@odata.context", default=None)
    odata_etag: str | None = Field(alias="@odata.etag", default=None)
    odata_id: str = Field(alias="@odata.id")
    odata_type: str = Field(
        alias="@odata.type", default="#FeaturesRegistry.v1_2_1.FeaturesRegistry"
    )
    actions: Actions | None = None
    description: str | None = None
    feature_mappings: list[FeatureMap]
    features: list[SupportedFeature] | None = None
    features_used: list[str]
    id: str
    language: str
    name: str
    oem_features_used: list[str] | None = Field(alias="OEMFeaturesUsed", default=None)
    oem: dict[str, Any] | None = None
    owning_entity: str
    registry_prefix: str
    registry_version: str


class SupportedFeature(RedfishModel):
    corresponding_profile_definition: str | None = None
    description: str | None = None
    feature_name: str | None = None
    version: str | None = None

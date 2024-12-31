from __future__ import annotations  # PEP563 Forward References

from typing import Any

from ..base import RedfishResource
from ..odata_v4 import IdRef


class Actions(RedfishResource):
    oem: OemActions | None = None


class FeatureMap(RedfishResource):
    corresponding_profile_definition: str
    description: str
    feature_name: str
    resources: list[IdRef] | None = None
    version: str


class FeaturesRegistry(RedfishResource):
    actions: Actions | None = None
    description: str | None = None
    feature_mappings: list[FeatureMap]
    features: list[SupportedFeature] | None = None
    features_used: list[str]
    language: str
    oemfeatures_used: list[str] | None = None
    oem: dict[str, Any] | None = None
    owning_entity: str
    registry_prefix: str
    registry_version: str


class OemActions(RedfishResource):
    pass


class SupportedFeature(RedfishResource):
    corresponding_profile_definition: str
    description: str
    feature_name: str
    version: str

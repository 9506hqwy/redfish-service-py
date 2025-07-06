from __future__ import annotations  # PEP563 Forward References

from enum import StrEnum
from typing import Any

from pydantic import Field

from . import RedfishModel
from .odata_v4 import IdRef
from .resource import Status


class Actions(RedfishModel):
    submit_job: SubmitJob | None = Field(
        serialization_alias="#JobDocument.SubmitJob", default=None
    )
    oem: dict[str, Any] | None = None


class DataType(StrEnum):
    BOOLEAN = "Boolean"
    NUMBER = "Number"
    STRING = "String"


class JobDocument(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str = Field(serialization_alias="@odata.id")
    odata_type: str = Field(
        serialization_alias="@odata.type", default="#JobDocument.v1_0_0.JobDocument"
    )
    actions: Actions | None = None
    creation_time: str | None = None
    description: str | None = None
    document_data: str | None = None
    document_data_hash: str | None = None
    document_data_uri: str | None = Field(serialization_alias="DocumentDataURI", default=None)
    document_type: str | None = None
    id: str
    links: Links | None = None
    name: str
    oem: dict[str, Any] | None = None
    parameter_metadata: list[ParameterMetadata] | None = None
    status: Status | None = None
    version: str | None = None


class JobDocumentOnCreate(RedfishModel):
    odata_context: str | None = Field(serialization_alias="@odata.context", default=None)
    odata_etag: str | None = Field(serialization_alias="@odata.etag", default=None)
    odata_id: str | None = Field(serialization_alias="@odata.id", default=None)
    odata_type: str | None = Field(
        serialization_alias="@odata.type", default="#JobDocument.v1_0_0.JobDocument"
    )
    actions: Actions | None = None
    creation_time: str | None = None
    description: str | None = None
    document_data: str | None = None
    document_data_hash: str | None = None
    document_data_uri: str | None = Field(serialization_alias="DocumentDataURI", default=None)
    document_type: str | None = None
    id: str | None = None
    links: Links | None = None
    name: str | None = None
    oem: dict[str, Any] | None = None
    parameter_metadata: list[ParameterMetadata] | None = None
    status: Status | None = None
    version: str | None = None


class Links(RedfishModel):
    supported_executors: list[IdRef] | None = None
    supported_executors_odata_count: int | None = Field(
        serialization_alias="SupportedExecutors@odata.count", default=None
    )


class ParameterMetadata(RedfishModel):
    allowable_numbers: list[str] | None = None
    allowable_pattern: str | None = None
    allowable_value_descriptions: list[str] | None = None
    allowable_values: list[str] | None = None
    data_type: DataType
    description: str | None = None
    maximum_value: float | None = None
    minimum_value: float | None = None
    name: str
    required: bool | None = None
    value_hint: str | None = None


class SubmitJob(RedfishModel):
    target: str | None = Field(serialization_alias="target", default=None)
    title: str | None = Field(serialization_alias="title", default=None)


class SubmitJobRequest(RedfishModel):
    hide_payload: bool | None = None
    job_creator: IdRef | None = None
    parameters: dict[str, Any]
    preferred_executors: list[IdRef]
    start_time: str | None = None

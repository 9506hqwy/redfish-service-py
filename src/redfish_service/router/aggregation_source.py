from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.aggregation_source import (
    AggregationSource,
    AggregationSourceOnUpdate,
    GenerateSshIdentityKeyPairRequest,
)
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(aggregation_source_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(AggregationSource, request)
    b: dict[str, Any] = {
        "aggregation_source_id": aggregation_source_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}",
    response_model_exclude_none=True,
)
async def get1(
    aggregation_source_id: str, request: Request, response: Response
) -> AggregationSource:
    s: Service = get_service(AggregationSource, request)
    b: dict[str, Any] = {
        "aggregation_source_id": aggregation_source_id,
        "request": request,
        "response": response,
    }
    m = cast(AggregationSource, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    aggregation_source_id: str,
    request: Request,
    response: Response,
    body: AggregationSourceOnUpdate,
) -> AggregationSource:
    s: Service = get_service(AggregationSource, request)
    b: dict[str, Any] = {
        "aggregation_source_id": aggregation_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(AggregationSource, s.patch(**b))


@router.post(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/Actions/AggregationSource.GenerateSSHIdentityKeyPair",
    response_model_exclude_none=True,
)
@authenticate
async def generate_ssh_identity_key_pair1(
    aggregation_source_id: str,
    request: Request,
    response: Response,
    body: GenerateSshIdentityKeyPairRequest,
) -> RedfishError:
    s: Service = get_service(AggregationSource, request)
    b: dict[str, Any] = {
        "aggregation_source_id": aggregation_source_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "GenerateSSHIdentityKeyPair",
    }
    return s.action(**b)

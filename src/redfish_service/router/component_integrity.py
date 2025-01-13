from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.component_integrity import (
    ComponentIntegrity,
    ComponentIntegrityOnUpdate,
    SpdmGetSignedMeasurementsRequest,
    TpmGetSignedMeasurementsRequest,
)
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service

router = APIRouter()


@router.get(
    "/redfish/v1/ComponentIntegrity/{component_integrity_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/ComponentIntegrity/{component_integrity_id}", response_model_exclude_none=True
)
async def get1(
    component_integrity_id: str, request: Request, response: Response
) -> ComponentIntegrity:
    s: Service = get_service(ComponentIntegrity, request)
    b: dict[str, Any] = {
        "component_integrity_id": component_integrity_id,
        "request": request,
        "response": response,
    }
    return cast(ComponentIntegrity, s.get(**b))


@router.patch(
    "/redfish/v1/ComponentIntegrity/{component_integrity_id}", response_model_exclude_none=True
)
@authenticate
async def patch1(
    component_integrity_id: str,
    request: Request,
    response: Response,
    body: ComponentIntegrityOnUpdate,
) -> ComponentIntegrity:
    s: Service = get_service(ComponentIntegrity, request)
    b: dict[str, Any] = {
        "component_integrity_id": component_integrity_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(ComponentIntegrity, s.patch(**b))


@router.post(
    "/redfish/v1/ComponentIntegrity/{component_integrity_id}/Actions/ComponentIntegrity.SPDMGetSignedMeasurements",
    response_model_exclude_none=True,
)
@authenticate
async def spdm_get_signed_measurements1(
    component_integrity_id: str,
    request: Request,
    response: Response,
    body: SpdmGetSignedMeasurementsRequest,
) -> RedfishError:
    s: Service = get_service(ComponentIntegrity, request)
    b: dict[str, Any] = {
        "component_integrity_id": component_integrity_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SPDMGetSignedMeasurements",
    }
    return s.action(**b)


@router.post(
    "/redfish/v1/ComponentIntegrity/{component_integrity_id}/Actions/ComponentIntegrity.TPMGetSignedMeasurements",
    response_model_exclude_none=True,
)
@authenticate
async def tpm_get_signed_measurements1(
    component_integrity_id: str,
    request: Request,
    response: Response,
    body: TpmGetSignedMeasurementsRequest,
) -> RedfishError:
    s: Service = get_service(ComponentIntegrity, request)
    b: dict[str, Any] = {
        "component_integrity_id": component_integrity_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "TPMGetSignedMeasurements",
    }
    return s.action(**b)

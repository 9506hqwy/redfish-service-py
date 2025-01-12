from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.nvme_firmware_image import NvmeFirmwareImage
from ...service import Service
from ...util import get_service

router = APIRouter()


@router.delete(
    "/redfish/v1/NVMeDomains/{domain_id}/AvailableFirmwareImages/{firmware_image_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    domain_id: str, firmware_image_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(NvmeFirmwareImage, request)
    b: dict[str, Any] = {
        "domain_id": domain_id,
        "firmware_image_id": firmware_image_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/NVMeDomains/{domain_id}/AvailableFirmwareImages/{firmware_image_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/NVMeDomains/{domain_id}/AvailableFirmwareImages/{firmware_image_id}",
    response_model_exclude_none=True,
)
async def get1(
    domain_id: str, firmware_image_id: str, request: Request, response: Response
) -> NvmeFirmwareImage:
    s: Service = get_service(NvmeFirmwareImage, request)
    b: dict[str, Any] = {
        "domain_id": domain_id,
        "firmware_image_id": firmware_image_id,
        "request": request,
        "response": response,
    }
    return cast(NvmeFirmwareImage, s.get(**b))

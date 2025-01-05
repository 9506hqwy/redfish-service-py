from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ...authenticate import authenticate
from ...model.swordfish.nvme_firmware_image import NvmeFirmwareImage
from ...service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/NVMeDomains/{domain_id}/AvailableFirmwareImages/{firmware_image_id}",
    response_model_exclude_none=True,
)
@authenticate
async def get1(
    domain_id: str, firmware_image_id: str, request: Request, response: Response
) -> NvmeFirmwareImage:
    s: Service = find_service(NvmeFirmwareImage)
    b: dict[str, Any] = {
        "domain_id": domain_id,
        "firmware_image_id": firmware_image_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(NvmeFirmwareImage, s.get(**b))

from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.leak_detector_collection import LeakDetectorCollection
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/LeakDetection/LeakDetectors",
    response_model_exclude_none=True,
)
@authenticate
async def get1(chassis_id: str, request: Request, response: Response) -> LeakDetectorCollection:
    s: Service = find_service(LeakDetectorCollection)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}

    response.headers["OData-Version"] = "4.0"

    return cast(LeakDetectorCollection, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/LeakDetection/LeakDetectors",
    response_model_exclude_none=True,
)
@authenticate
async def get2(
    cooling_unit_id: str, request: Request, response: Response
) -> LeakDetectorCollection:
    s: Service = find_service(LeakDetectorCollection)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LeakDetectorCollection, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/LeakDetection/LeakDetectors",
    response_model_exclude_none=True,
)
@authenticate
async def get3(
    cooling_unit_id: str, request: Request, response: Response
) -> LeakDetectorCollection:
    s: Service = find_service(LeakDetectorCollection)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LeakDetectorCollection, s.get(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/LeakDetection/LeakDetectors/",
    response_model_exclude_none=True,
)
@authenticate
async def get4(
    cooling_unit_id: str, request: Request, response: Response
) -> LeakDetectorCollection:
    s: Service = find_service(LeakDetectorCollection)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LeakDetectorCollection, s.get(**b))

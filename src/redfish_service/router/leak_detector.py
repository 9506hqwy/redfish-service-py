from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.leak_detector import LeakDetector, LeakDetectorOnUpdate
from ..service import Service, find_service

router = APIRouter()


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/LeakDetection/LeakDetectors/{leak_detector_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/LeakDetection/LeakDetectors/{leak_detector_id}",
    response_model_exclude_none=True,
)
async def get1(
    chassis_id: str, leak_detector_id: str, request: Request, response: Response
) -> LeakDetector:
    s: Service = find_service(LeakDetector)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "leak_detector_id": leak_detector_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LeakDetector, s.get(**b))


@router.patch(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/LeakDetection/LeakDetectors/{leak_detector_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    chassis_id: str,
    leak_detector_id: str,
    request: Request,
    response: Response,
    body: LeakDetectorOnUpdate,
) -> LeakDetector:
    s: Service = find_service(LeakDetector)
    b: dict[str, Any] = {
        "chassis_id": chassis_id,
        "leak_detector_id": leak_detector_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LeakDetector, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/LeakDetection/LeakDetectors/{leak_detector_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/LeakDetection/LeakDetectors/{leak_detector_id}",
    response_model_exclude_none=True,
)
async def get2(
    cooling_unit_id: str, leak_detector_id: str, request: Request, response: Response
) -> LeakDetector:
    s: Service = find_service(LeakDetector)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "leak_detector_id": leak_detector_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LeakDetector, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/LeakDetection/LeakDetectors/{leak_detector_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    cooling_unit_id: str,
    leak_detector_id: str,
    request: Request,
    response: Response,
    body: LeakDetectorOnUpdate,
) -> LeakDetector:
    s: Service = find_service(LeakDetector)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "leak_detector_id": leak_detector_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LeakDetector, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/LeakDetection/LeakDetectors/{leak_detector_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/LeakDetection/LeakDetectors/{leak_detector_id}",
    response_model_exclude_none=True,
)
async def get3(
    cooling_unit_id: str, leak_detector_id: str, request: Request, response: Response
) -> LeakDetector:
    s: Service = find_service(LeakDetector)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "leak_detector_id": leak_detector_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LeakDetector, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/LeakDetection/LeakDetectors/{leak_detector_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    cooling_unit_id: str,
    leak_detector_id: str,
    request: Request,
    response: Response,
    body: LeakDetectorOnUpdate,
) -> LeakDetector:
    s: Service = find_service(LeakDetector)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "leak_detector_id": leak_detector_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LeakDetector, s.patch(**b))


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/LeakDetection/LeakDetectors/{leak_detector_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/LeakDetection/LeakDetectors/{leak_detector_id}",
    response_model_exclude_none=True,
)
async def get4(
    cooling_unit_id: str, leak_detector_id: str, request: Request, response: Response
) -> LeakDetector:
    s: Service = find_service(LeakDetector)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "leak_detector_id": leak_detector_id,
        "request": request,
        "response": response,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LeakDetector, s.get(**b))


@router.patch(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/LeakDetection/LeakDetectors/{leak_detector_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    cooling_unit_id: str,
    leak_detector_id: str,
    request: Request,
    response: Response,
    body: LeakDetectorOnUpdate,
) -> LeakDetector:
    s: Service = find_service(LeakDetector)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "leak_detector_id": leak_detector_id,
        "request": request,
        "response": response,
        "body": body,
    }

    response.headers["OData-Version"] = "4.0"

    return cast(LeakDetector, s.patch(**b))

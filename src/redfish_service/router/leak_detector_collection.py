from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..model.leak_detector_collection import LeakDetectorCollection
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get("/redfish/v1/Chassis/{chassis_id}/LeakDetectors", response_model_exclude_none=True)
@router.head("/redfish/v1/Chassis/{chassis_id}/LeakDetectors", response_model_exclude_none=True)
async def get1(chassis_id: str, request: Request, response: Response) -> LeakDetectorCollection:
    s: Service = get_service(LeakDetectorCollection, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}
    m = cast(LeakDetectorCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/LeakDetection/LeakDetectors",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Chassis/{chassis_id}/ThermalSubsystem/LeakDetection/LeakDetectors",
    response_model_exclude_none=True,
)
async def get2(chassis_id: str, request: Request, response: Response) -> LeakDetectorCollection:
    s: Service = get_service(LeakDetectorCollection, request)
    b: dict[str, Any] = {"chassis_id": chassis_id, "request": request, "response": response}
    m = cast(LeakDetectorCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/LeakDetection/LeakDetectors",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/LeakDetection/LeakDetectors",
    response_model_exclude_none=True,
)
async def get3(
    cooling_unit_id: str, request: Request, response: Response
) -> LeakDetectorCollection:
    s: Service = get_service(LeakDetectorCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    m = cast(LeakDetectorCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/LeakDetection/LeakDetectors",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/LeakDetection/LeakDetectors",
    response_model_exclude_none=True,
)
async def get4(
    cooling_unit_id: str, request: Request, response: Response
) -> LeakDetectorCollection:
    s: Service = get_service(LeakDetectorCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    m = cast(LeakDetectorCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/LeakDetection/LeakDetectors/",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/LeakDetection/LeakDetectors/",
    response_model_exclude_none=True,
)
async def get5(
    cooling_unit_id: str, request: Request, response: Response
) -> LeakDetectorCollection:
    s: Service = get_service(LeakDetectorCollection, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    m = cast(LeakDetectorCollection, s.get(**b))
    set_link_header(m, response)
    return m

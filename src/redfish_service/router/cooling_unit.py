from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.cooling_unit import CoolingUnit, CoolingUnitOnUpdate, SetModeRequest
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}", response_model_exclude_none=True
)
async def get1(cooling_unit_id: str, request: Request, response: Response) -> CoolingUnit:
    s: Service = get_service(CoolingUnit, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    m = cast(CoolingUnit, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}", response_model_exclude_none=True
)
@authenticate
async def patch1(
    cooling_unit_id: str, request: Request, response: Response, body: CoolingUnitOnUpdate
) -> CoolingUnit:
    s: Service = get_service(CoolingUnit, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CoolingUnit, s.patch(**b))


@router.post(
    "/redfish/v1/ThermalEquipment/CDUs/{cooling_unit_id}/Actions/CoolingUnit.SetMode",
    response_model_exclude_none=True,
)
@authenticate
async def set_mode1(
    cooling_unit_id: str, request: Request, response: Response, body: SetModeRequest
) -> RedfishError:
    s: Service = get_service(CoolingUnit, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetMode",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}",
    response_model_exclude_none=True,
)
async def get2(cooling_unit_id: str, request: Request, response: Response) -> CoolingUnit:
    s: Service = get_service(CoolingUnit, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    m = cast(CoolingUnit, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    cooling_unit_id: str, request: Request, response: Response, body: CoolingUnitOnUpdate
) -> CoolingUnit:
    s: Service = get_service(CoolingUnit, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CoolingUnit, s.patch(**b))


@router.post(
    "/redfish/v1/ThermalEquipment/ImmersionUnits/{cooling_unit_id}/Actions/CoolingUnit.SetMode",
    response_model_exclude_none=True,
)
@authenticate
async def set_mode2(
    cooling_unit_id: str, request: Request, response: Response, body: SetModeRequest
) -> RedfishError:
    s: Service = get_service(CoolingUnit, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetMode",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}",
    response_model_exclude_none=True,
)
async def get3(cooling_unit_id: str, request: Request, response: Response) -> CoolingUnit:
    s: Service = get_service(CoolingUnit, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    m = cast(CoolingUnit, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    cooling_unit_id: str, request: Request, response: Response, body: CoolingUnitOnUpdate
) -> CoolingUnit:
    s: Service = get_service(CoolingUnit, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CoolingUnit, s.patch(**b))


@router.post(
    "/redfish/v1/ThermalEquipment/HeatExchangers/{cooling_unit_id}/Actions/CoolingUnit.SetMode",
    response_model_exclude_none=True,
)
@authenticate
async def set_mode3(
    cooling_unit_id: str, request: Request, response: Response, body: SetModeRequest
) -> RedfishError:
    s: Service = get_service(CoolingUnit, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetMode",
    }
    return s.action(**b)


@router.get(
    "/redfish/v1/ThermalEquipment/RPUs/{cooling_unit_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/ThermalEquipment/RPUs/{cooling_unit_id}", response_model_exclude_none=True
)
async def get4(cooling_unit_id: str, request: Request, response: Response) -> CoolingUnit:
    s: Service = get_service(CoolingUnit, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
    }
    m = cast(CoolingUnit, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/ThermalEquipment/RPUs/{cooling_unit_id}", response_model_exclude_none=True
)
@authenticate
async def patch4(
    cooling_unit_id: str, request: Request, response: Response, body: CoolingUnitOnUpdate
) -> CoolingUnit:
    s: Service = get_service(CoolingUnit, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(CoolingUnit, s.patch(**b))


@router.post(
    "/redfish/v1/ThermalEquipment/RPUs/{cooling_unit_id}/Actions/CoolingUnit.SetMode",
    response_model_exclude_none=True,
)
@authenticate
async def set_mode4(
    cooling_unit_id: str, request: Request, response: Response, body: SetModeRequest
) -> RedfishError:
    s: Service = get_service(CoolingUnit, request)
    b: dict[str, Any] = {
        "cooling_unit_id": cooling_unit_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "SetMode",
    }
    return s.action(**b)

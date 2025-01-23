from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.outlet_group import OutletGroup, OutletGroupOnCreate
from ..model.outlet_group_collection import OutletGroupCollection
from ..service import Service, ServiceCollection
from ..util import get_service, get_service_collection, set_link_header

router = APIRouter()


@router.get(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/OutletGroups",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/OutletGroups",
    response_model_exclude_none=True,
)
async def get1(
    power_distribution_id: str, request: Request, response: Response
) -> OutletGroupCollection:
    s: Service = get_service(OutletGroupCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    m = cast(OutletGroupCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/OutletGroups",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/OutletGroups/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post1(
    power_distribution_id: str, request: Request, response: Response, body: OutletGroupOnCreate
) -> OutletGroup:
    s: ServiceCollection = get_service_collection(OutletGroupCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(OutletGroup, s.post(**b))


@router.get(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/OutletGroups",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/OutletGroups",
    response_model_exclude_none=True,
)
async def get2(
    power_distribution_id: str, request: Request, response: Response
) -> OutletGroupCollection:
    s: Service = get_service(OutletGroupCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    m = cast(OutletGroupCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/OutletGroups",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/OutletGroups/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post2(
    power_distribution_id: str, request: Request, response: Response, body: OutletGroupOnCreate
) -> OutletGroup:
    s: ServiceCollection = get_service_collection(OutletGroupCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(OutletGroup, s.post(**b))


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/OutletGroups",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/OutletGroups",
    response_model_exclude_none=True,
)
async def get3(
    power_distribution_id: str, request: Request, response: Response
) -> OutletGroupCollection:
    s: Service = get_service(OutletGroupCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    m = cast(OutletGroupCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/OutletGroups",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/OutletGroups/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post3(
    power_distribution_id: str, request: Request, response: Response, body: OutletGroupOnCreate
) -> OutletGroup:
    s: ServiceCollection = get_service_collection(OutletGroupCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(OutletGroup, s.post(**b))


@router.get(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/OutletGroups",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/OutletGroups",
    response_model_exclude_none=True,
)
async def get4(
    power_distribution_id: str, request: Request, response: Response
) -> OutletGroupCollection:
    s: Service = get_service(OutletGroupCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
    }
    m = cast(OutletGroupCollection, s.get(**b))
    set_link_header(m, response)
    return m


@router.post(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/OutletGroups",
    response_model_exclude_none=True,
)
@router.post(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/OutletGroups/Members",
    response_model_exclude_none=True,
)
@authenticate
async def post4(
    power_distribution_id: str, request: Request, response: Response, body: OutletGroupOnCreate
) -> OutletGroup:
    s: ServiceCollection = get_service_collection(OutletGroupCollection, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(OutletGroup, s.post(**b))

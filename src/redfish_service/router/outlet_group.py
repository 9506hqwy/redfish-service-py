from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.outlet_group import OutletGroup, OutletGroupOnUpdate, PowerControlRequest
from ..model.redfish_error import RedfishError
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/OutletGroups/{outlet_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete1(
    power_distribution_id: str, outlet_group_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(OutletGroup, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "outlet_group_id": outlet_group_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/OutletGroups/{outlet_group_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/OutletGroups/{outlet_group_id}",
    response_model_exclude_none=True,
)
async def get1(
    power_distribution_id: str, outlet_group_id: str, request: Request, response: Response
) -> OutletGroup:
    s: Service = get_service(OutletGroup, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "outlet_group_id": outlet_group_id,
        "request": request,
        "response": response,
    }
    m = cast(OutletGroup, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/OutletGroups/{outlet_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch1(
    power_distribution_id: str,
    outlet_group_id: str,
    request: Request,
    response: Response,
    body: OutletGroupOnUpdate,
) -> OutletGroup:
    s: Service = get_service(OutletGroup, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "outlet_group_id": outlet_group_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(OutletGroup, s.patch(**b))


@router.post(
    "/redfish/v1/PowerEquipment/RackPDUs/{power_distribution_id}/OutletGroups/{outlet_group_id}/Actions/OutletGroup.PowerControl",
    response_model_exclude_none=True,
)
@authenticate
async def power_control1(
    power_distribution_id: str,
    outlet_group_id: str,
    request: Request,
    response: Response,
    body: PowerControlRequest,
) -> RedfishError:
    s: Service = get_service(OutletGroup, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "outlet_group_id": outlet_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "PowerControl",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/OutletGroups/{outlet_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete2(
    power_distribution_id: str, outlet_group_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(OutletGroup, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "outlet_group_id": outlet_group_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/OutletGroups/{outlet_group_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/OutletGroups/{outlet_group_id}",
    response_model_exclude_none=True,
)
async def get2(
    power_distribution_id: str, outlet_group_id: str, request: Request, response: Response
) -> OutletGroup:
    s: Service = get_service(OutletGroup, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "outlet_group_id": outlet_group_id,
        "request": request,
        "response": response,
    }
    m = cast(OutletGroup, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/OutletGroups/{outlet_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch2(
    power_distribution_id: str,
    outlet_group_id: str,
    request: Request,
    response: Response,
    body: OutletGroupOnUpdate,
) -> OutletGroup:
    s: Service = get_service(OutletGroup, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "outlet_group_id": outlet_group_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(OutletGroup, s.patch(**b))


@router.post(
    "/redfish/v1/PowerEquipment/TransferSwitches/{power_distribution_id}/OutletGroups/{outlet_group_id}/Actions/OutletGroup.PowerControl",
    response_model_exclude_none=True,
)
@authenticate
async def power_control2(
    power_distribution_id: str,
    outlet_group_id: str,
    request: Request,
    response: Response,
    body: PowerControlRequest,
) -> RedfishError:
    s: Service = get_service(OutletGroup, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "outlet_group_id": outlet_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "PowerControl",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/OutletGroups/{outlet_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete3(
    power_distribution_id: str, outlet_group_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(OutletGroup, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "outlet_group_id": outlet_group_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/OutletGroups/{outlet_group_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/OutletGroups/{outlet_group_id}",
    response_model_exclude_none=True,
)
async def get3(
    power_distribution_id: str, outlet_group_id: str, request: Request, response: Response
) -> OutletGroup:
    s: Service = get_service(OutletGroup, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "outlet_group_id": outlet_group_id,
        "request": request,
        "response": response,
    }
    m = cast(OutletGroup, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/OutletGroups/{outlet_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch3(
    power_distribution_id: str,
    outlet_group_id: str,
    request: Request,
    response: Response,
    body: OutletGroupOnUpdate,
) -> OutletGroup:
    s: Service = get_service(OutletGroup, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "outlet_group_id": outlet_group_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(OutletGroup, s.patch(**b))


@router.post(
    "/redfish/v1/PowerEquipment/PowerShelves/{power_distribution_id}/OutletGroups/{outlet_group_id}/Actions/OutletGroup.PowerControl",
    response_model_exclude_none=True,
)
@authenticate
async def power_control3(
    power_distribution_id: str,
    outlet_group_id: str,
    request: Request,
    response: Response,
    body: PowerControlRequest,
) -> RedfishError:
    s: Service = get_service(OutletGroup, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "outlet_group_id": outlet_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "PowerControl",
    }
    return s.action(**b)


@router.delete(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/OutletGroups/{outlet_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete4(
    power_distribution_id: str, outlet_group_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(OutletGroup, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "outlet_group_id": outlet_group_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/OutletGroups/{outlet_group_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/OutletGroups/{outlet_group_id}",
    response_model_exclude_none=True,
)
async def get4(
    power_distribution_id: str, outlet_group_id: str, request: Request, response: Response
) -> OutletGroup:
    s: Service = get_service(OutletGroup, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "outlet_group_id": outlet_group_id,
        "request": request,
        "response": response,
    }
    m = cast(OutletGroup, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/OutletGroups/{outlet_group_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    power_distribution_id: str,
    outlet_group_id: str,
    request: Request,
    response: Response,
    body: OutletGroupOnUpdate,
) -> OutletGroup:
    s: Service = get_service(OutletGroup, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "outlet_group_id": outlet_group_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(OutletGroup, s.patch(**b))


@router.post(
    "/redfish/v1/PowerEquipment/ElectricalBuses/{power_distribution_id}/OutletGroups/{outlet_group_id}/Actions/OutletGroup.PowerControl",
    response_model_exclude_none=True,
)
@authenticate
async def power_control4(
    power_distribution_id: str,
    outlet_group_id: str,
    request: Request,
    response: Response,
    body: PowerControlRequest,
) -> RedfishError:
    s: Service = get_service(OutletGroup, request)
    b: dict[str, Any] = {
        "power_distribution_id": power_distribution_id,
        "outlet_group_id": outlet_group_id,
        "request": request,
        "response": response,
        "body": body,
        "action": "PowerControl",
    }
    return s.action(**b)

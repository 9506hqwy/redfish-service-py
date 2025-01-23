from typing import Any, cast

from fastapi import APIRouter, Request, Response

from ..authenticate import authenticate
from ..model.key import Key, KeyOnUpdate
from ..service import Service
from ..util import get_service, set_link_header

router = APIRouter()


@router.delete("/redfish/v1/KeyService/NVMeoFSecrets/{key_id}", response_model_exclude_none=True)
@authenticate
async def delete1(key_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {"key_id": key_id, "request": request, "response": response}
    return s.delete(**b)


@router.get("/redfish/v1/KeyService/NVMeoFSecrets/{key_id}", response_model_exclude_none=True)
@router.head("/redfish/v1/KeyService/NVMeoFSecrets/{key_id}", response_model_exclude_none=True)
async def get1(key_id: str, request: Request, response: Response) -> Key:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {"key_id": key_id, "request": request, "response": response}
    m = cast(Key, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch("/redfish/v1/KeyService/NVMeoFSecrets/{key_id}", response_model_exclude_none=True)
@authenticate
async def patch1(key_id: str, request: Request, response: Response, body: KeyOnUpdate) -> Key:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {"key_id": key_id, "request": request, "response": response, "body": body}
    return cast(Key, s.patch(**b))


@router.delete(
    "/redfish/v1/UpdateService/RemoteServerSSHKeys/{key_id}", response_model_exclude_none=True
)
@authenticate
async def delete2(key_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {"key_id": key_id, "request": request, "response": response}
    return s.delete(**b)


@router.get(
    "/redfish/v1/UpdateService/RemoteServerSSHKeys/{key_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/UpdateService/RemoteServerSSHKeys/{key_id}", response_model_exclude_none=True
)
async def get2(key_id: str, request: Request, response: Response) -> Key:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {"key_id": key_id, "request": request, "response": response}
    m = cast(Key, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/UpdateService/RemoteServerSSHKeys/{key_id}", response_model_exclude_none=True
)
@authenticate
async def patch2(key_id: str, request: Request, response: Response, body: KeyOnUpdate) -> Key:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {"key_id": key_id, "request": request, "response": response, "body": body}
    return cast(Key, s.patch(**b))


@router.delete(
    "/redfish/v1/UpdateService/PublicIdentitySSHKey/{key_id}", response_model_exclude_none=True
)
@authenticate
async def delete3(key_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {"key_id": key_id, "request": request, "response": response}
    return s.delete(**b)


@router.get(
    "/redfish/v1/UpdateService/PublicIdentitySSHKey/{key_id}", response_model_exclude_none=True
)
@router.head(
    "/redfish/v1/UpdateService/PublicIdentitySSHKey/{key_id}", response_model_exclude_none=True
)
async def get3(key_id: str, request: Request, response: Response) -> Key:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {"key_id": key_id, "request": request, "response": response}
    m = cast(Key, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/UpdateService/PublicIdentitySSHKey/{key_id}", response_model_exclude_none=True
)
@authenticate
async def patch3(key_id: str, request: Request, response: Response, body: KeyOnUpdate) -> Key:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {"key_id": key_id, "request": request, "response": response, "body": body}
    return cast(Key, s.patch(**b))


@router.delete(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Keys/{key_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete4(
    manager_account_id: str, key_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {
        "manager_account_id": manager_account_id,
        "key_id": key_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Keys/{key_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Keys/{key_id}",
    response_model_exclude_none=True,
)
async def get4(manager_account_id: str, key_id: str, request: Request, response: Response) -> Key:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {
        "manager_account_id": manager_account_id,
        "key_id": key_id,
        "request": request,
        "response": response,
    }
    m = cast(Key, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/AccountService/Accounts/{manager_account_id}/Keys/{key_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch4(
    manager_account_id: str, key_id: str, request: Request, response: Response, body: KeyOnUpdate
) -> Key:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {
        "manager_account_id": manager_account_id,
        "key_id": key_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Key, s.patch(**b))


@router.delete(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Keys/{key_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete5(
    manager_id: str, manager_account_id: str, key_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "manager_account_id": manager_account_id,
        "key_id": key_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Keys/{key_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Keys/{key_id}",
    response_model_exclude_none=True,
)
async def get5(
    manager_id: str, manager_account_id: str, key_id: str, request: Request, response: Response
) -> Key:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "manager_account_id": manager_account_id,
        "key_id": key_id,
        "request": request,
        "response": response,
    }
    m = cast(Key, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/Managers/{manager_id}/RemoteAccountService/Accounts/{manager_account_id}/Keys/{key_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch5(
    manager_id: str,
    manager_account_id: str,
    key_id: str,
    request: Request,
    response: Response,
    body: KeyOnUpdate,
) -> Key:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {
        "manager_id": manager_id,
        "manager_account_id": manager_account_id,
        "key_id": key_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Key, s.patch(**b))


@router.delete(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/TrustedPublicHostKeys/{key_id}",
    response_model_exclude_none=True,
)
@authenticate
async def delete6(
    aggregation_source_id: str, key_id: str, request: Request, response: Response
) -> None:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {
        "aggregation_source_id": aggregation_source_id,
        "key_id": key_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/TrustedPublicHostKeys/{key_id}",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/TrustedPublicHostKeys/{key_id}",
    response_model_exclude_none=True,
)
async def get6(
    aggregation_source_id: str, key_id: str, request: Request, response: Response
) -> Key:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {
        "aggregation_source_id": aggregation_source_id,
        "key_id": key_id,
        "request": request,
        "response": response,
    }
    m = cast(Key, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/TrustedPublicHostKeys/{key_id}",
    response_model_exclude_none=True,
)
@authenticate
async def patch6(
    aggregation_source_id: str,
    key_id: str,
    request: Request,
    response: Response,
    body: KeyOnUpdate,
) -> Key:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {
        "aggregation_source_id": aggregation_source_id,
        "key_id": key_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Key, s.patch(**b))


@router.delete(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/PresentedPublicHostKey",
    response_model_exclude_none=True,
)
@authenticate
async def delete7(aggregation_source_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {
        "aggregation_source_id": aggregation_source_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/PresentedPublicHostKey",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/PresentedPublicHostKey",
    response_model_exclude_none=True,
)
async def get7(aggregation_source_id: str, request: Request, response: Response) -> Key:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {
        "aggregation_source_id": aggregation_source_id,
        "request": request,
        "response": response,
    }
    m = cast(Key, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/PresentedPublicHostKey",
    response_model_exclude_none=True,
)
@authenticate
async def patch7(
    aggregation_source_id: str, request: Request, response: Response, body: KeyOnUpdate
) -> Key:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {
        "aggregation_source_id": aggregation_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Key, s.patch(**b))


@router.delete(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/PublicIdentityKey",
    response_model_exclude_none=True,
)
@authenticate
async def delete8(aggregation_source_id: str, request: Request, response: Response) -> None:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {
        "aggregation_source_id": aggregation_source_id,
        "request": request,
        "response": response,
    }
    return s.delete(**b)


@router.get(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/PublicIdentityKey",
    response_model_exclude_none=True,
)
@router.head(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/PublicIdentityKey",
    response_model_exclude_none=True,
)
async def get8(aggregation_source_id: str, request: Request, response: Response) -> Key:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {
        "aggregation_source_id": aggregation_source_id,
        "request": request,
        "response": response,
    }
    m = cast(Key, s.get(**b))
    set_link_header(m, response)
    return m


@router.patch(
    "/redfish/v1/AggregationService/AggregationSources/{aggregation_source_id}/PublicIdentityKey",
    response_model_exclude_none=True,
)
@authenticate
async def patch8(
    aggregation_source_id: str, request: Request, response: Response, body: KeyOnUpdate
) -> Key:
    s: Service = get_service(Key, request)
    b: dict[str, Any] = {
        "aggregation_source_id": aggregation_source_id,
        "request": request,
        "response": response,
        "body": body,
    }
    return cast(Key, s.patch(**b))

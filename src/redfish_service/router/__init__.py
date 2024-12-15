from functools import wraps
from inspect import Parameter, Signature, signature
from typing import Any, Callable

from fastapi import Depends, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from ..exception import ResourceAtUriUnauthorizedError

PATH_SERVICE_ROOT = "/redfish/v1"
PATH_SESSION_COLLECTION = "/redfish/v1/SessionService/Sessions"

basic_auth = HTTPBasic()


def check_basic_auth(username: str, password: str) -> bool:
    # TODO: account management
    return username == "admin" and password == "admin"  # noqa: S105


def authenticate(f: Callable) -> Callable:
    @wraps(f)
    async def wrapper(*args: list[Any], **kwds: dict[str, Any]) -> Any:
        req: Request = kwds.pop("req")  # type: ignore
        auth: HTTPBasicCredentials = kwds.pop("auth")  # type: ignore
        if not check_basic_auth(auth.username, auth.password):
            uri = req.url.path
            raise ResourceAtUriUnauthorizedError(uri, "Invalid username or password")

        # TODO: session management
        return await f(*args, **kwds)

    req = Parameter(
        "req",
        Parameter.POSITIONAL_OR_KEYWORD,
        annotation=Request,
    )

    auth = Parameter(
        "auth",
        Parameter.POSITIONAL_OR_KEYWORD,
        default=Depends(basic_auth),
        annotation=HTTPBasicCredentials,
    )

    sig = signature(wrapper)
    wrapper.__signature__ = Signature(  # type: ignore
        parameters=[*sig.parameters.values(), req, auth], return_annotation=sig.return_annotation
    )

    return wrapper

from functools import wraps
from inspect import Parameter, Signature, signature
from typing import Any, Callable, cast

from fastapi import Depends, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel

from .exception import ResourceAtUriUnauthorizedError
from .model.manager_account import ManagerAccount
from .model.session import Session
from .repository import instances


class AuthTokenCredentials(BaseModel):
    token: str


class HttpBasicOrAuthToken(HTTPBasic):
    async def __call__(  # type: ignore
        self, request: Request
    ) -> HTTPBasicCredentials | AuthTokenCredentials | None:
        token = request.headers.get("X-Auth-Token")
        if token:
            return AuthTokenCredentials(token=token)
        else:
            return await super().__call__(request)


basic_or_token_auth = HttpBasicOrAuthToken()


def check_token_auth(token: str) -> bool:
    for session in instances.enum_by_type(Session):
        if session.extra_fields["token"] == token:
            return True

    return False


def check_basic_auth(username: str, password: str) -> bool:
    for account in instances.enum_by_type(ManagerAccount):
        if account.name == username and account.extra_fields["password"] == password:
            return True

    return False


def authenticate(f: Callable) -> Callable:
    @wraps(f)
    async def wrapper(*args: list[Any], **kwds: dict[str, Any]) -> Any:
        req = cast(Request, kwds.get("request"))
        auth = cast(Any, kwds.pop("auth"))

        if isinstance(auth, HTTPBasicCredentials) and not check_basic_auth(
            auth.username, auth.password
        ):
            uri = req.url.path
            raise ResourceAtUriUnauthorizedError(uri, "Invalid username or password")

        if isinstance(auth, AuthTokenCredentials) and not check_token_auth(auth.token):
            uri = req.url.path
            raise ResourceAtUriUnauthorizedError(uri, "Invalid X-Auth-Token")

        # TODO: session management
        return await f(*args, **kwds)

    auth = Parameter(
        "auth",
        Parameter.POSITIONAL_OR_KEYWORD,
        default=Depends(basic_or_token_auth),
        annotation=HTTPBasicCredentials | AuthTokenCredentials,
    )

    sig = signature(wrapper)
    wrapper.__signature__ = Signature(  # type: ignore
        parameters=[*sig.parameters.values(), auth], return_annotation=sig.return_annotation
    )

    return wrapper

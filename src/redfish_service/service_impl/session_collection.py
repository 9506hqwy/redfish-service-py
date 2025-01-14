import uuid
from http import HTTPStatus
from typing import Any, cast

from fastapi import Request, Response

from ..authenticate import check_basic_auth
from ..exception import ResourceAtUriUnauthorizedError, ResourceNotFoundError
from ..model.odata_v4 import IdRef
from ..model.session import Session, SessionOnCreate
from ..model.session_collection import SessionCollection
from ..repository import instances
from ..service import ServiceCollection


class SessionCollectionService(ServiceCollection[SessionCollection, Session]):
    def respond(self, ty: type) -> bool:
        return ty == SessionCollection

    def get(self, **kwargs: dict[str, Any]) -> SessionCollection:
        i = instances.find_by_type(SessionCollection)
        if i is None:
            raise ResourceNotFoundError("SessionCollection", "SessionCollection")

        i.members = [IdRef(odata_id=s.odata_id) for s in instances.enum_by_type(Session)]
        i.members_odata_count = len(i.members)

        req: Request = cast(Request, kwargs["request"])
        i.odata_id = req.url.path

        return i

    def post(self, **kwargs: dict[str, Any]) -> Session:
        body: SessionOnCreate = cast(SessionOnCreate, kwargs.get("body"))
        req: Request = cast(Request, kwargs["request"])
        res: Response = cast(Response, kwargs["response"])

        if body.user_name is None or body.password is None:
            uri = req.url.path
            raise ResourceAtUriUnauthorizedError(uri, "Invalid username or password")

        if not check_basic_auth(body.user_name, body.password):
            uri = req.url.path
            raise ResourceAtUriUnauthorizedError(uri, "Invalid username or password")

        id = uuid.uuid4()
        token = uuid.uuid4()

        session = Session(
            odata_id=f"{req.url.path}/{id}",
            id=str(id),
            name=str(id),
            user_name=body.user_name,
        )
        session.extra_fields["token"] = str(token)
        instances.add(session)

        res.headers["Location"] = session.odata_id
        res.headers["X-Auth-Token"] = cast(str, session.extra_fields["token"])
        res.status_code = HTTPStatus.CREATED

        return session

from http import HTTPStatus

from fastapi.testclient import TestClient

from redfish_service.server import app

client = TestClient(app)


def test_root() -> None:
    response = client.get("/redfish")
    assert response.status_code == HTTPStatus.OK


def test_odata() -> None:
    response = client.get("/redfish/v1/odata")
    assert response.status_code == HTTPStatus.OK


def test_metadata() -> None:
    response = client.get("/redfish/v1/$metadata")
    assert response.status_code == HTTPStatus.OK


def test_404() -> None:
    response = client.get("/redfish/v2")
    assert response.status_code == HTTPStatus.NOT_FOUND

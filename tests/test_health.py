from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint_reports_process_health() -> None:
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "indian-law-assistant"}

def test_root_has_legal_information_disclaimer() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "not legal advice" in response.json()["disclaimer"]

def test_openapi_is_available() -> None:
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert "/api/v1/health" in response.json()["paths"]

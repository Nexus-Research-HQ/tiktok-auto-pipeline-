from fastapi.testclient import TestClient
from api_server import app, API_KEY

client = TestClient(app)
headers = {"X-API-Key": API_KEY}

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200

def test_register_and_workflow():
    reg_response = client.post("/register?username=test_user_ci&country=Nigeria", headers=headers)
    assert reg_response.status_code == 200

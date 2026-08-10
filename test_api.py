from fastapi.testclient import TestClient
from api_server import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"

def test_register_and_workflow():
    # Test user registration
    reg_response = client.post("/register", json={"username": "test_user_ci", "country": "Nigeria"})
    assert reg_response.status_code == 200
    assert reg_response.json()["username"] == "test_user_ci"
    assert reg_response.json()["balance"] == 20.0

    # Test video view logging
    view_response = client.post("/view?username=test_user_ci")
    assert view_response.status_code == 200
    assert view_response.json()["new_balance"] == 30.0

    # Test withdrawal
    withdraw_response = client.post("/withdraw", json={
        "username": "test_user_ci",
        "method": "bank_naira",
        "destination": "Test Bank - 1234567890"
    })
    assert withdraw_response.status_code == 200
    assert withdraw_response.json()["status"] == "success"

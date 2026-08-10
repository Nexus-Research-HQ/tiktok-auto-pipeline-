import unittest
from fastapi.testclient import TestClient
from api_server import app

client = TestClient(app)

class TestAPIEndpoints(unittest.TestCase):
    def test_root_endpoint(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "online")

    def test_register_and_workflow(self):
        # Test user registration
        reg_response = client.post("/register", json={"username": "test_user_ci", "country": "Nigeria"})
        self.assertEqual(reg_response.status_code, 200)
        self.assertEqual(reg_response.json()["username"], "test_user_ci")
        self.assertEqual(reg_response.json()["balance"], 20.0)

        # Test video view logging
        view_response = client.post("/view?username=test_user_ci")
        self.assertEqual(view_response.status_code, 200)
        self.assertEqual(view_response.json()["new_balance"], 30.0)

        # Test withdrawal
        withdraw_response = client.post("/withdraw", json={
            "username": "test_user_ci",
            "method": "bank_naira",
            "destination": "Test Bank - 1234567890"
        })
        self.assertEqual(withdraw_response.status_code, 200)
        self.assertEqual(withdraw_response.json()["status"], "success")

if __name__ == "__main__":
    unittest.main()

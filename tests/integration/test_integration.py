from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_integration():
    # Simulate a more complex scenario 
    response = client.get("/add/20/30")
    assert response.status_code == 200
    assert response.json() == {"result": 50}
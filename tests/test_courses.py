from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_health():
    assert client.get("/health").json() == {"status": "ok"}

def test_list_courses():
    r = client.get("/courses/")
    assert r.status_code == 200

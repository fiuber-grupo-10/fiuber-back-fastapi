from fastapi.testclient import TestClient
from app.main import app, get_db
from app.database.db import create_session_from_url

""" Fake DB to test stuff (should add mock) """


def override_get_db():
    db_session = create_session_from_url('postgresql:///./test.db')()
    try:
        yield db_session
    finally:
        db_session.close()
    pass


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_read_greeting():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello World"

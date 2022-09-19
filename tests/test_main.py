# by @tomyrd (https://github.com/tomyrd/heroku-docker-demo/)

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_greeting():
    response = client.get("/greeting/Tomy")
    assert response.status_code == 200
    assert response.json() == "Hola Tomy! Te quiero mucho <3"


def test_read_no_vowels():
    response = client.get("/no_vowels/murcielago")
    assert response.status_code == 200
    assert response.json() == "mrclg"

    response = client.get("/no_vowels/hola")
    assert response.status_code == 200
    assert response.json() == "hl"

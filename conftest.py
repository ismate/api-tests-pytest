import random
import requests
import pytest


@pytest.fixture(scope="session")
def base_url():
    return "http://127.0.0.1:8000"


@pytest.fixture(scope="function")
def user_payload():
    return {
        "name": "Oleg",
        "email": f"Oleg_{random.randint(1, 1000)}@gmail.com"
    }


@pytest.fixture(scope="function")
def create_user(base_url, user_payload):
    response = requests.post(f"{base_url}/users", json=user_payload)

    assert response.status_code == 201
    user_data = response.json()

    yield user_data

    requests.delete(f"{base_url}/users/{user_data['id']}")

@pytest.fixture(scope="module")
def auth_headers():
    return {"Authorization": "Bearer testtoken"}

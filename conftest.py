import random
import requests
import pytest
from faker import Faker
from api.users_api import create_user, delete_user


@pytest.fixture(scope="session")
def base_url():
    return "http://127.0.0.1:8000"


fake = Faker()
@pytest.fixture(scope="function")
def user_payload():
    return {
        "name": fake.first_name(),
        "email": f"{fake.user_name()}_{fake.random_int(1000, 9999)}@gmail.com"
    }


@pytest.fixture(scope="function")
def created_user(base_url, user_payload, headers=None):
    response = create_user(base_url, user_payload, headers=headers)
    assert response.status_code == 201

    data = response.json()
    user_id = data["id"]

    yield data

    delete_user(base_url, user_id, headers=auth_headers)


@pytest.fixture(scope="module")
def auth_headers():
    return {"Authorization": "Bearer testtoken"}

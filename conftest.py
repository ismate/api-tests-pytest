import random
import requests
import pytest
from faker import Faker
from api.users_api import create_user, delete_user
import os
from api.auth_api import register_user, login_user

@pytest.fixture(scope="session")
def base_url():

    return os.getenv("BASE_URL", "http://127.0.0.1:8000")


fake = Faker()
@pytest.fixture(scope="function")
def user_payload():
    return {
        "name": fake.first_name(),
        "email": f"{fake.user_name()}_{fake.random_int(1000, 9999)}@gmail.com"
    }


@pytest.fixture(scope="function")
def created_user(base_url, user_payload, auth_headers):
    response = create_user(base_url, user_payload, auth_headers)
    assert response.status_code == 201

    data = response.json()
    user_id = data["id"]

    yield data

    delete_user(base_url, user_id, headers=auth_headers)

@pytest.fixture(scope="function")
def auth_payload():
    return {
        "name": fake.first_name(),
        "email": f"{fake.user_name()}_{fake.random_int(1000, 9999)}@gmail.com",
        "password": "123456"
    }

@pytest.fixture(scope="function")
def auth_headers(base_url, auth_payload):
    register_user(base_url, auth_payload)
    response = login_user(base_url, auth_payload)

    token = response.json()["access_token"]

    return {"Authorization": f"Bearer {token}"}

@pytest.fixture(scope="function")
def registered_auth_user(base_url, auth_payload):
    response = register_user(base_url, auth_payload)

    assert response.status_code == 201
    return auth_payload

@pytest.fixture(scope="function")
def auth_token(base_url, registered_auth_user):
    response = login_user(base_url, registered_auth_user)

    assert response.status_code == 200

    return response.json()["access_token"]
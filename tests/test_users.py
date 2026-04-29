import pytest
from api.users_api import get_user, patch_user


def test_get_user_with_valid_headers(base_url, created_user, auth_headers):
    user_id = created_user["id"]

    response = get_user(base_url, user_id, headers=auth_headers)
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == user_id
    

def test_patch_non_existing_user(base_url, auth_headers):
    update_payload = {
        "name": "Ivan"
    }

    response = patch_user(base_url, 999, update_payload, headers=auth_headers)

    assert response.status_code == 404

    data = response.json()
    error = ErrorSchema(**data)
    assert "not found" in error.detail.lower()


def test_patch_user_with_invalid_data(base_url, created_user, auth_headers):
    user_id = created_user["id"]

    invalid_payload = {
        "name": "",
        "email": ""
    }

    patch_response = patch_user(base_url, user_id, invalid_payload, headers=auth_headers)
    assert patch_response.status_code == 422

    get_response = get_user(base_url, user_id, headers=auth_headers)
    assert get_response.status_code == 200

    data = get_response.json()

    assert data["name"] == created_user["name"]
    assert data["email"] == created_user["email"]

from schemas.user_schema import ErrorSchema

@pytest.mark.parametrize(
    "headers",
    [
        None,
        {"Authorization": "Bearer wrongtoken"},
    ],
    ids=["without_token", "invalid_token"]
)
def test_patch_user_without_token(base_url, created_user, headers):
    user_id = created_user["id"]

    payload = {
        "name": "Ivan"
    }

    response = patch_user(base_url, user_id, payload, headers=headers)

    assert response.status_code == 401
    
    data = response.json()
    error = ErrorSchema(**data)
    
    assert "unauthorized" in error.detail.lower()



@pytest.mark.parametrize(
    "payload, expected_status",
    [
        ({"name": "", "email": ""}, 422),
        ({"name": "Ivan", "email": "invalid_email"}, 422),
        ({"name": "Updated Name"}, 200),
    ],
    ids=["empty_fields", "invalid_email", "valid_partial_update"]
)
def test_patch_user_with_various_payloads(base_url, created_user, auth_headers, payload, expected_status):
    user_id = created_user["id"]

    response = patch_user(base_url, user_id, payload, headers=auth_headers)
    assert response.status_code == expected_status

    get_response = get_user(base_url, user_id, headers=auth_headers)
    assert get_response.status_code == 200

    user_data = get_response.json()

    if expected_status == 200:
        assert user_data["name"] == payload["name"]
    else:
        assert user_data["name"] == created_user["name"]
        assert user_data["email"] == created_user["email"]


from schemas.user_schema import UserSchema
from api.users_api import get_user

def test_get_user_schema(base_url, created_user, auth_headers):
    user_id = created_user["id"]

    get_response = get_user(base_url, user_id, headers=auth_headers)
    assert get_response.status_code == 200

    data = get_response.json()
    user = UserSchema(**data)
    assert user.id == user_id
    assert user.name == created_user["name"]
    assert user.email == created_user["email"]


def test_get_non_existing_user(base_url, auth_headers):
    get_response = get_user(base_url, 999, headers=auth_headers)

    assert get_response.status_code == 404

    data = get_response.json()
    error = ErrorSchema(**data)

    assert "not found" in error.detail.lower()


from api.users_api import get_users


def test_get_users_list_schema(base_url, created_user, auth_headers):
    response = get_users(base_url, headers=auth_headers)

    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)

    users = [UserSchema(**user) for user in data]

    assert any(user.id == created_user["id"] for user in users)

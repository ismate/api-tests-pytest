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
    assert "detail" in response.json()


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
    assert "detail" in response.json()


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

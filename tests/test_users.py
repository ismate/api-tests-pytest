from api.users_api import get_user, patch_user


def test_get_user_with_valid_headers(base_url, create_user, auth_headers):
    user_id = create_user["id"]

    response = get_user(base_url, user_id, headers=auth_headers)

    assert response.status_code == 200
    assert response.json()["id"] == user_id


def test_patch_non_existing_user(base_url, auth_headers):
    update_payload = {
        "name": "Ivan"
    }

    response = patch_user(base_url, 999, update_payload, headers=auth_headers)

    assert response.status_code == 404
    assert "detail" in response.json()


def test_patch_user_with_invalid_data(base_url, create_user, auth_headers):
    user_id = create_user["id"]

    invalid_payload = {
        "name": "",
        "email": ""
    }

    patch_response = patch_user(base_url, user_id, invalid_payload, headers=auth_headers)

    assert patch_response.status_code == 422

    get_response = get_user(base_url, user_id, headers=auth_headers)
    data = get_response.json()

    assert data["name"] == create_user["name"]
    assert data["email"] == create_user["email"]

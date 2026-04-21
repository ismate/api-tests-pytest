from api.users_api import get_user_request, patch_user_request


def test_user_with_headers(base_url, create_user):
    user_id = create_user["id"]

    headers = {
        "Authorization": "Bearer testtoken123"
    }

    get_response = get_user_request(base_url, user_id, headers=headers)

    assert get_response.status_code == 200
    assert get_response.json()["id"] == user_id


def test_invalid_headers_user(base_url, create_user):
    user_id = create_user["id"]

    headers = {
        "Authorization": ""
    }

    get_response = get_user_request(base_url, user_id, headers=headers)

    assert get_response.status_code == 401


def test_unexisting_user(base_url):
    update_payload = {
        "name": "Ivan"
    }

    headers = {
        "Authorization": "Bearer testtoken123"
    }

    patch_response = patch_user_request(base_url, 999, update_payload, headers=headers)

    assert patch_response.status_code == 404
    data = patch_response.json()
    assert "detail" in data


def test_invalid_user_data(base_url, create_user):
    user_id = create_user["id"]

    invalid_payload = {
        "name": "",
        "email": ""
    }

    headers = {
        "Authorization": "Bearer testtoken123"
    }

    patch_response = patch_user_request(base_url, user_id, invalid_payload, headers=headers)

    assert patch_response.status_code == 422

    get_response = get_user_request(base_url, user_id, headers=headers)
    data = get_response.json()

    assert data["name"] == create_user["name"]
    assert data["email"] == create_user["email"]
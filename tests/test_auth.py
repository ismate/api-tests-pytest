from api.auth_api import register_user, login_user, get_profile

def test_register_user_success(base_url, auth_payload):
    response = register_user(base_url, auth_payload)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == auth_payload["name"]
    assert data["email"] == auth_payload["email"]
    assert "password" not in data

def test_register_existing_email(base_url, auth_payload):
    register_user(base_url, auth_payload)
    response = register_user(base_url, auth_payload)

    assert response.status_code == 409

def test_login_success(base_url, registered_auth_user):
    response = login_user(base_url, registered_auth_user)

    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_login_with_wrong_password(base_url, registered_auth_user):
    payload = {
        "email": registered_auth_user["email"],
        "password": "wrong_password"
    }

    response = login_user(base_url, payload)

    assert response.status_code == 401

def  test_get_profile_with_valid_token(base_url, auth_token, registered_auth_user):
    response = get_profile(base_url, auth_token)

    assert response.status_code == 200

    data = response.json()
    assert data["name"] == registered_auth_user["name"]
    assert data["email"] == registered_auth_user["email"]

def test_get_profile_without_token(base_url):
    response = get_profile(base_url)

    assert response.status_code == 401

def test_get_profile_with_invalid_token(base_url):
    response = get_profile(base_url, "invalid_token")

    assert response.status_code == 401
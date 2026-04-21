import requests


def create_user_request(base_url, payload, headers=None):
    return requests.post(f"{base_url}/users", json=payload, headers=headers)


def get_user_request(base_url, user_id, headers=None):
    return requests.get(f"{base_url}/users/{user_id}", headers=headers)


def patch_user_request(base_url, user_id, payload, headers=None):
    return requests.patch(f"{base_url}/users/{user_id}", json=payload, headers=headers)


def delete_user_request(base_url, user_id, headers=None):
    return requests.delete(f"{base_url}/users/{user_id}", headers=headers)
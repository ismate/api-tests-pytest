import requests


def create_user(base_url, payload, headers=None):
    return requests.post(f"{base_url}/users", json=payload, headers=headers)


def get_user(base_url, user_id, headers=None):
    return requests.get(f"{base_url}/users/{user_id}", headers=headers)


def update_user(base_url, user_id, payload):
    return requests.patch(f"{base_url}/users/{user_id}", json=payload)


def delete_user(base_url, user_id):
    return requests.delete(f"{base_url}/users/{user_id}")

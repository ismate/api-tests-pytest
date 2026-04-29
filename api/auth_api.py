import requests

def register_user(base_url, payload):
    return requests.post(f"{base_url}/register", json=payload)

def login_user(base_url, payload):
    return requests.post(f"{base_url}/login", json=payload)

def get_profile(base_url, token=None):
    headers = None
    if token:
        header = {"Authorization": f"Bearer{token}"}

    return requests.get(f"{base_url}/profile", headers=headers)
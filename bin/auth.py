# auth.py

import logging
from .client import FiremonClient

logger = logging.getLogger(__name__)

class Auth:
def __init__(self, client: FiremonClient):
self.client = client

def login(self, username: str, password: str):
"""Authenticate and retrieve token."""
path = "/login"
payload = {
"username": username,
"password": password
}
response = self.client.post(path, json=payload)
token = response.get("token")
if token:
self.client.set_token(token)
return response

def logout(self):
"""Invalidate current session."""
path = "/logout"
return self.client.post(path)

def get_current_user(self):
"""Get details of the currently authenticated user."""
path = "/users/me"
return self.client.get(path)

def refresh_token(self):
"""Refresh session token."""
path = "/refresh"
return self.client.post(path)

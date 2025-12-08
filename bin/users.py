# users.py

from .utils import FiremonApiRequest

class Users:
def __init__(self, token, base):
self.token = token
self.base = base

def list(self, filter=None):
"""
List all users with optional filter.

:param filter: Dictionary of filter parameters
:return: List of user records
"""
endpoint = f"{self.base}/users"
return FiremonApiRequest.get(self.token, endpoint, params=filter)

def get(self, user_id):
"""
Retrieve a specific user by ID.

:param user_id: User identifier
:return: User details
"""
endpoint = f"{self.base}/users/{user_id}"
return FiremonApiRequest.get(self.token, endpoint)

def create(self, data):
"""
Create a new user.

:param data: Dictionary with user data
:return: Created user
"""
endpoint = f"{self.base}/users"
return FiremonApiRequest.post(self.token, endpoint, json=data)

def update(self, user_id, data):
"""
Update an existing user.

:param user_id: User identifier
:param data: Dictionary with updated user data
:return: Updated user
"""
endpoint = f"{self.base}/users/{user_id}"
return FiremonApiRequest.put(self.token, endpoint, json=data)

def delete(self, user_id):
"""
Delete a user by ID.

:param user_id: User identifier
:return: API response
"""
endpoint = f"{self.base}/users/{user_id}"
return FiremonApiRequest.delete(self.token, endpoint)

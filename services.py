# services.py

from .utils import FiremonApiRequest

class Services:
def __init__(self, token, base):
self.token = token
self.base = base

def list(self, filter=None):
"""
List all services with optional filters.

:param filter: Optional dictionary of filter parameters
:return: List of services
"""
endpoint = f"{self.base}/services"
return FiremonApiRequest.get(self.token, endpoint, params=filter)

def get(self, service_id):
"""
Retrieve a specific service by ID.

:param service_id: Service identifier
:return: Service details
"""
endpoint = f"{self.base}/services/{service_id}"
return FiremonApiRequest.get(self.token, endpoint)

def create(self, data):
"""
Create a new service.

:param data: Dictionary of service attributes
:return: Created service
"""
endpoint = f"{self.base}/services

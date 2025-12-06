# client.py

import requests
import logging

logger = logging.getLogger(__name__)

class FiremonClient:
def __init__(self, base_url: str, token: str = None, verify_ssl: bool = True, proxies: dict = None):
self.base_url = base_url.rstrip('/')
self.token = token
self.verify_ssl = verify_ssl
self.session = requests.Session()
self.proxies = proxies or {}

def set_token(self, token: str):
self.token = token

def _headers(self):
headers = {'Content-Type': 'application/json'}
if self.token:
headers['Authorization'] = f'Bearer {self.token}'
return headers

def get(self, path: str, params: dict = None):
url = f"{self.base_url}{path}"
logger.debug(f"GET {url} with params {params}")
response = self.session.get(
url, headers=self._headers(), params=params,
verify=self.verify_ssl, proxies=self.proxies
)
response.raise_for_status()
return response.json()

def post(self, path: str, json: dict = None):
url = f"{self.base_url}{path}"
logger.debug(f"POST {url} with json {json}")
response = self.session.post(
url, headers=self._headers(), json=json,
verify=self.verify_ssl, proxies=self.proxies
)
response.raise_for_status()
return response.json()

def put(self, path: str, json: dict = None):
url = f"{self.base_url}{path}"
logger.debug(f"PUT {url} with json {json}")
response = self.session.put(
url, headers=self._headers(), json=json,
verify=self.verify_ssl, proxies=self.proxies
)
response.raise_for_status()
return response.json()

def delete(self, path: str):
url = f"{self.base_url}{path}"
logger.debug(f"DELETE {url}")
response = self.session.delete(
url, headers=self._headers(),
verify=self.verify_ssl, proxies=self.proxies
)
response.raise_for_status()
return response.json()

# config.py

import os

class FiremonConfig:
def __init__(self, base_url=None, token=None, verify_ssl=True, proxies=None):
self.base_url = base_url or os.getenv("FIREMON_BASE_URL", "https://firemon.local")
self.token = token or os.getenv("FIREMON_TOKEN")
self.verify_ssl = verify_ssl
self.proxies = proxies or self._default_proxies()

def _default_proxies(self):
return {
"http": os.getenv("HTTP_PROXY", ""),
"https": os.getenv("HTTPS_PROXY", "")
}

def as_dict(self):
return {
"base_url": self.base_url,
"token": self.token,
"verify_ssl": self.verify_ssl,
"proxies": self.proxies
}

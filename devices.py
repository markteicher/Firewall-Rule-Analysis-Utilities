# devices.py

import requests

class DeviceManager:
def __init__(self, config):
self.base_url = config.base_url
self.headers = {
"Authorization": f"Bearer {config.token}",
"Content-Type": "application/json"
}
self.verify_ssl = config.verify_ssl
self.proxies = config.proxies

def list_devices(self):
url = f"{self.base_url}/sm/devices"
response = requests.get(url, headers=self.headers, verify=self.verify_ssl, proxies=self.proxies)
response.raise_for_status()
return response.json()

def get_device(self, device_id):
url = f"{self.base_url}/sm/devices/{device_id}"
response = requests.get(url, headers=self.headers, verify=self.verify_ssl, proxies=self.proxies)
response.raise_for_status()
return response.json()

def get_device_rules(self, device_id):
url = f"{self.base_url}/sm/devices/{device_id}/rules"
response = requests.get(url, headers=self.headers, verify=self.verify_ssl, proxies=self.proxies)
response.raise_for_status()
return response.json()

def get_device_interfaces(self, device_id):
url = f"{self.base_url}/sm/devices/{device_id}/interfaces"
response = requests.get(url, headers=self.headers, verify=self.verify_ssl, proxies=self.proxies)
response.raise_for_status()
return response.json()

# policy.py

import requests

class PolicyManager:
def __init__(self, config):
self.base_url = config.base_url
self.headers = {
"Authorization": f"Bearer {config.token}",
"Content-Type": "application/json"
}
self.verify_ssl = config.verify_ssl
self.proxies = config.proxies

def list_policies(self):
url = f"{self.base_url}/sm/policies"
response = requests.get(url, headers=self.headers, verify=self.verify_ssl, proxies=self.proxies)
response.raise_for_status()
return response.json()

def get_policy(self, policy_id):
url = f"{self.base_url}/sm/policies/{policy_id}"
response = requests.get(url, headers=self.headers, verify=self.verify_ssl, proxies=self.proxies)
response.raise_for_status()
return response.json()

def get_policy_rules(self, policy_id):
url = f"{self.base_url}/sm/policies/{policy_id}/rules"
response = requests.get(url, headers=self.headers, verify=self.verify_ssl, proxies=self.proxies)
response.raise_for_status()
return response.json()
